from selenium import webdriver
import time
#chrome adds on     ChroPath
# driver = webdriver.Chrome('C:/Users/sj/Downloads/chromedriver.exe')
driver = webdriver.Chrome('C:/Users/YG/Downloads/chromedriver.exe')
# driver.fullscreen_window()
driver.get("http://www.women.org.cn")
driver.find_element_by_xpath("//a[@id='应用']").click()
