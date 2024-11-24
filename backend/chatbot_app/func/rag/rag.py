import os
from .document_store import NewsDocumentStore
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, SystemMessage, BaseChatMessageHistory
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv
import requests
import re
from bs4 import BeautifulSoup as bs
from pprint import pprint

# Load environment variables
load_dotenv()

class StreamHandler(BaseCallbackHandler):
    def __init__(self):
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        # print(self.text, end="\r")

def initialize():
    """Initialize document store and language model."""
    doc_store = NewsDocumentStore.from_existing("news_documents")
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.7,
        streaming=True,
        # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    )
    return doc_store, llm

def search_documents(doc_store, query: str, k: int = 3):
    """Search for relevant documents."""
    try:
        return doc_store.similarity_search(query, k=k)
    except Exception as e:
        print(f"Error during search: {str(e)}")
        return []

def extract_company(query: str, llm) -> str:
    """Extract company name from user input."""
    system_prompt = "Extract the company name from the user's input. 오직 회사 이름만을 단어로 출력"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Input: {query}")
    ]
    
    try:
        response = llm.invoke(messages)
        return response.content.strip()
    except Exception as e:
        print(f"Error during company name extraction: {str(e)}")
        return "Error extracting company name."

def extract_jobrole(query: str, llm) -> str:
    """Extract company name from user input."""
    system_prompt = "Extract the jobrole name from the user's input. 최소한의 단어로 명확하고 간결하게 job role word 만을 출력"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Input: {query}")
    ]
    
    try:
        response = llm.invoke(messages)
        return response.content.strip()
    except Exception as e:
        print(f"Error during company name extraction: {str(e)}")
        return "Error extracting company name."

def clean(text):
    i = text.find('글자수')
    text = text[:i]
    return text.strip()

def get_company_recruit(search_keyword):
    base_url = "https://www.jobkorea.co.kr/starter/PassAssay"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f"{base_url}?schTxt={search_keyword}", headers=headers)
    soup = bs(response.text, 'html.parser')
    items = [item.select('.txBx') for item in soup.select('#container > div.stContainer > div.starListsWrap.ctTarget > ul > li')]

    if not items or not items[0]:
        return None
    
    qna_texts = []
    sources = []
    for item in items:
        item_id = re.findall("\d{6}", item[0].select('a')[0].attrs['href'])[0]
        response_ans = requests.get(f"{base_url}/View/{item_id}", headers=headers)
        soup_ans = bs(response_ans.text, 'html.parser')
        
        questions = [q.select_one('.tx').text for q in soup_ans.select('#container > div.selfQnaWrap > dl > dt')]
        answers = [clean(a.select_one('.tx').text) for a in soup_ans.select('#container > div.selfQnaWrap > dl > dd')]
        
        sources.append(f"{base_url}/View/{item_id}")
        for q, a in zip(questions, answers):
            qna_texts.append(f"Question: {q} \nAnswer: {a}")
    
    return "\n".join(qna_texts), sources

def generate_answer(query: str, relevant_docs: list, llm, stream_handler):
    """Generate answer using GPT model based on documents and user query."""
    
    jobrole_name = extract_jobrole(query, llm)
    company_name = extract_company(query, llm).replace(' ', '')
    print(f"Company name extracted: {company_name}")
    
    company_qna = get_company_recruit(company_name)
    if company_qna is None:
        recruit_sources = []
        context = "Context:\n"
    else:
        company_qna, recruit_sources = company_qna
        context = f"QnA: {company_qna}\nContext:\n"

    context = "Context:\n"
    sources = []
    for i, doc in enumerate(relevant_docs, 1):
        print(i, doc)
        sources.append(doc['metadata']['url'])
        context += f"{i}. {doc['title']}\n{doc['content']}\n"

    system_prompt = """
    당신은 모두를 합격시키는 취업 전문가입니다. 주어진 {context}와 QnA(합격자 자기소개서)를 분석하고 사용자에게 취업 컨설팅을 해주세요.
    - {context}에서 기업에 취업 하기 위한 정보를 요약해 취업에 도움을 줄 수 있습니다.
        - 사용자가 원하는 산업, 기업, 직무와 유사하거나 연관있는 내용들을 제공
    - 자기소개서 작성법을 묻는 {question}에는 QnA를 기반으로 취업한 사람들의 자기소개서를 분석하여 많이 나온 문항과 그 문항에 대한 답을 분석하여 요약해 제공합니다.
        - 만약 QnA가 주어지지 않았다면 기업명을 요구
        - 가끔은 당신이 중요할 것 같은 질문을 던질 수도 있습니다.
    * 답변은 한국어로 작성하며, 취업을 위한 자기소개서/면접에 도움이 될 내용 정확하고 자세하게 알려주세요.
    example:
    Q: {company}
    A: {company}는 {context}한 상황입니다.
        **취업 준비를 위한 팁**: {company}와 같은 기업에 지원할 때는 {recommend} 한 것들을 신경쓰는 것이 좋습니다.
        **성공 사례**:
        {q}에 대한 문항에,
        합격자들은 {a}라고 답했습니다.
        그러므로 당신은 {solution}을 염두에 두고 준비할 수 있습니다.
    Q: {question}
    A: 
    """

    # 메시지 구성
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""
        다음 docs를 참고하여 제가 이 기업에 취업하는데 필요한 정보를 알려주세요.
        docs: {context}
        
        질문: {query}""")
    ]
    
    # try:
    # GPT로 스트리밍 답변 생성 (invoke 메소드 사용)
    response = llm(
        messages,
        callbacks=[stream_handler]
    )
    sources = list(set(sources))
    recruit_sources = list(set(recruit_sources))
    return response.content, {'news_src': sources, 'recruit_src': recruit_sources}, company_name, jobrole_name
    
    # except Exception as e:
    #     print(f"Error generating answer: {str(e)}")
    #     return "Sorry, there was an error generating an answer."

def main():
    doc_store, llm = initialize()
    chat_history = []
    
    print("Welcome to ChuiBBOt! Ask your questions or type 'exit' to quit.")
    
    while True:
        # query = input("Your question: ")
        query = "삼성전자 가고 싶어요"
        if query.lower() == "exit":
            break
        
        chat_history.append({"role": "user", "content": query})
        
        print("Searching for relevant documents...")
        results = search_documents(doc_store, query)
        
        print("Generating answer...")
        stream_handler = StreamHandler()
        answer = generate_answer(query, results, llm, stream_handler)
        chat_history.append({"role": "assistant", "content": answer})
        
        print("\nChuiBBOt's Answer:")
        print(answer)
        
        print("\nDo you want to continue? (Type 'exit' to quit or ask another question.)")
        break

if __name__ == "__main__":
    main()
