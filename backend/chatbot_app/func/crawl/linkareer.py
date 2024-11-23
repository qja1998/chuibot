# linkareer.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tqdm import tqdm

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 1)

def url_crawl(keyword='', organizatio_name='', role=''):
    pbar = tqdm()

    results = []
    for page in range(1):
        url = f"https://linkareer.com/cover-letter/search?keyword={keyword}&organizationName={organizatio_name}&page={page}&role={role}&sort=PASSED_AT"
        try:
            driver.get(url)
        except:
            break
        detail_info_list = get_detail(driver)
        results.extend(detail_info_list)
        pbar.update()
    pbar.close()
    driver.close()
    return results

def get_detail(driver:webdriver.Chrome):
    detail_info_list = []
    
    detail_info = {}
    
    first_box_list_url = f'//*[@id="__next"]/div[1]/div/div[4]/div/div/section[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/a'
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, first_box_list_url)))
    
    first_box = driver.find_elements(By.XPATH, first_box_list_url)[0]
    first_box.click()
    
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]')))

    # print(info_box_list[0].text)

    title_path = '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/h1'
    subtitle_path = '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/h3'
    content_path = '//*[@id="coverLetterContent"]/main'

    title=driver.find_element(By.XPATH, title_path)
    subtitle=driver.find_element(By.XPATH, subtitle_path)
    content=driver.find_element(By.XPATH, content_path)
    detail_info['title'] = title.text # 지원자 정보
    detail_info['subtitle'] = subtitle.text # 지원자 스펙
    detail_info['content'] = content.text # 지원자 자소서
    detail_info_list.append(detail_info)

    for i in range(2, 21):
        detail_info = {}
        info_box_path = f'//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]/div[{i}]/a'
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, info_box_path)))
        info_box = driver.find_element(By.XPATH, info_box_path)
        info_box.click()
        
        # driver.execute_script(f"window.scrollTo(0, {160*i})")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, title_path)))
        
        title=driver.find_element(By.XPATH, title_path)
        subtitle=driver.find_element(By.XPATH, subtitle_path)
        content=driver.find_element(By.XPATH, content_path)
        detail_info['title'] = title.text # 지원자 정보
        detail_info['subtitle'] = subtitle.text # 지원자 스펙
        detail_info['content'] = content.text # 지원자 자소서
        # print()
        # print(info_box_path)
        # print(title.text)
        detail_info_list.append(detail_info)

    return detail_info_list


if __name__ == '__main__':
    import json

    results = url_crawl('삼성')

    print(len(results))
    for result in results:
        print(result['title'])
    
    with open("crawl_test.json", 'w') as f:
        json.dump({'result': results}, f, ensure_ascii=False)