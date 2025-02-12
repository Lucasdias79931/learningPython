
def isprimo(number):
    if number < 2:
        return False
    if number == 2:
        return True  

    if number % 2 == 0:
        return False  

    for i in range(3, number, 1):  
        if number % i == 0:
            return False  

    return True


lista = [numero for numero in range(10)]


lista2 = [n for n in lista if n%2 == 0]
lista3 = [n for n in lista if n%2 == 1]

primos = [n for n in lista if isprimo(n)]

primosImp = [n for n in lista if isprimo(n) and n%2 ==1]
primosPar = [n for n in lista if isprimo(n) and n%2 ==0]
print(f"somente par:{lista2}\nsomente impar:{lista3}")

print("primos:", primos)
print(f"primos pares:{primosPar}\nprimos Imp:{primosImp}")



