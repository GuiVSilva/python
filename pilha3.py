from Stack import Stack
valida = 1
abre = 0
fechamento = 0 

matematica = Stack()

opr = str(input("Digite um expressao matematica: "))

for i in range(len(opr)):
    if opr [i] == "(" or opr [i] == ")":
        matematica.push(opr[i])
if matematica.peek() == "(":  
    valida = 0

for i in range (len(matematica)):
    
    if matematica.pop() == ")":
        fechamento += 1
    else:
        abre +=1

    if i == len(matematica) - 1:
        if matematica.peek() ==  ")":
            valida = 0


if fechamento == abre and valida == 1:
    print("EQUAÇAO VALIDA")
else:
    print("EQUAÇAO INVALIDA")

  












 
   

       

    

    




