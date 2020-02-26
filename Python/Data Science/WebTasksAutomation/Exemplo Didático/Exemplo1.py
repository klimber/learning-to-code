#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:08:33 2018

@author: Allan Krueger (klimber.mail@gmail.com)
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from time import time
import csv

start = time() #Marcando o tempo de início da execução

driver = webdriver.Chrome() #Iniciando o chrome com o selenium

driver.get("https://www.w3schools.com/html/html_tables.asp") #Indicando para navegar até a página

table = driver.find_element_by_id("customers") #Encontrando a tabela com id=customers

table = table.get_attribute("outerHTML") #Pegando todo o HTML dela

table = BeautifulSoup(table,"html.parser").find("table", attrs={"id":"customers"}) #Usa o html parser do BeautifulSoup nele

dataset = [] #Inicializando um dataset vazio

#Encontra a primeira linha (table row)("tr") da tabela, nessa linha, encontra todos os cabeçalhos (table header)("th")
#Pega o texto de cada cabeçalho, remove espaços desnecessários, e forma um array
#Adiciona esse array no dataset, assim cada array formará uma nova linha
dataset.append([th.get_text().strip() for th in table.find("tr").find_all("th")])

# Para cada linha (table row)("tr") da tabela(menos a linha 0, que foi os headers)
# Encontra todos os dados (table data)("td"), e forma um array com eles
# Adiciona esse array no dataset, assim cada array formará uma nova linha
for row in table.find_all("tr")[1:]:
    dataset.append([td.get_text().strip() for td in row.find_all("td")])

#Agora que o dataset está completo, escrevemos o arquivo
with open("Relatorio.csv", "w", newline='') as csvfile: #Abrindo o arquivo em modo de escrita
    writer = csv.writer(csvfile) #Chamando a função de escrever neste csv de writer
    
    for data in dataset: #Para cada array presente no Dataset
        writer.writerow(data) #Escreve o array no CSV

driver.quit() #Fecha o Chrome e o selenium
print(start - time()) #Imprime a diferença entre o tempo inicial e o atual (ou seja, o tempo que o script levou)