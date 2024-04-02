from selenium import webdriver
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    #Inicializar o streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    #Iniciar o web driver com o chrome
    #yeld serve para o processo ficar rodando sem parar, se passar o return ele finaliza a função
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    yield driver

    #Fechar o webdrive e o streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    #Verificar se a pagina abre
    driver.get("http://localhost:8501")
    sleep(5)