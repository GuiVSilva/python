soma = 0
qtd = 0
while True:
  n = int(input("Digite um numero inteiro ou [Digite 0 para parar] : "))

  if n == 0:
    break
  soma += n
  qtd += 1
  media = soma / qtd

print("Quantidade dos numeros digitados:", qtd)
print("Soma: ", soma)
print("Media: ", media)  
