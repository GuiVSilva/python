class Potencia:

  def __init__(self, base = 3, expoente = 4):
    self.base = base
    self.expoente = expoente

  def potencia(self):
    return self.base ** self.expoente

calcular = Potencia() 
print(calcular.potencia())   
n=4
r=1
while n>0:
  r *= 3
  n -=1
print(r)  
  

