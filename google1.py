from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.current_url)
element = driver.find_element_by_xpath("//*[@id='zV9nZe']/div")  # //*[@id="zV9nZe"]/div   
#driver.get("https://www.google.com/?gws_rd=ssl")
#driver.find_element_by_name("Zgadzam się").click()
#driver.find_element_by_xpath("//*[@id="introAgreeButton"]/span/span")
#element = driver.find_element_by_name("introAgreeButton") NoSuchElementException:Unable to locate element:
#element = driver.find_element_by_name("Zgadzam się") Unable to locate element
#driver.find_element_by_class_name("RveJvd snByac").click()
driver.maximize_window()
actions = ActionChains(driver)
actions.move_to_element(element)
actions.click(element).perform()
#actions.perform()
#element.click()



#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"Zgadzam się"))).click()

"""
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"inpNumber"))).send_keys('190')
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"inpStreet"))).send_keys('ELI HARTLEY')
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"btSearch"))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"tr.SearchResults"))).click()
"""