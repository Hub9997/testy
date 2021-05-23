from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.google.com")
#element0 = driver.find_element_by_name("Zgadzam się")
#results = driver.find_elements_by_css_selector('.M9Bg4d > a:nth-child(1) > span:nth-child(3) > span:nth-child(1)')
results = driver.find_element_by_name("Szukaj")
driver.find_element_by_class_name("RveJvd snByac").click()
#<span class="RveJvd snByac">Zgadzam się</span>
#first_result = results[0]
#first_result.click()
#element = driver.find_element(By.ID,"Zgadzam się")

#element = driver.find_element_by_css_selector("#introAgreeButton > span:nth-child(3) > span:nth-child(1)")
#html body.EIlDfe div#yDmH0d.MCcOAc.IqBfM.ecJEib.EWZcud.cjGgHb.d8Etdd.LcUz9d c-wiz.SSPGKf.fkimef div.T4LgNb.eejsDc div.kFwPee div.cui-csn-data div.fkimef.I47yTd.k8Lt0 div div.OvJdSb.UTd6ef form.A28uDc div#introAgreeButton.U26fgb.O0WRkf.oG5Srb.HQ8yf.C0oVfc.wtr0xd.ic02He.M9Bg4d span.CwaK9 span.RveJvd.snByac
#actions = ActionChains(driver)
#actions.move_to_element(element)
#actions.click(on_element=element)
#actions.perform()
#element0.click()
#option.click()

#element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
#element.click()

element = driver.find_element_by_name("Szukaj")
#element2 = driver.find_element_by_xpath(/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input)
#trzeba jeszcze wcisnąć zgadzam się  #introAgreeButton > span:nth-child(3) > span:nth-child(1) Zgadzam się
#element.send_keys("Zgadzam się")
#element.send_keys("audi a4")


#element.send_keys("audi a4", Keys.ARROW_DOWN)