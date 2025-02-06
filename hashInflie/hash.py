import hashlib
import os
import re

def insertHash(password: str) -> str:
    hashstr = hashlib.sha512(password.encode()).hexdigest()
    return hashstr

def writeData(outfile, data):
    try:
        with open(outfile, "a") as file:
            for key, value in data.items():
                file.write(f"{key}:{value}\n")
        print("Dados do usuário inseridos com sucesso!")
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(e)

def autentica(inputfile, passw):
    try:
        with open(inputfile, "r") as file:
            passw = hashlib.sha512(passw.encode()).hexdigest()
            dataAux = {}
            for line in file:
                key, value = line.strip().split(":")
                
                dataAux[key] = value
               
                if key == "Password":
                    if value == passw:
                        return dataAux
                    else:
                        dataAux.clear()

            return False
            
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(e)

data = autentica("Pessoas.txt", "gatocezar")

if data: 
    print("Autenticação bem sucedida")

    for key, value in data.items():
        print(f"{key}:{value}")
else:
    print("Pessoa não encontrada!")


