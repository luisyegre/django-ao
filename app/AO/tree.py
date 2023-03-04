# clase nodo el seencarga de dar niveles al arbol binario
# guarda el valor el cual es una lista

class Node:
    left = None
    right = None
    value = []
    size = None
    def add(self,size=None,value=None):
        node = Node()
        node.value = [value]
        node.size = size
        if size>self.size:
            self.right = node
        else: 
            self.left = node

    def next(self,size):
        if size > self.size:
            return self.right
        else:
            return self.left

#appo tree es la estructura de datos que se encargara de realizar la busqueda binaria para reducir los tiempos
#agrupa en cada nodo un nivel el cual es el entero resultante de unir el dia-mes-año como diamesaño (01/01/2020)=(1012020)
#cuando coniciden lo coloca en la lista de los mismos valores

class AppoTree:
    __head:Node = None
    cache = {} 
    def move_and_do(self,path,fn):
        def _move(node):
            while node.next(path)!=None:
                if path == node.size :
                    return fn(node)
                node = node.next(path)
            return fn(node)
        return _move(self.__head)
    @property    
    def head(self):
        return self.__head
    
    @head.setter
    def head(self,vl):
        n = Node()
        n.value = [vl]
        n.size = int(str(vl.date).replace('-',''))
        self.__head = n
   
    def find(self, size):
        value = self.move_and_do(size, lambda node: node)        
        self.cache[size]=value
        return value
    
    def append(self,appo):
        size = int(str(appo.date).replace('-',''))
        def _append(node):  
            if node.size ==size:
                return node.value.append(appo) 
            return node.add(size=size,value=appo)

        self.move_and_do(size, _append)
  