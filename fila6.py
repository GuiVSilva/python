from Queue import Queue
import time
batata = Queue()

while True:
    pessoas = str(input("DIGITE SEU NOME (DIGITE 1 PARA INICIAR): "))
    if pessoas == "1":
        break
    batata.push(pessoas)



quente = int(input("QUANTAS VEZES VAI DIZER QUENTE? : "))
print("BATATA")

P = ""

for i in range(quente):   
    time.sleep(1)
    print("QUENTE")  
    
    P = batata.pop()
    batata.push(P)

P = batata.pop()    

print("QUEIMOU")
print(P)






