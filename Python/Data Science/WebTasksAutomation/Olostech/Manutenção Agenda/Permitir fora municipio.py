# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:35:21 2018

@author: Allan Krueger (klimber.mail@gmail.com)

O objetivo deste script é ativar a permissão de usuários fora do município em todas as agendas
abertas do Centrinho.

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import time
from subprocess import Popen
from bs4 import BeautifulSoup as bsoup
import csv

#Variáveis do código
OlostechPath = "../SaudeTech.exe"

#Pegando a hora de início da execução
start = time()

#Abrindo o google-chrome com a porta de Debug ativa, chamando o de chrome
chrome = Popen('chrome --remote-debugging-port=9222')

#Criando um arquivo de configuranção do Selenium para trabalhar na Debug
#port do chrome
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Conectando o selenium no chrome, chamando a conexão de driver
driver = webdriver.Chrome(chrome_options=chrome_options)

#Abrindo Olostech, chamando-o de olos
olos = Popen(OlostechPath)
#Esperando abrir a aba do Olostech e instruindo o driver a controlá-la
while(True):
    try:
        driver.switch_to.window(driver.window_handles[1])
        break
    except:
        pass

#Esperando a tela de login
WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@desc="Nome de Acesso"]')))

#Aguardando o usuário fazer login e o aparecimento da tela de seleção de Unidades
WebDriverWait(driver, 180).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="lstUnidades"]')))

#Selecionando a unidade
driver.find_element_by_xpath('//select[@name="lstUnidades"]/option[contains(text(),"Centrinho")]').click()
driver.find_element_by_name("btnConfirmar").click()

#Selecionando o ambiente clínica
WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="lstAmbientes"]')))
driver.find_element_by_xpath('//select[@name="lstAmbientes"]/option[contains(text(),"Clínica")]').click()
driver.find_element_by_name("btnConfirmar").click()

#Trocando para o frame do menu lateral e escrolhendo "Agendar"
WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.ID, "menuLeft")))
driver.switch_to.frame(driver.find_element_by_id("menuLeft"))
driver.find_element_by_link_text("Agenda Local...").click()
driver.find_element_by_link_text("Agendar").click()
#No frame principal, lendo a lista de profissionais (leio a partir desse menu pois aqui aparecem somente os que tem agenda)
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_name("main"))
#Lendo a lista de profissionais em texto
profissionais = [profissional.text for profissional in driver.find_elements_by_xpath('//*[@id="lstProfissionais"]/option')]
profissionais.pop(0) #Removendo a opção "Todos"

#Abrindo o menu de Administração
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_id("menuLeft"))
driver.find_element_by_link_text("Administração...").click()

#Para cada profissional com agenda
for profissional in profissionais:
    #Escolhe manutenção
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_id("menuLeft"))
    driver.find_element_by_link_text("Manutenção").click()
    #Clica no profissional e gera o relatório
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_name("main"))
    driver.find_element_by_xpath('//*[@id="lstProfissionais"]/option[text()="'+profissional+'"]').click()
    driver.find_element_by_name('btnGerar').click()

    #Encontra todos as agendas com "Editar"
    for i in range(len(driver.find_elements_by_link_text("Editar"))):
        driver.find_elements_by_link_text("Editar")[i].click()
        driver.switch_to.window(driver.window_handles[2])
        if driver.find_element_by_name("chkAL_AgendaOutrosMunicipios").get_property("checked") is False:
            driver.find_element_by_name("chkAL_AgendaOutrosMunicipios").click()
        driver.find_element_by_name("btnSalvar").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.switch_to.frame(driver.find_element_by_name("main"))

#Ao chegar ao final, fecha a ligação do selenium no chrome
driver.quit()
#Encerra o olostech
olos.terminate()
#Encerra o chrome
chrome.terminate()
#Imprime a quatidade de segundos entre a hora atual e o inicial
print(time()-start)