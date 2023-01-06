from Node import Node

class Stack1:

  def __init__(self):
    self.top = None
    self.size = 0

  def push(self,item):
    node = Node(item) 
    node.next = self.top
    self.top = node
    self.size = self.size + 1

  def pop(self):
    if self.size > 0:
      node = self.top
      self.top = self.top.next
      return node.data
    raise IndexError("The stack is empty")

pilha = Stack1()
a = int(input("Digite o primeiro numero: "))
opr = str(input("Digite a operacao: "))  

if opr == "!":
  if a == 0:
    print("Fatorial = 1")
  else:
    for num in range(a):
      fat = a * num
    print(fat)

else:

  b = int(input("Digite o segundo numero: "))
  pilha.push(a)
  pilha.push(opr)
  pilha.push(b)

print(pilha)

if opr == "+":
  soma = a+b
  print(soma)

if opr == "-":
  sub = a-b
  print(sub)

if opr == "*":
  mult = a*b
  print(mult)

if opr == "/":
  if b == 0:
    print("Divisao = ", a)
  else:
    div = a/b
    print(div)  

if opr == "^":
  pot = a**b
  print(pot)          



