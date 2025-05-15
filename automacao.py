from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Abre chrome
navegador = webdriver.Chrome()
espera = WebDriverWait(navegador, 10)


# Abre SmartSync e bota em tecla cheia
navegador.get("https://smartsync.app.br")
navegador.maximize_window()

# Seleciona email, senha e preenche
navegador.find_elements(By.TAG_NAME, "input")[1].send_keys("testeteste")
navegador.find_elements(By.TAG_NAME, "input")[0].send_keys("unifg@gmail.com")

#seleciona e procura o botao de conectar
navegador.find_element(By.TAG_NAME, "button").click()

# Espera o botão "Contratos" aparecer e ser clicável
espera.until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/contracts']/button[contains(text(), 'Contratos')]"))).click()

#clica no contrato UNIFG 
navegador.find_element(By.XPATH, "//a[@href='/unifg_contract']").click()

#clica bloco1
navegador.find_element(By.XPATH, "//a[@href='/bloco1']").click()

#seleciona data e hora
navegador.find_elements(By.TAG_NAME, "input")[0].send_keys("10/10/2025")
navegador.find_elements(By.TAG_NAME, "input")[1].send_keys("12:30")

#liga switch
navegador.find_elements(By.TAG_NAME, "label")[0].click()
time.sleep(1.5)

#selecionar andar
navegador.find_elements(By.TAG_NAME, "select")[0].click()
navegador.find_elements(By.TAG_NAME, "option")[1].click()

#preenche dispositivo do 2º andar
navegador.find_elements(By.TAG_NAME, "input")[0].send_keys("10/10/2025")
navegador.find_elements(By.TAG_NAME, "input")[1].send_keys("12:30")
navegador.find_elements(By.TAG_NAME, "label")[0].click()
time.sleep(1.5)

navegador.find_element(By.XPATH, "//a[@href='/about']/button[contains(text(), 'Sobre')]").click()
time.sleep(1.5)

#clica em desconectar
navegador.find_element(By.LINK_TEXT, "Desconectar").click()
time.sleep(1)
