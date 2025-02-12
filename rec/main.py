def reverse(lista: list, left, right) -> None:
    lista[left], lista[right] = lista[right], lista[left]
    if left < right:
        reverse(lista, left + 1, right - 1)


lista = [1,2,3,4,5,6,7,8,9,10]
reverse(lista, 0, len(lista) -1)
print(lista)