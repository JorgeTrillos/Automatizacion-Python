from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="D:\Python_Automatizacion\chromedriver_win32/chromedriver.exe") 
driver.get("https://psi.icbf.gov.co/entregaraciones/seguimiento")
wait = WebDriverWait(driver,10)
time.sleep(4)
driver.find_element_by_id("identificacion").send_keys("900221578")
driver.find_element_by_id("password").send_keys("n6115SLj03")
time.sleep(2)
btniniciar = driver.find_element_by_xpath("/html/body/app-root/body/div/app-login/div/form/button")
btniniciar.click()
time.sleep(2)
acompañamiento = driver.find_element_by_xpath("/html/body/app-root/body/app-nav-menu/header/nav/div/div/div/ul/li[3]/a")
acompañamiento.click() 
time.sleep(2)
#Seccion 1
Regional = driver.find_element_by_id("mat-select-8")
Regional.click()
time.sleep(2)
wait.until(driver.find_element_by_id())
Bgta = driver.find_element_by_xpath("//*[@id="'cdk-overlay-0'"]")
Bgta.click()
time.sleep(2)
Vg = driver.find_element_by_id("mat-select-9")
Vg.click()
time.sleep(2)
#Seccion 2
Fecha = driver.find_element_by_id("mat-option-26")
Fecha.click()
time.sleep(2)
Contrato = driver.find_element_by_id("mat-select-2")
Contrato.click()
time.sleep(2)
Data = driver.find_element_by_id("mat-option-29")
Data.click()
time.sleep(2)

