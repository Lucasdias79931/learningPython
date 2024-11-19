#https://docs.python.org/3/library/re.html
import re


# findall search sub
# compile 

string = "Este é um teste de expressões teste regulares"

print(re.search(r'teste', string))

print(re.findall(r'teste2', string))

print(re.sub(r'teste', 'TESTE', string))

regexp = re.compile(r'teste2')

print(regexp.search(string),regexp.findall(string),regexp.sub('TESTE', string))

