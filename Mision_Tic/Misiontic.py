from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox(executable_path="D:\Python_Automatizacion\geckodriver-v0.30.0-win64\geckodriver.exe")

def funcion():
#Ingresa al login de google
 driver.get("https://accounts.google.com/signin/v2/identifier?hl=es&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
 driver.find_element_by_id("identifierId").send_keys("sjtrillos@uninorte.edu.co")
 next = driver.find_element_by_id("identifierNext")
 next.click()
 time.sleep(3)
 driver.find_element_by_name("password").send_keys("Jo.12357864")
 btnpasw = driver.find_element_by_id("passwordNext")
 btnpasw.click()
 time.sleep(4)
 # Abre la url uninorte, y nos abre la clase.
 driver2 = driver
 driver2.get("https://misiontic.uninorte.edu.co/ultra/courses/_800_1/outline")
 time.sleep(1)
 butt = driver.find_element_by_id("agree_button")
 butt.click()
 driver.find_element_by_name("user_id").send_keys("sjtrillos")
 driver.find_element_by_name("password").send_keys("Jo.12357864")
 btn = driver.find_element_by_id("entry-login")
 btn.click()
 time.sleep(5)
 btn_clas = driver.find_element_by_class_name("editable-title-container")
 btn_clas.click()
 time.sleep(2)
 btn_clas2 =  driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[2]/ng-switch/div/bb-folder/div/div[2]/div[1]/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div/div[1]/div[1]/div/ng-switch/div/div[2]/div[1]/bb-content-item-course-outline/div/div[1]/ng-switch/div/a")
 btn_clas2.click()
#Apartado del meet
 time.sleep(5)
 btn_micro = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
 btn_micro.click()

try:
    funcion()
except TimeoutException:
    print("Ejecutando de nuevo")
    funcion()

  