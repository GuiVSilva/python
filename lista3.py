numeros = [1,2,2,3,4,4,5,6,7,8,9,9,9,9,10,11,11]


while True:
  valor = int(input("Digite um numero: "))

  if valor in numeros:     
    print("Esse numero consta na lista")   
    print("Esse numero aparece: ",numeros.count(valor), "vezes")
    
  
  else:
    print("Esse numero nao aparece na lista")
    print("\nPor favor digite um novo numero")
    


  
