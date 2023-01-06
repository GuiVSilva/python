numeros = [[],[]]
valor = 0

for c in range (1,8):
  valor = int(input(f"Digite o {c}° valor: "))
  if valor > 0:
    numeros[0].append(valor)
  else:
    numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f"Positivos: {numeros[0]}")
print(f"Negativos: {numeros[1]}")




