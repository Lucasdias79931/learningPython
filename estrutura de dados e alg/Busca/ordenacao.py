class Busca_ordenacao:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def qsort(arr):
        if len(arr) < 2:
            return arr
        else:
            pivo = arr[0]
            menores = []
            maiores = []
            for i in range(1, len(arr)): 
                if arr[i] <= pivo:
                    menores.append(arr[i])
                else:
                    maiores.append(arr[i])
            
            return Busca_ordenacao.qsort(menores) + [pivo] + Busca_ordenacao.qsort(maiores)
    
    @staticmethod
    def bsort(arr):
        for i in range(0, len(arr) -1):
            for j in range(1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]




## testes
if __name__  == "__main__":
    arr = [["lucas","ana","claudia"], ["marley", "xela","ana"], [5,2,0,-1,-4,-5],[0,3,4,5,6,7,8,8,9,0],[True,False]]

    ARR = [Busca_ordenacao.qsort(sublista) for sublista in arr]

    print(ARR)

