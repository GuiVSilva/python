tamanho = 0
palindromo = []

tamanho = int(input("Digite o tamanho do numero: ")) 

for c in range(tamanho): #repete o numero que foi pedido em tamanho (ex:3, repete tres vezes para dgitar cada numero)
    palindromo.append(input("Digite numero separadamente: "))  


palindromo_reverse = palindromo.copy() #.copy para ter mais uma lista igual a palindromo, para fazer a comparacao com reverse dela.
palindromo_reverse.reverse()  #gera o reverse da lista palindromo


if palindromo == palindromo_reverse: #se a lista palindromo for igual ao reserve dela:
    print("É um Palíndromo")

else:
    print("Não é um Palíndromo")    