#!/usr/bin/env python3
amount = float(input("Inserir valor: "))
inrate = float(input("Inserir taxa de juros: "))
period = int(input("Insira o período: "))
value = 0
year = 1

while year <= period:
    value = amount + (inrate * amount)
    print("Ano %d Rs. %.2f" % (year,value))
    amount = value
    year = year + 1