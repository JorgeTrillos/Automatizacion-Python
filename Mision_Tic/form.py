from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as panda


driver = webdriver.Chrome(executable_path="D:\Python_Automatizacion\chromedriver_win32/chromedriver.exe") 
driver.get("https://forms.gle/FFHefSFyzsgZgvBP8")
wait = WebDriverWait(driver,10)