from selenium import webdriver
import time
# driver = webdriver.Chrome('C:/Users/sj/Downloads/chromedriver.exe')
# driver = webdriver.Chrome('C:/Users/YG/Downloads/chromedriver.exe')
driver = webdriver.Chrome('D:/python37/Scripts/chromedriver.exe')
driver.get('http://www.baidu.com')
# driver.find_element_by_name('wd').send_keys('妇联 金高\n')
# driver.find_element_by_id('su').click()
# driver.find_element_by_link_text('下载').click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# # driver.find_element_by_partial_link_text('登').click()

driver.save_screenshot('C:/Users/tengy/Desktop/test.png')

driver.quit()
