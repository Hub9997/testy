from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)   # działa
time.sleep(5)
assert "No results found." not in driver.page_source  # jak zrobię samo in, nie idzie dalej
driver.close()
