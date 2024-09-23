lista = [numero for numero in range(10)]

lista2 = [n for n in lista if n%2 == 0]
lista3 = [n for n in lista if n%2 == 1]
lista2.reverse()

lista = []
for i in range((len(lista2)+len(lista3))//2):
    lista.append(lista2.pop())
    lista.append(lista3.pop())

print(lista)

    

