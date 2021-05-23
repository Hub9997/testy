from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

driver.get('https://www.w3schools.com/')

link = driver.find_element_by_link_text("Raport")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID, "accept-choices"))
    

    element.click()
    driver.back()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.LINK_TEXT, "Poinformuj nas"))
    element.click()



except:
    pass

#print(driver.title)