
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://github.com/login")


navegador.find_element('xpath' , '//*[@id="login_field"]').send_keys(" EMAIL DE LOGIN ") # Insira no campo seu email de login no github

navegador.find_element('xpath' , '//*[@id="password"]').send_keys(" SENHA ") # Insira no campo sua senha para o github

navegador.find_element('xpath' , '//*[@id="login"]/div[4]/form/div/input[13]').click()



sleep(10) # Tempo de visualização da página


navegador.quit()
