def carregar_dados_alunos(arq):
    with open(arq, "r") as file:
        alunos = file.readlines()
    dados_alunos = []
    for aluno in alunos:
        infos_aluno = aluno.split(",")
        dados = {
            'prontuario': infos_aluno[0],
            'nome': infos_aluno[1],
            'email': infos_aluno[2]
        }
        dados_alunos.append(dados)
    return tuple(dados_alunos)


nome_arq = input("Digite o caminho do arquivo: ")

# src\06-arquivos\alunos.txt
alunos = carregar_dados_alunos(nome_arq)
print(alunos)
