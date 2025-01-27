import hashlib
import os

def insertHash(password: str) -> str:
    hashstr = hashlib.sha512(password.encode()).hexdigest()
    return hashstr

here = os.getcwd()

pessoas = os.path.join(here, "Pessoas.txt")

try:
    
    email = input("Digite o email:")
    password = input("Digite a senha:")
    password = insertHash(password)

    
    with open(pessoas, "a") as file:
        file.write(f"Email: {email}\nPassword: {password}\n")
    print("Dados do usuário inseridos com sucesso!")
except FileExistsError as e:
    print(e)
except Exception as e:
    print(e)