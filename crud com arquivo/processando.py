import os

# Inicializar a lista
lista = []

# Definir o caminho do arquivo
diretorio_destino = os.path.join(os.getcwd(), "crud com arquivo")
fileName = os.path.join(diretorio_destino, "livrosAleatoriosERepetidos.txt")

# Ler o arquivo e preencher a lista
tamanho_bloco = 1024

# Função para processar o arquivo em blocos
with open(fileName, 'r') as file:
    buffer = ""
    
    while True:
        # Ler um bloco do arquivo
        bloco = file.read(tamanho_bloco)
        
        # Se o bloco estiver vazio, atingimos o fim do arquivo
        if not bloco:
            # Processa o restante do buffer
            if buffer:
                livros = buffer.split(',')
                lista.extend(livro.strip() for livro in livros)
            break
        
        # Adicionar o conteúdo do bloco ao buffer
        buffer += bloco
        
        # Processar linhas completas (divididas por vírgula)
        while ',' in buffer:
            # Encontrar a primeira ocorrência da vírgula
            livro, buffer = buffer.split(',', 1)
            # Adicionar o livro à lista
            lista.append(livro.strip())

# Exibir a lista de livros

opcao = input("Digite 1 para imprimi ")

if opcao == 1:
    print(lista)



