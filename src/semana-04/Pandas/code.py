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
    'src/semana-04/Pandas/pesquisa_de_satisfacao.csv')
print("Data Frame salvo.")
