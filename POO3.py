class Calculadora:

  def soma(self,a,b):
    return a + b

  def subtracao(self,a,b):
    return a - b

  def multiplicacao(self,a,b):
    return a * b

  def divisao(self,a,b):
    return a / b
    

calcular = Calculadora()
print(calcular.soma(2,2))    
print(calcular.subtracao(2,2)) 
print(calcular.multiplicacao(2,2)) 
print(calcular.divisao(2,2)) 

#-----------------------------------------------------------#
#OUTRO MODO DE FAZER

class Calculadora:
  def __init__(self, a = 2 , b = 4):
    self.a = a
    self.b = b

  def soma(self):
    return self.a + self.b 

  def subtracao(self):
    return self.a - self.b

  def multiplicacao(self):
    return self.a * self.b

  def divisao(self):
    return self.a / self.b  

calcular = Calculadora()
print(calcular.soma())    
print(calcular.subtracao()) 
print(calcular.multiplicacao()) 
print(calcular.divisao()) 