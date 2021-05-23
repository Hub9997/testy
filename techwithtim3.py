from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

driver.get('http://techwithtim.net')

print(driver.title)  # Title of the page
search = driver.find_element_by_name("s")  # działa
# search = driver.find_element_by_class_name("search-field") działa
# search = driver.find_element_by_xpath('//*[@id="search-2"]/form/label/input')
# search = driver.find_elements_by_css_selector('search-2.content') nie działa

search.send_keys("test")
search.send_keys(Keys.ENTER)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID, "main"))
    print(main.text)
except:
    driver.quit()
articles = driver.find_elements_by_tag_name("article")
for article in articles:
    header = article.find_element_by_class_name("entry-summary")
    print(header.text)
print(main.text)
time.sleep(5)
print(driver.current_url)

driver.quit()
