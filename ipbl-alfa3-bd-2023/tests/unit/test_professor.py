from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


username = "999.999.999-99"
password = "123"


def simulate_login():

    driver = webdriver.Chrome("chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    service = ChromeService(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost:85/professor/login")
    driver.find_element("name", "identificador_professor").send_keys(username)
    driver.find_element("name", "senha_professor").send_keys(password)
    driver.find_element("name", "login").click()

    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    logged = driver.find_element(By.CSS_SELECTOR,"span.b-title").get_attribute("innerHTML")
    return logged


def test_login():
    assert "Página do Professor" in simulate_login()



