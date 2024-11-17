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
from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    user = data['user']
    senha = data['senha']
    search_query = data['search']

    # Configurar o navegador com webdriver-manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)

    # Acessar o LinkedIn e fazer login
    browser.get("https://www.linkedin.com/")
    sleep(2)
    login = browser.find_element(By.XPATH, "/html/body/main/section[1]/div/div/a")
    login.click()
    sleep(2)
    email = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    btn_enter = browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[4]/button")
    email.send_keys(user)
    password.send_keys(senha)
    btn_enter.click()
    sleep(5)

    # Buscar vagas
    browser.get("https://www.linkedin.com/jobs")
    wait = WebDriverWait(browser, 10)  # Espera até 10 segundos
    input_jobs_search = wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))
    input_jobs_search.send_keys(search_query)
    input_jobs_search.send_keys(Keys.ENTER)

    wait = WebDriverWait(browser, 10)
    ul_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jobs-search-results-list")))

    # Função para rolar a lista de vagas
    def scroll_list(pixels):
        browser.execute_script(f"arguments[0].scrollTop+={pixels};", ul_element)
        sleep(2)

    links = []
    for _ in range(25):
        scroll_list(200)
        link_elements = browser.find_elements(By.XPATH, "//main//div/div//ul//li//a[@data-control-id]")
        for link in link_elements:
            job_data = {
                "url": link.get_attribute("href"),
                "titulo": link.text
            }
            links.append(job_data)
        if len(links) >= 25:
            break

    browser.quit()

    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)



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
