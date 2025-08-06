import pandas as pd

# Gerando DF
print('='*60)
alunos_df = pd.DataFrame({
    'nome': ['Joao', 'Carlos', 'Amanda'],
    'idade': [21, 20, 19],
    'aprovado': [True, False, True]
})
print(alunos_df)
alunos_df.info()
# Renomeando colunas
print('='*60)
print(alunos_df.columns)
print(type(alunos_df.columns))

alunos_df_renamed = alunos_df.rename(columns={
    'nome': 'Primeiro Nome',
    'idade': 'Idade',
    'aprovado': 'Aprovado'
})  # com parametro inplace=True substitui no df

print(alunos_df_renamed)

alunos_df_renamed.columns = ['nome', 'idade', 'aprovacao']
print(alunos_df_renamed)

# Selecionando uma coluna inteira
print('='*60)
print(alunos_df['aprovado'])
print(alunos_df.aprovado)
print(type(alunos_df.aprovado))

# Selecionando uma linha inteira
print('='*60)
print(alunos_df.iloc[1])

# Criando uma Series
print('='*60)
print(pd.Series([5.5, 6.0, 9.5], index=[
      'p1', 'p2', 'p3'], name='Notas nome_aluno'))

# Atribuindo Constantes
print('='*60)
aprovacoes = alunos_df['aprovado'].copy()
print(aprovacoes)

alunos_df['aprovado'] = True
print(alunos_df['aprovado'])

# Atribuindo listas ou series
nrows, ncols = alunos_df.shape
nomes = [f'Nome {i}' for i in range(nrows)]
alunos_df.nome = nomes
print(alunos_df)

alunos_df['aprovado'] = aprovacoes
print(alunos_df)

# Criando novas colunas
alunos_df['curso'] = 'DEFAULT'
print(alunos_df)

alunos_df['col p list'] = range(alunos_df.shape[0])
print(alunos_df)

alunos_df['pontuacao'] = alunos_df['aprovado'] * 10
print(alunos_df)

# Índices
print('='*60)
# print(alunos_df.index)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 20],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstaion4', 'Nintendo Switch'])

print(pesquisa_de_satisfacao.head())

# Selecionando uma ou mais observações (Indexação)
print('='*60)
print(alunos_df.iloc[1])
print(alunos_df.iloc[:3])
print(alunos_df.iloc[1:3])
print(alunos_df.iloc[[0, 2]])

# Retornando valor da linha indice 1, coluna 2 ('aprovado')
print(alunos_df.iloc[1, 2])

# Seleção por labels
print('='*60)
print(pesquisa_de_satisfacao.loc['XboxOne'])
# NÃO FUNCIONA ===> iloc tentando usar índices com números
print(pesquisa_de_satisfacao.loc['Playstaion4', 'ruim'])
print(pesquisa_de_satisfacao.loc[['Playstaion4', 'Nintendo Switch']])

# Retorna todas as linha e apenas as colunas com
# rótulos bom e pessimo
print(pesquisa_de_satisfacao[['bom', 'pessimo']])
print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']])

# Seleção de Colunas/Atributos
print('='*60)
print(alunos_df['nome'])
print(alunos_df.loc[:, 'nome'])
print(alunos_df[['nome', 'aprovado']])

# Removendo Colunas
print('='*60)
print(alunos_df.head())
del alunos_df['col p list']
print(alunos_df.head())
del alunos_df['curso']
del alunos_df['pontuacao']
print(alunos_df.head())

# Salvando um Data Frame
print('='*60)
pesquisa_de_satisfacao.to_csv(
    'src/semana-04/Pandas/anotacoes/pesquisa_de_satisfacao.csv')
print("Data Frame salvo.")


print('='*60)
data = pd.read_csv(
    'src/semana-04/Pandas/anotacoes/GasPricesinBrazil_2004-2019_preprocessado.csv')

# Seleção Condicional: Filtrando amostras
print(data.info())
print('='*60)
print(data['ESTADO'].unique())

# Selecionando apenas os Postos de São Paulo
print('='*60)
selecao = data['ESTADO'] == 'SAO PAULO'
print(data[selecao])
# data.loc[selecao]
# ------------------------#
print('='*60)
postos_sp = data.query('ESTADO == "SAO PAULO"')
print(postos_sp.head())
print('='*60)
postos_sp.reset_index(inplace=True)  # drop=True, remove a coluna index
print(postos_sp)
# ------------------------#
print('='*60)
postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True)
print(postos_sp)

# Selecionando registros de postos do RJ com preços acima de 2 reais
print('='*60)
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (
    data['PREÇO MÉDIO REVENDA'] > 2.0)
print(data[selecao])
# ------------------------#
print('='*60)
selecao1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao1]
selecao2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2.0
postos_rj_revenda_maiorq_2 = postos_rj[selecao2]
print(postos_rj_revenda_maiorq_2['PREÇO MÉDIO REVENDA'])

# Selecionando registros de postos de SP ou do RJ com gasolina comum acima de 2 reais
print('='*60)
selecao1 = (data['ESTADO'] == 'SAO PAULO') | (
    data['ESTADO'] == 'RIO DE JANEIRO')
selecao2 = (data['PRODUTO'] == 'GASOLINA COMUM')
selecao3 = (data['PREÇO MÉDIO REVENDA'] > 2.0)
selecao_final = selecao1 & selecao2 & selecao3
print(data[selecao_final])
# ------------------------#
print('='*60)
selecao1 = (data['ESTADO'] == 'SAO PAULO') | (
    data['ESTADO'] == 'RIO DE JANEIRO')
postos_sp_rj = data[selecao1]

selecao2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM')
gas_comum_sp_rj = postos_sp_rj[selecao2]

selecao3 = (gas_comum_sp_rj['PREÇO MÉDIO REVENDA'] > 2.0)
gas_comum_sp_rj_preco_maior_que_2 = gas_comum_sp_rj[selecao3]
print(gas_comum_sp_rj_preco_maior_que_2)

# Selecionando registros dos anos de 2008, 2010 e 2012
print('='*60)
selecao = (data['ANO'] == 2008) | (data['ANO'] == 2010) | (data['ANO'] == 2012)
print(data[selecao])  # ['ANO'].unique()
# ------------------------#
print('='*60)
lista_de_anos = [2008, 2010, 2012]
selecao = data['ANO'].isin(lista_de_anos)
print(data[selecao])
# ------------------------#
print('='*60)
print(data.query('ANO in @lista_de_anos'))

# Iterando com DataFrames
print('='*60)

# For-each DataFrame.iterrows() (LENTO ==> apenas indicado para iterar pequenos conjuntos de dados)
for index, row, in data.head(10).iterrows():
    print(f'indice {index} ==> {row["ESTADO"]}')
