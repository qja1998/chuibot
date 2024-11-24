import os
import sys
import json
import urllib.request
import hashlib

def get_id(s: str):
    sha256_hash = hashlib.sha256()
    s = s.encode()
    sha256_hash.update(s)
    hash_result = sha256_hash.hexdigest()
    return hash_result

client_id = "0tMv4g2WDP16JIK879ki"
client_secret = "Gd9Tlfterv"

"""
{
        "lastBuildDate":"Thu, 21 Nov 2024 15:43:09 +0900",
        "total":3788958,
        "start":1,
        "display":2,
        "items":[
                {
                        "title":"<b>삼성<\/b>중공업, 완<b>전자<\/b>율운항 연구 선박 출항…기술 고도화 추진",
                        "originallink":"https:\/\/news.tf.co.kr\/read\/economy\/2153688.htm",
                        "link":"https:\/\/n.news.naver.com\/mnews\/article\/629\/0000340546?sid=101",
                        "description":""
                        "pubDate":"Thu, 21 Nov 2024 15:42:00 +0900"
                },
        ]
}
"""

def crawl_articles(query):
    result = {'articles':[]}
    id_list = []
    
    if not os.path.exists('./article_id.txt'):
        with open('./article_id.txt', 'w') as file:
            pass
            
    if not os.path.exists('./articles.json'):
        with open('./articles.json', 'w') as file:
            json.dump({"articles":[]}, file)
            
    with open('./article_id.txt', 'r') as file:
        lines = file.readlines()
        article_id_list = [line.strip() for line in lines]
    
    encText = urllib.parse.quote(query)
    for start in range(100):
        url = f"https://openapi.naver.com/v1/search/news?query={encText}&strat={start}&sort=date&display=100"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        try:
            response = urllib.request.urlopen(request)
        except:
            print(start)
            break
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)
            items = response_body['items']
        else:
            print("Error Code:" + rescode)
            return False
        
        articles = []
        for item in items:
            hash_id = get_id(item['originallink'])
            url = item['originallink']
            title = item['title']
            content = item['description']
            
            if hash_id in article_id_list:
                # print(hash_id)
                continue
            
            article = {
                'id': hash_id,
                'url': url,
                'title': title,
                'content': content,
            }
            article_id_list.append(hash_id)
            articles.append(article)
        
        result['articles'] += articles
    
    with open('./article_id.txt', 'w', encoding='utf-8') as file:
        for article_id in article_id_list:
            file.write(article_id+'\n')
    
    try:
        with open('./articles.json', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
            result['articles'] += existing_data.get('articles', [])
    except json.JSONDecodeError:
        existing_data = {"articles": []}
    
    with open('./articles.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent="\t", ensure_ascii=False)
    
    return len(result["articles"])

if __name__ == '__main__':
    company_list = ['삼성', '엘지', '현대그룹', '기업은행', '하나은행']
    domain_list = ['IT', '프로그래머', '개발자', 'AI 개발자']
    
    for company in company_list:
        for domain in domain_list:
            query = company + ' ' + domain
            print(query)
            print(crawl_articles(query))