# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:08:38 2019

@author: Allan Krueger (klimber.mail@gmail.com)
"""
#Com este script, tentarei obter as datas de início e fim do processo licitatório

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import time, sleep
from subprocess import Popen
import csv

#Variáveis do código
csvRelatorio = "Datas Licitações.csv"
processos = []

#Pegando a hora de início da execução
start = time()

with open(csvRelatorio, "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Licitação', 'Data Inicial', 'Data Final'])

with open("Pasta1.csv") as f: #Lê o csv de processos
    reader = csv.reader(f)
    for row in reader:
        processos.extend(row)

driver = webdriver.Chrome() #Abrindo o chrome
driver.get("https://portalsei.joinville.sc.gov.br/") #Acessando a página da Intranet
driver.find_element_by_xpath('//*[@alt="Usuário Interno"]').click() #Acessando "Usuário interno"
driver.close() #Fechando a aba anterior
driver.switch_to.window(driver.window_handles[0]) #Definindo para controlar a nova aba

#Aguardando o usuário fazer login e o aparecimento do menu lateral
WebDriverWait(driver, 180).until(expected_conditions.visibility_of_element_located((By.ID, "main-menu")))

#Acessando a pagina de pesquisa
driver.find_element_by_xpath('//*[@id="main-menu"]//a[.="Pesquisa"]').click()

#Para cada processo licitatório
for processo in processos:
    #Preenche os campos da pesquisa
    driver.find_element_by_class_name("infraText").clear()
    driver.find_element_by_class_name("infraText").send_keys(processo)
    driver.find_element_by_class_name("ms-choice").click()
    driver.find_element_by_xpath('//label[contains(text(), "PMJ")]').click()
    driver.find_element_by_class_name("ms-choice").click()
    driver.find_element_by_xpath('//*[@id="selTipoProcedimentoPesquisa"]/option[.="Suprimentos - Processo Licitatório"]').click()
    driver.find_element_by_xpath('//*[@id="selSeriePesquisa"]/option[.="Aviso de Licitação"]').click()
    driver.find_element_by_id("sbmPesquisar").click()
    try:
        #Acessa o consultar andamento
        driver.switch_to.frame("ifrArvore")
        driver.find_element_by_xpath('//img[@title="Consultar Andamento"]').click()
        #Pega as datas inicial e final
        driver.switch_to.parent_frame()
        driver.switch_to.frame("ifrVisualizacao")
        dataFinal = driver.find_element_by_xpath('//table[@id="tblHistorico"]/tbody/tr[2]').text.split(" ")[0]
        dataInicial = driver.find_elements_by_xpath('//table[@id="tblHistorico"]/tbody/tr')[-1].text.split(" ")[0]
        with open(csvRelatorio, "a", newline='',encoding='utf-8') as csvfile: #Abre o csv em modo de adição
            writer = csv.writer(csvfile)
            writer.writerow([processo, dataInicial, dataFinal])
    except:
        sleep(5)
    finally:
        #Volta para a página de pesquisa
        driver.switch_to.parent_frame()
        try:
            driver.find_element_by_xpath('//*[@id="main-menu"]//a[.="Pesquisa"]').click()
        except:
            driver.find_element_by_id("lnkInfraMenuSistema").click()
            driver.find_element_by_xpath('//*[@id="main-menu"]//a[.="Pesquisa"]').click()

#Ao chegar ao final, fecha a ligação do selenium no chrome
driver.quit()
#Imprime o tempo de execução
duracao = int(time() - start)
print("Tempo de execução: {}min {}seg.".format(int(duracao/60),duracao%60))