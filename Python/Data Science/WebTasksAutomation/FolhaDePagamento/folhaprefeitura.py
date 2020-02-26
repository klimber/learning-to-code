#Este script usa python 3 acessa o site da prefeitura de joinville e acessa
#a ultima folha de pagamento, gerando um .csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

CPF = "Seu CPF"
Senha = "Sua Senha"


driver = webdriver.Firefox()
driver.get("https://www.joinville.sc.gov.br/splash/")
sleep(2)
assert "Joinville" in driver.title
driver.find_element_by_xpath('//*[@title="Acesso Rápido a Folha de Pagamento"]').click()
sleep(2)
driver.find_element_by_id("user").send_keys(CPF)
driver.find_element_by_id("pass").send_keys(Senha, Keys.RETURN)
sleep(2)
driver.find_element_by_xpath('//a[@href="/folha/folha/lista"]').click()
sleep(2)
driver.find_element_by_xpath('//a[@class="td_link"]').click()
sleep(2)
table = driver.find_element_by_xpath('//*[@width="670px"]')
with open('folhapagamento.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in table.find_elements_by_css_selector('tr'):
        wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
sleep(2)
driver.close()
