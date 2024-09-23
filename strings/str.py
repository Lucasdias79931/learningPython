class ManipuladorString:
    def __init__(self, texto):
        self.texto = texto

    def upper(self):
        """Converte todas as letras para maiúsculas."""
        return self.texto.upper()

    def lower(self):
        """Converte todas as letras para minúsculas."""
        return self.texto.lower()

    def capitalize(self):
        """Converte o primeiro caractere para maiúscula e os demais para minúsculas."""
        return self.texto.capitalize()

    def count(self, substring):
        """Conta o número de ocorrências de uma substring."""
        return self.texto.count(substring)

    def find(self, substring):
        """Encontra a primeira ocorrência de uma substring."""
        return self.texto.find(substring)

    def rfind(self, substring):
        """Encontra a última ocorrência de uma substring."""
        return self.texto.rfind(substring)

    def startswith(self, substring):
        """Verifica se a string começa com uma substring."""
        return self.texto.startswith(substring)

    def endswith(self, substring):
        """Verifica se a string termina com uma substring."""
        return self.texto.endswith(substring)

    def split(self, separador):
        """Divide a string em uma lista de palavras."""
        return self.texto.split(separador)

    def join(self, lista_strings):
        """Junta uma lista de strings em uma única string."""
        return " ".join(lista_strings)

    def replace(self, substring_antiga, substring_nova):
        """Substitui todas as ocorrências de uma substring por outra."""
        return self.texto.replace(substring_antiga, substring_nova)

    def format(self, *args, **kwargs):
        """Formata a string com valores dinâmicos."""
        return self.texto.format(*args, **kwargs)


def invert(string):
    return string[::-1]

string = "ovo"

nova  = invert(string)

print(nova)


