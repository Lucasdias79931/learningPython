lista = []

for element in range(0,10):
    lista.append(element)

tamanho = len(lista)
ocorrencia = lista.count(4)
index = lista.index(6)


dados = f"tamanho: {tamanho}\nocorrencia de 4: {ocorrencia}\nindex do 4: {index}"

print(dados)