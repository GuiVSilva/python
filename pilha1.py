from Node import Node

# Stack:
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0: #Verifica antes se a pilha esta vazia
            node = self.top #Salvo uma copia do ultimo item
            self.top = self.top.next #troco o ultimo item da pilha pelo penultimo
            self._size = self._size - 1 #Diminuo o tamanho da pilha
            return node.data
        raise IndexError("The Stack is Empty!")

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

#Criando 4 pilhas vazias
pilha1 = Stack()
pilha2 = Stack()
pilha3 = Stack()
pilha4 = Stack()

# Verifica se o codigo inputado é igual a um dos códigos que já estão na pilha
# Se for encontrado na pilha, retorna 1
# Se não for encontrado na pilha, retorna 0
def procurar_codigo(codigo, pilha):
    exiteCodigo = 0
    for i in range(len(pilha)):
        cod_da_pilha = pilha.pop()
        pilha.push(cod_da_pilha)
        if codigo == cod_da_pilha:
            exiteCodigo = 1
    return exiteCodigo

while True:
    codigo = str(input("DIGITE O CODIGO QUE DESEJA ADICIONAR, OU -1 PARA TERMINAR: "))
    
    if codigo == "-1":
        break
    
    # Procurar codigo nas 4 pilhas
    codigo_encontrado = (procurar_codigo(codigo, pilha1)) + (procurar_codigo(codigo, pilha2)) + (procurar_codigo(codigo, pilha3)) + (procurar_codigo(codigo, pilha4))

# Se for encontrado em alguma pilha:    
    if codigo_encontrado > 0:
        print("Esse codigo ja exite.")
  
    else:
    # Se nao for encontrado, então pode salvar o codigo na pilha que tiver espaço
        if (len(pilha1) < 3):
            pilha1.push(codigo)
        elif (len(pilha2) < 3):
            pilha2.push(codigo)
        elif (len(pilha3) < 3):   
            pilha3.push(codigo)
        elif (len(pilha4) < 3):
            pilha4.push(codigo)
        else:
            print("Todos as pilhas estao cheias.")
  

while True:
    # Procurar codigo nas 4 pilhas se existe o codigo ou se possivel remover
    codigo = str(input("DIGITE O CODIGO QUE DESEJA REMOVER, OU -1 PARA TERMINAR: "))
    
    if codigo == "-1":
        break
    #Procurar codigo nas 4 pilhas    
    codigo_encontrado = (procurar_codigo(codigo, pilha1)) + (procurar_codigo(codigo, pilha2)) + (procurar_codigo(codigo, pilha3)) + (procurar_codigo(codigo, pilha4))


    # Verifica se existe algum elemento, se exitir ele tira o do topo e compara para ver se é o mesmo que deseja REMOVER
    # Se o codigo digitado ser o mesmo do topo da pilha, ele pode remover.
    if (len(pilha1) > 0 and pilha1.peek() == codigo):
        pilha1.pop()
        print("Codigo removido da pilha 1")
    elif (len(pilha2) > 0 and pilha2.peek() == codigo):
        pilha2.pop()
        print("Codigo removido da pilha 2")
    elif (len(pilha3) > 0 and pilha3.peek() == codigo):
        pilha3.pop()
        print("Codigo removido da pilha 3")
    elif (len(pilha4) > 0 and pilha4.peek() == codigo):
        pilha4.pop()
        print("Codigo removido da pilha 4")

    elif (len(pilha1) > 0 and pilha1.peek() != codigo):
        print("Nao e possivel remover o produto, pois esta em baixo do topo.") 
    elif (len(pilha2) > 0 and pilha2.peek() != codigo):
        print("Nao e possivel remover o produto, pois esta em baixo do topo.") 
    elif (len(pilha3) > 0 and pilha3.peek() != codigo):
        print("Nao e possivel remover o produto, pois esta em baixo do topo.")
    elif (len(pilha4) > 0 and pilha4.peek() != codigo):
         print("Nao e possivel remover o produto, pois esta em baixo do topo.")

    else:
        print("A PILHA ESTA VAZIA")
        break




            
        
                    
        
            

     
            
        






