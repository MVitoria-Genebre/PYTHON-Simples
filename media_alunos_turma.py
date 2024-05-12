quant_turma = int(input("Insira a quantidade de Turmas: "))
total_alunos = 0

for i in range(1, quant_turma + 1):
    while True:
        quant_alunos = int(input("Insira o número de Alunos de cada Turma: "))
        if (quant_alunos < 41):
            total_alunos += quant_alunos
            break
        else:
            print("Uma turma não pode ter mais de 40 alunos.")
media = total_alunos / quant_turma
print("A média de alunos por turma é de: ", media)
       
