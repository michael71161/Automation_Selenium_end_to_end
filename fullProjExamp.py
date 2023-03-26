from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains #import to make actiones like hover 
import time

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window() #to make large browser window

#adding implicitly wait, may be redused
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice")
action = ActionChains(driver) #to do actions

time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click() #go to shop , using partially href 
time.sleep(3)
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']") #grab all prod elements
#now prod holds the whole element we need grab name from the prod(which is the parent now)
#we want to add blackberry to the cart
for prod in products:
    productName = prod.find_element(By.XPATH, "div/h4/a").text #our root page now is card not the whole page so prod.find
    if productName == "Blackberry":
        prod.find_element(By.XPATH, "div/button").click() #click add to cart 

time.sleep(3)
#now click on checkout 
driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click() #click on checkout
time.sleep(3)
#no Israel in ship to country, we will choose Ukraine
#its take time to countru to load so we will use exeplicit wait 
driver.find_element(By.ID,"country").send_keys("uk")
time.sleep(3)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Ukraine"))) #wait until ukraine present in the search results on the bar

driver.find_element(By.LINK_TEXT,"Ukraine").click() #select Ukraine
time.sleep(5)
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click() #click on checkbox - agree of terms
time.sleep(3)    
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click() #click on purchase
time.sleep(3)

#now as assertion we want to grab the success message - if we have it and it the same as should be- purchase comleted
successMsg= driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text #grab the message 
#now parcially assert instead of entire text part of it
assert "Success! Thank you!" in successMsg , "there is problem with porchuse confirm"

driver.close()