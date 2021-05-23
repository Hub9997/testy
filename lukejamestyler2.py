#http://demo.guru99.com/test/simple_context_menu.html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

#cos = driver.find_elements_by_css_selector("#authentication > button") nie dziala
#xpath  //button[@ondbclick="myfunction()"]
#cos = driver.find_element_by_name("Double-Click Me To See Alert")
cos = driver.find_element_by_xpath("//button[@ondblclick='myFunction()']")

actionchains = ActionChains(driver)                                         # nie wiem, o co chodzi.tamto xpath zrobił nakladka
ActionChains(driver).double_click(cos).perform()

#selector #authentication > button

