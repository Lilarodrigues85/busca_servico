from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

app = Flask(__name__)

# Função para ler credenciais de um arquivo
def read_credentials(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split(":")
            credentials[key] = value
        return credentials

file_path_credentials = "credentials.txt"
credentials = read_credentials(file_path_credentials)

@app.route('/search', methods=['POST'])
def search_jobs():
    data = request.json
    search = data.get('title')

    print("Iniciando busca por vagas:", search)

    # Iniciar a navegação
    browser = webdriver.Chrome()
    browser.get("https://www.linkedin.com/")
    sleep(2)

    login = browser.find_element(By.XPATH, "/html/body/main/section[1]/div/div/a")
    login.click()
    sleep(2)

    email = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    btn_enter = browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[4]/button")
    sleep(2)

    email.send_keys(credentials['user'])
    password.send_keys(credentials['senha'])
    sleep(2)
    
    btn_enter.click()
    sleep(5)

    browser.get("https://www.linkedin.com/jobs")
    input_jobs_search = browser.find_element(By.XPATH, "//header//input")
    sleep(5)
    
    input_jobs_search.send_keys(search)
    sleep(5)
    input_jobs_search.send_keys(Keys.ENTER)
    sleep(5)

    ul_element = browser.find_element(By.CSS_SELECTOR, "main div.jobs-search-results-list")
    sleep(5)

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
                "titulo": link.text  # Coleta o texto visível do link
            }
            links.append(job_data)
        
        print(len(links))
        if len(links) >= 25:
            print(f"Chegamos ao número esperado de {len(links)}")
            break

    browser.quit()
    
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
