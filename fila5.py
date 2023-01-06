from Queue import Queue

fila = Queue()

numprioritario = 0  #senha
numnormal = 0  #senha
qtdPrioritarioFila = 0
qtdNormaFila = 0

while True:
  cliente = int(input("DIGITE SUA IDADE OU ZERO PARA SAIR: "))
  code = ""

  if cliente == 0:
    break
    

  elif cliente >= 50:
    qtdPrioritarioFila += 1
    numprioritario += 1
    code = "P" + str(numprioritario)
    fila.push(code)
    print("TOTAL DE IDOSOS É: {}".format(qtdPrioritarioFila))

  elif cliente >= 20 and cliente <= 49:
    qtdNormaFila += 1
    numnormal += 1
    code = "N" + str(numnormal)
    fila.push(code)
    print("TOTAL DE NORMAL É: {}".format(qtdNormaFila))

  else:
    print("INVALIDO")
    


print("ORDEM DA FILA")

while len(fila) > 0:
  cont = 0
  if qtdPrioritarioFila <= 0:
    qtdNormaFila -= 1
    print("ATEDIMENTO NORMAL")
    print("NORMAL: ", fila.pop())

  else:
    if qtdPrioritarioFila > 0:
        removeuPrioritario = 0
        for n in range(len(fila)):
            pessoaCode = fila.pop()
            if pessoaCode.find("P") == -1:
                fila.push(pessoaCode) 
            elif removeuPrioritario < 3:
                qtdPrioritarioFila -= 1
                removeuPrioritario += 1
                print("ATENDIMENTO PRIORITARIO")
                print("PRIORITARIO: ", pessoaCode)  
            else:
                fila.push(pessoaCode)  
          
        print("ATENDIMENTO NORMAL")
        print("NORMAL: ", fila.pop())
        qtdNormaFila -= 1