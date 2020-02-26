# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:40:38 2019

@author: Allan Krueger (klimber.mail@gmail.com)
"""
from fuzzywuzzy import fuzz, process

with open("HMSJ.txt", encoding="utf-8") as f: #Lê o csv de processos
    HMSJ = [row.strip() for row in f]

with open("ePublica.txt", encoding="utf-8") as f: #Lê o csv de processos
    ePublica = [row.strip() for row in f]

for i in range(len(HMSJ)):
    comp = process.extractOne(HMSJ[i], ePublica, scorer=fuzz.)
    print( "{} - {} - {}".format(comp[0], HMSJ[i], comp[1]))

teste = fuzz.utils.full_process(HMSJ[0])

teste = [palavra[0] for palavra in teste.split(" ") if len(palavra)>2]
