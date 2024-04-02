from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep


#Código instância o webdriver, e verifica se consegue acessar a URL do local host
driver = webdriver.Chrome()

driver.set_page_load_timeout(5)

try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessou a página com sucesso")
except TimeoutException:
    print("Tempo de carregamento da página excedeu o limite")
finally:
    driver.quit()