def qsort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        esquerda = []
        meio = []
        direita = []
        
        for elemento in lista:
            if elemento < pivo:
                esquerda.append(elemento)
            elif elemento == pivo:
                meio.append(elemento)
            else:
                direita.append(elemento)
        
        return qsort(esquerda) + meio + qsort(direita)
