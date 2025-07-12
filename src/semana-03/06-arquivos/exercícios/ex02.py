def carregar_dados_projeto(arq):
    with open(arq, "r") as file:
        projetos = file.readlines()
    dados_projetos = []
    for projeto in projetos:
        infos_projeto = projeto.split(",")
        dados = {
            'chave': infos_projeto[0],
            'título': infos_projeto[1],
            'responsável': infos_projeto[2]
        }
        dados_projetos.append(dados)
    return tuple(dados_projetos)


nome_arq = input("Digite o caminho do arquivo: ")

# src\06-arquivos\projeto.txt
projetos = carregar_dados_projeto(nome_arq)
print(projetos)
