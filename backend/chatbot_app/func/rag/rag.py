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

def extract_company(query: str) -> str:    
    """Extract company name from user input."""

    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.1,
        streaming=True,
    )

    system_prompt = "사용자 입력에서 회사 이름을 추출해서 오직 회사 이름만을 ','로 구분하여 단어로 출력. 회사 이름이 없다면 아무 답도 하지 않을 것"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Input: {query}")
    ]
    
    try:
        response = llm.invoke(messages)
        print(response.content)
        return response.content.strip()
    except Exception as e:
        print(f"Error during company name extraction: {str(e)}")
        return "Error extracting company name."

def extract_jobrole(query: str) -> str:
    """Extract company name from user input."""

    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.1,
        streaming=True,
    )


    system_prompt = "사용자 입력에서 취업 키워드(명사)를 추출해서 최소한의 단어로 ','로 구분하여 명확하고 간결하게 키워드만을 출력. 취업과 관련된 키워드(명사)가 없다면 아무 답도 하지 않을 것"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Input: {query}")
    ]
    
    try:
        response = llm.invoke(messages)
        print(response.content)
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

def emotion(docs: str) -> str:
    """Extract company name from user input."""

    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.1,
        streaming=True,
    )


    system_prompt = """
    기업에 대한 문서가 주어집니다.
    이 문서에서 키워드(명사)를 모두 추출하여 긍정적인 단어와 부정적인 단어를 출력합니다.
    ** 무조건 아래의 형태를 지켜 출력하세요. **
    output: 긍정적단어1, 긍정적단어2, 긍정적단어3 / 부정적단어1, 부정적단어2, 부정적단어3
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Input: {docs}")
    ]
    
    try:
        response = llm.invoke(messages)
        print(response.content)
        return response.content.strip()
    except Exception as e:
        print(f"Error during company name extraction: {str(e)}")
        return "Error extracting company name."

def generate_answer(hope:str, query: str, relevant_docs: list, llm, stream_handler):
    """Generate answer using GPT model based on documents and user query."""
    
    keywords = extract_jobrole(query).split(', ')
    company_names = extract_company(query).split(', ')
    print(f"Keywords name extracted: {keywords}")
    print(f"Company name extracted: {company_names}")
    
    for company_name in company_names:
        company_qna = get_company_recruit(company_name)
        if company_qna is None:
            recruit_sources = []
            context = "Context:\n"
        else:
            company_qna, recruit_sources = company_qna
            context = f"QnA: {company_qna}\nContext:\n"

    sources = []
    for i, doc in enumerate(relevant_docs, 1):
        print(f"{i}. {doc['title']}\n{doc['content'][:50]}\n")
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
        관심사: {hope}
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

    emotion_result = emotion(context).split(':')[1]
    emotion_result = {'pos':emotion_result.split('/')[0].strip().split(', '),
                      'nag':emotion_result.split('/')[1].strip().split(', ')}
    print('emotion', emotion_result)

    return response.content, {'news_src': sources, 'recruit_src': recruit_sources}, company_names, keywords, emotion_result
    
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
