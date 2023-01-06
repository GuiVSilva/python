numeros = [[]]
posicoes = []
valor = 0
soma = 0

for c in range (1,8):
  valor = int(input(f"Digite o {c}° valor da {c}ª posicao: "))
  if valor > 0:
    numeros[0].append(valor)
  else:
    print("Somente numero positivo!!!")
    break
  if valor % 2 != 0:
    posicoes.append(c)
    soma += valor
    

print("posições dos números impares: ", posicoes)  
print("Soma dos numeros nas posicoes impares: ",soma)  






