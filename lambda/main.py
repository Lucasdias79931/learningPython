lista = [

    {'nome':'lucas', 'sobrenome': 'santos'},
    {'nome':'ana', 'sobrenome': 'santos'},
    {'nome':'paula', 'sobrenome': 'santos'},
    {'nome':'maria', 'sobrenome': 'santos'},
]


lista.sort(key = lambda item : item['nome'])


for i in lista:
    for key, value in i.items():
        print(f'{key}: {value}')
        
    print("\n")