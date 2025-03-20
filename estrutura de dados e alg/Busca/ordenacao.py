class Busca_ordenacao:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def qsort(arr, l, r):
        def partition(arr, l, r):
         
            pivot = arr[r]
            i = l - 1  

            for j in range(l, r):
                
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]  

            
            arr[i + 1], arr[r] = arr[r], arr[i + 1]
            return i + 1
        
        if l < r:
            
            pi = partition(arr, l, r)
            
            Busca_ordenacao.qsort(arr, l, pi - 1)
            Busca_ordenacao.qsort(arr, pi + 1, r)
        
    
        
    @staticmethod
    def bsort(arr):
        for i in range(0, len(arr) -1):
            for j in range(1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]




## testes
if __name__  == "__main__":
    arr = [["lucas","ana","claudia"], ["marley", "xela","ana"], [5,2,0,-1,-4,-5],[0,3,4,5,6,7,8,8,9,0,-5,-7,-9,-8,-5,-6,-6],[True,False]]

    for sublista in arr:
        Busca_ordenacao.qsort(sublista, 0, len(sublista) - 1)


    print(arr)

