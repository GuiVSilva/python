media = 0
mediaDosAlunos = []

n1 = int(input("Digite a quantidade de alunos que estão cusando o 3° semestre: "))

print("Digite a quantidade de disciplinas e a nota do aluno que cursou no 2° semestre: ")

for disciplina in range(n1):
  print("-----{}° ALUNO -----".format(disciplina+1))
  qtdDisciplina1 = int(input("QUANTIDADE DE DISCIPLINAS: "))  

  somaDasNotas =0
  nota= 0

  for notaDoAluno in range(qtdDisciplina1):
    nota = float(input("NOTA DA {}ª DISCIPLINA DO ALUNO {} : ".format(notaDoAluno+1,disciplina+1)))
    somaDasNotas += nota

  media = somaDasNotas / qtdDisciplina1
  mediaDosAlunos.append(media)
  


for aluno in range (n1):
   print("A media do aluno {} é de {} ".format (aluno+1,mediaDosAlunos[aluno]))
  



