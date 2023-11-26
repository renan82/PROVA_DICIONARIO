print("-=" * 20)
print("RESOLUÇÃO PROVA - DICIONÁRIOS AULA 03")
print("ALUNO - RENAN SALES MONTENEGRO")
print("ALUNO - INFINITY SCHOOL / período NOITE / QUINTA - FEIRA")
print("-=" * 20)
alunos = {}

def remover():
    for matricula, aluno in alunos.items():
        print(f"NOME: {aluno}, MATRICULA: {matricula}")
    remover = int(input("Digite o número da matrícula do aluno que deseja remover: "))
    if remover in alunos:
        nome = alunos.pop(remover)
        print('Aluno removido com sucesso')
        print(" *********** ")
        print("A nova lista de alunos é: ")
        for matricula, aluno in alunos.items():
            print(f"NOME: {aluno}, MATRICULA: {matricula}")
    else:
        print(" ***  ***")
        print("ALUNO NÃO LOCALIZADO, TENTE NOVAMETE")
        print(" ***  ***")

def adicionar():
    nome = str(input("Digite o nome do aluno (ou 'sair' para encerrar): "))
    matricula = int(input("Digite o número de matrícula do aluno: "))
    alunos[matricula] = nome
    print(f"Aluno {nome} com matrícula {matricula} foi adicionado com sucesso.")

def visualizar():
    print("Lista de alunos cadastrados:")
    for matricula, nome in alunos.items():
        print(f"Nome: {nome}, matrícula: {matricula}")

while True:
    escolha = int(input("""ESCOLHA UMA OPÇÃO:
          1 - ADICIONAR ALUNO
          2- REMOVER ALUNO
          3 - VISUALIZAR LISTA DE ALUNOS
          4- SAIR
          """))
    if escolha == 1:
        adicionar()
    if escolha == 2:
        remover()
    if escolha == 3:
        visualizar()
    if escolha == 4:
        break





      