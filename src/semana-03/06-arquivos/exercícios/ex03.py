def carregar_dados_arquivo(arq):
    with open(arq, "r") as file:
        infos = file.readlines()

    len_info = len(infos[0].split(","))

    # Talvez fosse melhor definir as chaves dentro de linha_para_dict
    # mas era requisito que essa função já recebesse a lista de keys
    keys = []
    for i in range(len_info):
        key = input(f"Informe a {i+1}° chave: ")
        keys.append(key)

    dados_arquivo = []
    for info in infos:
        dict = linha_para_dict(info, keys)
        print(dict, "\n--------------------------------------------")
        dados_arquivo.append(dict)

    return tuple(dados_arquivo)


def linha_para_dict(linha, lista_chaves):
    infos_linha = linha.split(",")
    dados = {}

    for i in range(len(lista_chaves)):
        dados[lista_chaves[i]] = infos_linha[i]

    return dados


nome_arq = input("Digite o caminho do arquivo: ")

# src\06-arquivos\alunos.txt
# src\06-arquivos\projeto.txt
dados = carregar_dados_arquivo(nome_arq)
print("\n", dados)
