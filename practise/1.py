from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
import requests
import dotenv
dotenv.load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
driver = webdriver.Chrome()
driver.get('https://aviso.bz/login')
driver.find_element(By.XPATH, '//input', name="username").send_keys(user)
driver.find_element(By.XPATH, '//input', name="password").send_keys(password)
driver.find_element(By.XPATH, '//button').click()