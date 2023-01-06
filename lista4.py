numeros = [[],[]]

for c in range(10):
  valor = int(input(f"Digite o {c}° valor: "))
  if valor > 0:
    numeros[0].append(valor)
    numeros[1].append(valor)


numeros[1].reverse()

for c in range(10):
  if numeros[0][c]==numeros[1][c]:
    print(f"Posicao {c} com o mesmo numero")


print(f"Numeros: {numeros[0]}")
print(f"Numeros na ordem inversa: {numeros[1]}")  
  