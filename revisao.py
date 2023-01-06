class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self._size = 0
        
  def push(self, item):
    node = Node(item)
    node.next = self.top
    self.top = node
    self._size = self._size + 1
        
  def pop(self):
    if self._size > 0 :
      node = self.top
      self.top = self.top.next
      self._size = self._size - 1
      return node.data
    raise IndexError ("The stack is Empty!")
        
  def peek(self):
    if self._size > 0:
      return self.top.data
    raise IndexError ("The stack is Empty!")
        
        
pilha = Stack()

a = int(input("Digite o primeiro numero: "))
opr = str(input("Digite uma operacao: "))
b = int(input("Digite o segundo numero: "))
opr2 = str(input("Digite a segunda operacao: "))
c = int(input("Digite o terceiro numero:"))

pilha.push(a)
pilha.push(opr)
pilha.push(b)
pilha.push(opr2)
pilha.push(c)

resultado1 = 0


if opr2 == "*":
  mult2 = b * c
  resultado1 = mult2

if opr2 == "/":
  if c == 0:
    print("Erro")
  else:
    div2 = b / c
    resultado1 = div2

if opr2 == "-":
  sub2 = b - c
  resultado1 = sub2
    
#############################################    
    
if opr == "+":
    soma = a + resultado1
    print(soma)
  


if opr == "-":
  subtracao = a - resultado1
  print(subtracao)

if opr == "*":
  multiplicacao = a * resultado1
  print(multiplicacao)

    
if opr == "/":
  if b == 0:
    print("Erro")
  else:
    divisao = a / resultado1
    print(divisao)