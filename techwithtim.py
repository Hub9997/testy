from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

driver.get('http://techwithtim.net')

print(driver.title)  # Title of the page
# search = driver.find_element_by_name("s")  #działa
# search = driver.find_element_by_class_name("search-field") działa
# search = driver.find_element_by_xpath('//*[@id="search-2"]/form/label/input')
search = driver.find_elements_by_css_selector('search-2.content')

search.send_keys("test")
search.send_keys(Keys.ENTER)
time.sleep(5)
print(driver.current_url)

driver.close()
