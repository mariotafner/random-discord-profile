from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

import time
import random
import requests
import os

import json

email = ""
password = ""

print("iniciando")

valor = random.randint(0, 100000)

response = requests.get("https://www.thiswaifudoesnotexist.net/example-" + str(valor) + ".jpg")
if (response.status_code == 200):
    file = open("profile.png", "wb")
    file.write(response.content)
    file.close()

with open('login.json') as json_file:
    data = json.load(json_file)
    email = data['email']
    password = data['password']

options = Options()
#options.add_argument("--start-minimized")
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
browser = webdriver.Firefox(options=options)

browser.get('https://discord.com/app')

time.sleep(3)

inputEmail = browser.find_element_by_name("email")
inputEmail.send_keys(email)
time.sleep(1)

inputPassword = browser.find_element_by_name("password")
inputPassword.send_keys(password)

time.sleep(1)
inputPassword.send_keys(Keys.ENTER)

time.sleep(5)
browser.find_element(By.XPATH, "//*[@aria-label='Configurações de Usuário']").click()

time.sleep(3)
browser.find_element(By.XPATH, 
    "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/main/div/div[1]/div/div/div[1]/div[1]/div/input"
    ).send_keys("C:\\dev\\random-discord-profile\\profile.png")

time.sleep(3)
browser.find_element(By.XPATH, "//*[text()='Aplicar']").click()

time.sleep(3)
browser.find_element(By.XPATH, "//*[text()='Salvar alterações']").click()
time.sleep(2)

browser.close()




