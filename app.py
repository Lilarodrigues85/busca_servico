#conceito-de-seletores

#- XPATH
#- EMAIL://input[@id='session_key']
#- SENHA://input[@id='session_password']
#BTN://button[normalize-space(text())='Entrar']
#-PESQUISA-JOBS-://header//input
#-LINKS DA PESQUISA://main//div/div//ul//li//a[@data-control-id]
#CSS-SELECTOR-:main div.jobs search results list

#INTALAR-PACOTES

#REALIZAR-O-PASSO-A-PASSO-ALGORITMO

from selenium import webdriver


print("Vamos começar a buscar suas vagas")
search = input("Digite sua Busca: ")


browser = webdriver.Chrome()
browser.get("")