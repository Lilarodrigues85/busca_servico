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
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import json

#funcao buscar credenciais
def read_credentials(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()

        credentials ={}
        for line in lines:
            key, value = line.strip().split(":")
            credentials[key] = value
        return credentials

file_path_credentials = "credentials.txt"

credentials = read_credentials(file_path_credentials)


print("Vamos comecar a buscar suas vagas")
search = input("Digite sua Busca: ")


#iniciar-a-navegacao
browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/")
sleep(2)

login = browser.find_element(By.XPATH,"/html/body/main/section[1]/div/div/a")
login.click()
sleep(2)
email = browser.find_element(By.ID,"username")
password = browser.find_element(By.ID,"password")
btn_enter = browser.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[4]/button")
sleep(2)
email.send_keys(credentials['user'])
password.send_keys(credentials['senha'])
sleep(2)
btn_enter.click()
sleep(5)
browser.get("https://www.linkedin.com/jobs")
input_jobs_search = browser.find_element(By.XPATH,"//header//input")
sleep(5)
input_jobs_search.send_keys(search)
sleep(5)
input_jobs_search.send_keys(Keys.ENTER)
sleep(5)
ul_element = browser.find_element(By.CSS_SELECTOR,"main div.jobs-search-results-list")
sleep(5)


def scroll_list(pixels):
    browser.execute_script(f"arguments[0].scrollTop+={pixels};",ul_element)
    sleep(2)

links = []

for _ in range(25):
    scroll_list(200)
    link_elements = browser.find_elements(By.XPATH, "//main//div/div//ul//li//a[@data-control-id]")
    
    for link in link_elements:
        job_data = {
            "url": link.get_attribute("href"),
            "titulo": link.text  # Isso coleta o texto visível do link (caso haja)
        }
        links.append(job_data)
    
    print(len(links))
    if len(links) >= 25:
        print(f"Chegamos ao numero esperado de {len(links)}")
        break

# Salvar os links organizados em um arquivo JSON
with open("job_links.json", "w") as json_file:
    json.dump(links, json_file, indent=4, ensure_ascii=False)

print("Links organizados salvos em job_links.json")


# #vamos criar nossa planilha
# spreadsheet = Workbook()

# sheet = spreadsheet.active

# sheet['A1'] = "NOME DA VAGA"
# sheet['B1'] = "LINK DA VAGA"

# next_line = sheet.max_row + 1

# for link in links:
#     text = link.text
#     url_link = link.get_attribute("href")

#     sheet[f'A{next_line}'] = text
#     sheet[f'B{next_line}'] = url_link

#     next_line+= 1

# spreadsheet.save("vagas_links"+search+".xlsx")
# print("planilha criada")
# print("Encerrando busca")
# sleep
browser.quit()
