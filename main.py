from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
import os
import json
import pathlib

print("iniciando")

email = ""
password = ""

print("Baixando imagem")
valor = random.randint(0, 100000)

response = requests.get("https://www.thiswaifudoesnotexist.net/example-" + str(valor) + ".jpg")
#response = requests.get("https://thispersondoesnotexist.com/image")
if (response.status_code == 200):
    file = open("profile.png", "wb")
    file.write(response.content)
    file.close()
    print("Imagem salva")

print("Carregando configurações")
with open('login.json') as json_file:
    data = json.load(json_file)
    email = data['email']
    password = data['password']

print("Iniciando Driver")
options = Options()
#options.add_argument("--start-minimized")
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
browser = webdriver.Firefox(options=options)

print("Abrindo discord")
browser.get('https://discord.com/app')

time.sleep(3)

print("Autenticando")
inputEmail = browser.find_element_by_name("email")
inputEmail.send_keys(email)
time.sleep(1)

inputPassword = browser.find_element_by_name("password")
inputPassword.send_keys(password)

time.sleep(1)
print("Login")
inputPassword.send_keys(Keys.ENTER)

try:
    time.sleep(5)
    print("Fechando pop-up")
    browser.find_element(By.XPATH, "//*[@aria-label='Fechar']").click()
except Exception as e:
    pass

time.sleep(5)
print("Abrindo configurações")
browser.find_element(By.XPATH, "//*[@aria-label='Configurações de Usuário']").click()

time.sleep(3)
print("Aterando perfil")
botoesEditarPerfil = browser.find_elements_by_class_name("button-38aScr")
for botaoEditarPerfil in botoesEditarPerfil:
    try:
        if botaoEditarPerfil.text == 'Edit User Profile':
            botaoEditarPerfil.click()
    except:
        pass

browser.find_element_by_class_name("fileInput-23-d-3").click()

time.sleep(3)
print("Anexando arquivo")
inputs = browser.find_elements_by_class_name("file-input")
for input in inputs:
    try:
        if '.jpg,.jpeg,.png,.gif' in input.get_attribute('accept'):
            input.send_keys(str(pathlib.Path(__file__).parent.absolute()) + "\\profile.png")
    except:
        pass

time.sleep(3)
print("Aplicando foto")
browser.find_element(By.XPATH, "//*[text()='Aplicar']").click()

time.sleep(3)
print("Salvando alterações")
browser.find_element(By.XPATH, "//*[text()='Salvar alterações']").click()

print("Saindo")
time.sleep(2)

browser.close()