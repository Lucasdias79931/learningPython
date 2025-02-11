class hashtable:
    def __init__(self, size = 100):
        self.size = size
        self.lista = [[] for _ in range(self.size)]
    
    def _hash(self, key):
            if not key:
                return None
            
            return len(key) % self.size

    def _push(self, key, value):
        

        index = self._hash(key)

        self.lista[index].append(value)
    def _get(self, key):
        index = self._hash(key)

        

