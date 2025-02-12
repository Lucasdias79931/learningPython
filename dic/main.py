Pessoas = []

while True:
    pessoa = {'nome': '','sobrenome': '','idade':None,'profissão':''}
    
    for atributo in pessoa:
        pessoa[atributo] = input(f"\nDigite o(a) {atributo} da pessoa: ")
        
    Pessoas.append(pessoa)
    controle = input("s para sair")
    if controle == 's' or controle == 'S':
        break

for element in Pessoas:
    for atributo in element.values():
        print(atributo)
        
    print("\n")




