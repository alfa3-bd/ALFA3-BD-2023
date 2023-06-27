#Info: Rodar fora do container

import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
#options.add_argument('--headless')
options.add_argument('--disable-gpu')

options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
service = ChromeService(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://localhost:85/")

def find_response(logs):
    for entry in logs:
        if entry["message"]:
            log = json.loads(entry["message"])['message']
            try:
                response_received = log['method'] == 'Network.responseReceived'
                if response_received:
                    return str(log['params']['response']['status'])
                    
            except:
                pass

def test_response():
    assert "200" in find_response(driver.get_log("performance"))


