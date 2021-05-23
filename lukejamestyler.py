from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

options = Options()
options.add_argument("--window-size = 1920,1080")

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver = webdriver.Chrome(options = options)
driver.get("https://github.com/lukejamestyler")

folder = driver.find_element_by_xpath("//img [@alt = 'Luke James Tyler']")  #xpath :   //*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div/article/p[1]/a/img
actionchains = ActionChains(driver)                                         # nie wiem, p co chodzi.tamto xpath zrobił nakladka
ActionChains(driver).double_click(folder).perform()