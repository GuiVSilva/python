from Node import Node

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, item): #insere um item na pilha
    node = Node(item) #Criou o Nó
    node.next = self.top #Apontou para o proximo
    self.top = node #Adiciona o nome criado no topo da pilha
    self.size = self.size + 1

  def pop(self): #Remove o ultimo item da pilha
    if self.size > 0: #Verifica antes se a pilha esta vazia
      node = self.top #Salvo uma copia do ultimo item
      self.top = self.top.next #troco o ultimo item da pilha pelo penultimo
      self.size = self.size - 1 #Diminuo o tamanho da pilha
      return node.data
    raise IndexError("The Stack is Empty!")

  def peek(self):
    if self.size > 0:
      return self.top.data
    raise IndexError("The Stack is Empty!")  
    
#pilha ate o peek


  def __len__(self):
    return self.size

  def __repr__(self):
    data = ""
    node = self.top
    while(node):
      data = data + str(node.data) + "\n"
      node = node.next
    return node

  def __str__(self):
    return self.__repr__()


'''pilha = Stack()
pilha.push(1)   
pilha.push(2)    
pilha.push(3)
pilha.push("pato")
print(pilha)'''
