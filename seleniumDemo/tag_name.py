from selenium import webdriver
import time

# driver = webdriver.Chrome('C:/Users/sj/Downloads/chromedriver.exe')
driver = webdriver.Chrome('C:/Users/YG/Downloads/chromedriver.exe')
# driver.fullscreen_window()
driver.get("http://baidu.com")
elements = driver.find_elements_by_tag_name('a')
# print(elements)
try:
    for element in elements:
        if '新闻' in element.text:
            element.click()
except:
    print('it\'s ok')