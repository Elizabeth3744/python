from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tkinter import Button


driver = webdriver.Chrome()
driver.get("https://identidad.mtess.gov.py/alumno/login.php")
web_element = driver.find_element(By.NAME, 'username')
web_element.send_keys("6542657")
web_element = driver.find_element(By.NAME, 'password')
web_element.send_keys("6542657tomterry"+ Keys.ENTER)
web_element  = driver.find_element(By.CLASS_NAME, "bs-welcome-header ")
web_element.click();
print(driver.title)
time.sleep(10)
driver.quit()