#!/usr/bin/env python3
data = ("Kushal Das", "India", "Python")
name, country, language = data
print("name = %s, country = %s, language = %s" % (name, country, language))

name = "Kushal"
language = "Python"
msg = "{0} loves {1}.".format(name, language)
print(msg)

msg = f"{name} loves {language}"
print(msg)