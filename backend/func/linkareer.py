# linkareer.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 2)

def url_crawl(keyword='', organizatio_name='', role=''):
    results = []
    for page in range(1,573):
        url = f"https://linkareer.com/cover-letter/search?keyword={keyword}&organizationName={organizatio_name}&page={page}&role={role}&sort=PASSED_AT"
        driver.get(url)
        detail_info_list = get_detail(driver)
        results.append(detail_info_list)
        break
    driver.close()
    return results

def get_detail(driver:webdriver.Chrome):
    detail_info_list = []
    
    detail_info = {}
    
    info_box_list_url = f'//*[@id="__next"]/div[1]/div/div[4]/div/div/section/div[2]/div/div[3]/div[1]'
    '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]'
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, info_box_list_url)))
    
    info_box_list = driver.find_elements(By.XPATH, info_box_list_url)
    
    info_box_list[0].click()
    
    info_box_list = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]')
    
    for info_box in info_box_list:
    
        
        title_url = '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/h1'
        subtitle_url = '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/h3'
        content_url = '//*[@id="coverLetterContent"]/main'
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, title_url)))
        
        title=driver.find_element(By.XPATH, title_url)
        subtitle=driver.find_element(By.XPATH, subtitle_url)
        content=driver.find_element(By.XPATH, content_url)
        detail_info['title'] = title.text # 지원자 정보
        detail_info['subtitle'] = subtitle.text # 지원자 스펙
        detail_info['content'] = content.text # 지원자 자소서
        driver.back()
        detail_info_list.append(detail_info)
    return detail_info_list


if __name__ == '__main__':
    results = url_crawl('삼성')
    print(len(results))
    print(results)
    for result in results:
        print(len(result))
        for info in result:
            print(info['title'])