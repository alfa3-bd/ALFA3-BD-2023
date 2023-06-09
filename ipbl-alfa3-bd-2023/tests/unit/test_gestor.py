from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pymongo import MongoClient

username = "119.876.543-22"
password = "123"
pages = ["professores","alunos"]

driver = webdriver.Chrome("chromedriver")
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

service = ChromeService(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

def simulate_login():
    driver.get("http://localhost:85/gestor/login")
    driver.find_element("name", "identificador_gestor").send_keys(username)
    driver.find_element("name", "senha_gestor").send_keys(password)
    driver.find_element("name", "login").click()

    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    logged = driver.find_element(By.CSS_SELECTOR,"span.b-title").get_attribute("innerHTML")
    
    return logged

def access_list(page): 
    driver.get("http://localhost:85/gestor/"+page)
    msg = driver.find_element(By.CSS_SELECTOR,"H5").get_attribute("innerHTML")

    return msg.lower()

def add(page):
    driver.get("http://localhost:85/gestor/add_"+page)

    if page in "alunos":      
        driver.find_element("name", "fst_name_aluno").send_keys("Joaquim")
        driver.find_element("name", "scn_name_aluno").send_keys("Silveira")
        driver.find_element("name", "tipo").send_keys(1)
        driver.find_element("name", "turma").send_keys(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()        
    else:
        driver.find_element("name", "cpf").send_keys("356.222.333-20")
        driver.find_element("name", "fst_name_prof").send_keys("Ana Maria")
        driver.find_element("name", "scn_name_prof").send_keys("Ramos")
        driver.find_element("name", "password").send_keys("123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()  

    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    msg = driver.find_element(By.CSS_SELECTOR,"H5").get_attribute("innerHTML")
     
    return msg.lower()


def test_login():
    assert "Página do Gestor" in simulate_login()

def test_lists():
    for page in pages:
        assert page in access_list(page)

def test_add():
    for page in pages:
        assert page in add(page)


