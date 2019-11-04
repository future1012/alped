from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome('C:/Users/sj/Downloads/chromedriver.exe')
# driver = webdriver.Chrome('C:/Users/YG/Downloads/chromedriver.exe')
dirver = webdriver.Chrome('D:/python37/Scripts/chromedriver.exe')
dirver.get('http://timeanddate.com')
dirver.maximize_window()

dirver.find_element_by_id('boxyear').clear()
dirver.find_element_by_id('boxyear').send_keys('1985')

monthElements=dirver.find_element_by_id('month')
months=Select(monthElements)
months.select_by_visible_text('十二月')
# print(monthElements)

countryElements=dirver.find_element_by_id('country')
print(countryElements)
print(type(countryElements))
countries=Select(countryElements)
countries.select_by_visible_text('China')

dirver.find_element_by_xpath("//input[@value='View Calendar']").click()

# monthelements=dirver.find_element_by_id('')

time.sleep(15)
dirver.close()