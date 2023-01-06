lista = [1, 'a', 2+3j, ['ab','CD']]
print(lista [0])
print(lista [2])
print(lista [3])
print(lista [-1])
lista [0] = 2
print(lista) 
##-----------------------------------------##
lista = [0,0,0,0,0]
lista = [0]*10
print(lista)
lista = lista + [1]*10
print(lista)
##-----------------------------------------##
lista = [1, 2, 3, ['ab', 'CD']]
del lista [2]
print(lista)
del lista [2][1]
print(lista)
##-----------------------------------------##
lista = [1, 'a', 2+3j, ['ab', 'CD']]
print(lista [1:])
print(lista [:1])
print(lista [1:2])
print(lista [0:-1])
##-----------------------------------------##
x = range (1,6)
if 1 in x: 
  print("contido")
else:
  print("nao tem")  
##-----------------------------------------##  
lista = [1, 2, 9, 3, 4]
print(len(lista))
print(min(lista)) #numero menor
print(max(lista)) #numero maior
print(len(lista)) #qtd de numeros na lista
##-----------------------------------------##  
lista = [1,2]
lista.append(3) #acrescenta o elemento no final da lista
print(lista)
lista.append([4,3])
print(lista)
##-----------------------------------------## 
lista = [1,1,2,2,2,4,5,6].count(2) #mostra quantas vezes o numero aparece
print(lista)
##-----------------------------------------## 
lista = [1,2]
lista.extend([3,4,5]) #adiciona os valores no final da lista
print(lista)
##-----------------------------------------## 
lista = [0,1,2,3]
lista.insert(1,"dois") #insere elemento na lista na posição indicada por índice, insert(indice, elemento)
print(lista)
##-----------------------------------------## 
lista = [1,2,3,4,5]
lista.pop() #remove o ultimo indice
print(lista)
lista.pop(1) #remove o indice 1 da lista
print(lista)
#pop(índice)Remove da lista o elemento na posição índice.Se índice não for mencionado, é assumido o último

##-----------------------------------------## 
lista = ['oi', 'ola', 'alo']
lista.remove('oi')
print(lista)
#remove(elemento)Remove da lista o primeiro elemento igual a elemento. 
#Se não existe tal elemento, um erro é gerado.

##-----------------------------------------## 
lista = [1,2,3] #reverse() Inverte a ordem dos elementos da lista.
lista.reverse()
print(lista)




