somaAltura= somaAlturaMulheres= mediaAltura= mediaAlturaMulheres= sexo_mais_Alto= qtdHomens= qtdMulheres = 0
maiorAltura = 0
menorAltura =  0

for pessoas in range(1,5):   
    print("-----{}ª PESSOA -----".format(pessoas))
    sexo = int(input("Sexo [Digite 1 para HOMEN/ Digite 2 para Mulher]: "))
    altura = float(input("Altura: "))
    if pessoas == 1:
      menorAltura = altura
      maiorAltura = altura
      sexo_mais_Alto = sexo
   
    if sexo == 1:
      qtdHomens+= 1
    else: 
      if sexo==2:
        qtdMulheres+=1
        somaAlturaMulheres+=altura

    if menorAltura > altura:
      menorAltura = altura
    
    if maiorAltura < altura:
      maiorAltura = altura
      sexo_mais_Alto = sexo

mediaAlturaMulheres = somaAlturaMulheres / qtdMulheres

             
print("A media da altura das Mulheres é de {} ".format (mediaAlturaMulheres))
print("A menor altura do grupo é de {} cm".format(menorAltura))
print("A quantidade de Homens é de {} ".format(qtdHomens))
print("O sexo mais alto é de {}".format(sexo_mais_Alto))
