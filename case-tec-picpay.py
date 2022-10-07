"""

##INSTRUÇÕES INICIAIS

Para obter as respostas deste case técnico, execute o arquivo 'case-tec-picpay.py' em um diretório a sua escolha.

Obs: Para executá-lo corretamente, será necessário:

    • ter instalado o Python na sua versão mais recente; 
    • ter instalado a biblioteca 'Pandas' e o módulo nativo do Python 'XlsxWriter'

No terminal você encontrará as respostas de cada questão. 
O código fonte para obtê-las está presente neste documento.

------------------------------------------------------------------------------------------------------------------------
CASE

Uma pequena corretora de Bitcoins está passando por avaliação de auditoria. 
Com isso, foi solicitado as análises abaixo das bases de dados com o objetivo 
de avaliar os riscos dos processos de cadastro e venda de criptomoedas.

------------------------------------------------------------------------------------------------------------------------------------------------------

"""

##QUESTÃO 01.
#Existe, na base de cadastro, e-mails atribuídos a mais de um usuário? Se existe, quais são os usuários?

#setando variavel de formatação
linha ='''--------------------------------------------------------------------------------'''


# PASSO 1 : ACESSAR A BASE DE DADOS

#adicionando lib pandas
import pandas as pd

#importando arquivo-base
baseCadastro = pd.read_excel("base_clientes.xlsx")

print('''
RESPOSTA QUESTÃO 01:

ACESSANDO "base_clientes.xlsx"
''') 
print(linha)
print(baseCadastro) #printando arquivo-base(método pandas)
print(linha)


# PASSO 2 : TRATAR OS DADOS

print(
'''
ACESSANDO COLUNA ALVO
''')
print(linha)

#isolar colunas alvo
email = baseCadastro.groupby(['email','name']).size()
print(email)

# PASSO 3 : ANÁLISE GERAL

#somar os valores mais ocorrentes de uma coluna

#metodo .value_counts() responsável por retornar uma série contendo contagens de valores exclusivos da coluna email
#metodo .head() imprime os 5 primeiros itens da contagem
#metodo to_frame() transforma os dados em um DataFrame
baseCadastro['email'].value_counts().head().to_frame() 
print(linha)

# PASSO 4 : ANÁLISE ESPECÍFICA  

# Quais os usuários com mesmo e-mail?
name = baseCadastro.query("email=='sed@hotmail.org'") #método .query() permite fazer uma pergunta ao DataFrame

resposta01 = '''\nResposta final 01:
\nExiste sim. O e-mail (sed@hotmail.org) está atribuído a mais de um usuário. 
Os usuários são: Charde Mann, Leroy Stevens e Geoffrey Blanchard e têm seus dados informados abaixo.
'''
print(resposta01)
print(name)
print(linha)


# ##2.Quais os 5 países com a maior quantidade de usuários cadastrados?"""

print(
'''
RESPOSTA QUESTÃO 02:
''')
print(
'''
FILTRANDO BANCO DE DADOS:
''')
print(linha)

# somar os valores mais ocorrentes de uma coluna

#metodo .value_counts() responsável por retornar uma série contendo contagens de valores exclusivos da coluna country
#metodo .head() imprime os 5 primeiros itens da contagem
#metodo to_frame() transforma os dados em um DataFrame
pais01 = baseCadastro['country'].value_counts().head(5).to_frame()
print(pais01) # retorna contagem dos 05 paises 
pais = pais01.reset_index() # método .reset_index() transforma o índice em coluna para ser adicionada numa lista
print(linha) # retorna varivael de formatação 

listPais = pais['index'].to_list() # método .tolist() transforma a coluna country em lista

resposta02 = f'''\nResposta final 02:
\nOs 5 países com a maior quantidade de usuários cadastrados são: {', '.join((map(str,listPais)))}.
'''
print(resposta02)
print(linha)

# ##3.Quais as transações onde o valor individual da transação ultrapasse em 50% a média mensal, do mês que foi realizada?

# PASSO 1 : ACESSAR A BASE DE DADOS

print(
'''
RESPOSTA QUESTÃO 03:
''')
print(
'''
ACESSANDO 'bitcoin_purchase.csv':
''')
print(linha)

#importando arquivo-base com o método pandas read_csv()
transacoes = pd.read_csv("bitcoin_purchase.csv", parse_dates=['date']) # convertendo os dados da coluna 'date' com o parametro do método pandas read_csv()
#printando arquivo-base
print(transacoes)
print(linha)
print(
'''
ISOLANDO COLUNA ALVO
''')
print(linha)

# PASSO 2 : TRATAR OS DADOS

# 2.1 isolar e tirar media mensal
# 2.3 transação maior que 50% da média

# 2.1 isolar e tirar media mensal
orderDate = transacoes.sort_values(by='date') # metodo sort_values() ordena o dataset em função da coluna date - padrão True crescente
orderDate.dtypes # retorna os tipo de dados do data-frame 

# isolando a coluna
print(orderDate['date']) # retorna a coluna 'date' ordenada
print(linha)

# agrupando meses e tirando média transacional 
mes09 = orderDate.loc[(orderDate['date'] <= '2021-09-30')] #método .loc[] filtra informação contida na linha baseado em condição
media09 = mes09['value'].mean() # valor medio da transação mensal

mes10 = orderDate.loc[(orderDate['date'] > '2021-09-30') & (orderDate['date'] <= '2021-10-31' )]
media10 = mes10['value'].mean()# valor medio da transação mensal

mes11 = orderDate.loc[(orderDate['date'] > '2021-10-31') & (orderDate['date'] <= '2021-11-30' )]
media11 = mes11['value'].mean()# valor medio da transação mensal

mes12 = orderDate.loc[(orderDate['date'] > '2021-11-30') & (orderDate['date'] <= '2021-12-31' )]
media12 = mes12['value'].mean()# valor medio da transação mensal

mes01 = orderDate.loc[(orderDate['date'] > '2021-12-31') & (orderDate['date'] <= '2022-01-31' )]
media01 = mes01['value'].mean()# valor medio da transação mensal

mes02 = orderDate.loc[(orderDate['date'] > '2022-01-31') & (orderDate['date'] <= '2022-02-28' )]
media02 = mes02['value'].mean()# valor medio da transação mensal

mes03 = orderDate.loc[(orderDate['date'] > '2022-02-28') & (orderDate['date'] <= '2022-03-31' )]
media03 = mes03['value'].mean()# valor medio da transação mensal

mes04 = orderDate.loc[(orderDate['date'] > '2022-03-31') & (orderDate['date'] <= '2022-04-30' )]
media04 = mes04['value'].mean()# valor medio da transação mensal

mes05 = orderDate.loc[(orderDate['date'] > '2022-04-30') & (orderDate['date'] <= '2022-05-31' )]
media05 = mes05['value'].mean()# valor medio da transação mensal

mes06 = orderDate.loc[(orderDate['date'] > '2022-05-31') & (orderDate['date'] <= '2022-06-30' )]
media06 = mes06['value'].mean()# valor medio da transação mensal

mes07 = orderDate.loc[(orderDate['date'] > '2022-06-30') & (orderDate['date'] <= '2022-07-31' )]
media07 = mes07['value'].mean()# valor medio da transação mensal

mes08 = orderDate.loc[(orderDate['date'] > '2022-07-31') & (orderDate['date'] <= '2022-08-31' )]
media08 = mes08['value'].mean()# valor medio da transação mensal

# 2.3 transação maior que 50% da média
print(
'''
Resposta final 03:
''')
print('''As transações onde o valor individual da transação ultrapassa 50% estão a seguir:\n''')
print(f'Transação média de Setembro/2021: {media09:,.2f}')
print('Transações 50% maiores que a média de Setembro/2021:')
for x in mes09['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes09
    if x > (media09*1.5):
        print(f'{x:,.2f}')
print(f'\nTransação média de Outubro/2021: {media10:,.2f}')
print('Transações 50% maiores que a média de Outubro/2021:')
for x in mes10['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes10
    if x > (media10*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Novembro/2021: {media11:,.2f}')
print('Transações 50% maiores que a média de Novembro/2021:')
for x in mes11['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes11
    if x > (media11*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Dezembro/2021: {media12:,.2f}')
print('Transações 50% maiores que a média de Dezembro/2021:')
for x in mes12['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes12
    if x > (media12*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Janeiro/2022: {media01:,.2f}')
print('Transações 50% maiores que a média de Janeiro/2022:')
for x in mes01['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes01
    if x > (media01*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Fevereiro/2022: {media02:,.2f}')
print('Transações 50% maiores que a média de Fevereiro/2022:')
for x in mes02['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes02
    if x > (media02*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Março/2022: {media03:,.2f}')
print('Transações 50% maiores que a média de Março/2022:')
for x in mes03['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes03
    if x > (media03*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Abril/2022: {media04:,.2f}')
print('Transações 50% maiores que a média de Abril/2022:')
for x in mes04['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes04
    if x > (media04*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Maio/2022: {media05:,.2f}')
print('Transações 50% maiores que a média de Maio/2022:')
for x in mes05['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes05
    if x > (media05*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Junho/2022: {media06:,.2f}')
print('Transações 50% maiores que a média de Junho/2022:')
for x in mes06['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes06
    if x > (media06*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Julho/2022: {media07:,.2f}')
print('Transações 50% maiores que a média de Julho/2022:')
for x in mes07['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes07
    if x > (media07*1.5):
        print(f'{x:,.2f}')

print(f'\nTransação média de Agosto/2022: {media08:,.2f}')
print('Transações 50% maiores que a média de Agosto/2022:')
for x in mes08['value']: # criação do iterador que percorrerá a coluna 'value' correspondente a variável mes8
    if x > (media08*1.5):
        print(f'{x:,.2f}')

print(linha)

# ##4.Quais os 10 usuários que mais transacionaram no ano de 2022?"""

#Os que mais transacionaram são os que o id ocorre em maior quantidade

print(
'''
RESPOSTA QUESTÃO 04:
''')
print(
'''
Filtrando 'bitcoin_purchase.csv':
''')
print(linha)

# metodo .value_counts() conta quantas vezes um item aparece no df
# metodo .head(10) mostra os 10 primeiros itens
# método .to_frame() transforma o resultado do value_counts em dataframe
maiores01 = transacoes['id'].value_counts().head(10).to_frame().reset_index()  
print(maiores01)
maiores01.info()
print(linha)
maiores = maiores01.reset_index() # método .reset_index() transforma o índice em coluna

listMaiores = maiores['index'].tolist() # método .to_list() transforma a coluna id em lista

resposta04 = f'''\nResposta final  04:
\nOs 10 usuários que mais transacionaram são: {', '.join((map(str,listMaiores)))} 
'''
# métodos map, join e str são usados para melhor visualização dos dados
print(resposta04)

###5.O analítico, em Excel, das transações dos 10 usuários que mais transacionaram em 2022 separando as transações de cada usuário em uma aba diferente do mesmo arquivo."""
print(
'''
RESPOSTA QUESTÃO 05:
''')
print(
'''
Filtrando 'bitcoin_purchase.csv':
''')
print(linha)

# Isolando as transações de cada usuário
# .query() filtra as informações baseado na condição
user01 = transacoes.query(f"id=={listMaiores[0]}") 
user02 = transacoes.query(f"id=={listMaiores[1]}")
user03 = transacoes.query(f"id=={listMaiores[2]}")
user04 = transacoes.query(f"id=={listMaiores[3]}")
user05 = transacoes.query(f"id=={listMaiores[4]}")
user06 = transacoes.query(f"id=={listMaiores[5]}")
user07 = transacoes.query(f"id=={listMaiores[6]}")
user08 = transacoes.query(f"id=={listMaiores[7]}")
user09 = transacoes.query(f"id=={listMaiores[8]}")
user10 = transacoes.query(f"id=={listMaiores[9]}")
print(user10)
print(linha)

# criando arquivo excel
writer = pd.ExcelWriter('tabela-10-users.xlsx', engine='xlsxwriter') # metodo pandas para criação de arquivos xlsx

# metodo .to_excel também para criação e configuração de arquivo xlsx
user01.to_excel(writer,sheet_name=f'Usuário {listMaiores[0]}') 
user02.to_excel(writer,sheet_name=f'Usuário {listMaiores[1]}')
user03.to_excel(writer,sheet_name=f'Usuário {listMaiores[2]}')
user04.to_excel(writer,sheet_name=f'Usuário {listMaiores[3]}')
user05.to_excel(writer,sheet_name=f'Usuário {listMaiores[4]}')
user06.to_excel(writer,sheet_name=f'Usuário {listMaiores[5]}')
user07.to_excel(writer,sheet_name=f'Usuário {listMaiores[6]}')
user08.to_excel(writer,sheet_name=f'Usuário {listMaiores[7]}')
user09.to_excel(writer,sheet_name=f'Usuário {listMaiores[8]}')
user10.to_excel(writer,sheet_name=f'Usuário {listMaiores[9]}')

# salvando arquivo excel
writer.save()
print(
'''
Resposta final 05: Arquivo criado com sucesso.
''')
print(linha)

# ##6.Verificar se existem compras de criptomoedas para carteiras bloqueadas por fraude após a data do bloqueio."""

print(
'''
RESPOSTA QUESTÃO 06:
''') 
print(
'''
Existem sim compras de criptomoedas após a data de bloqueio das mesmas. Seguem abaixo os endereços e as datas divergentes:
''') 
print(linha)

fraudes = pd.read_excel('bitcoin_restriction.xlsx', parse_dates=['Restriction_date']) # convertendo os dados da coluna 'Restriction_date' com o parametro do método pandas read_csv()
transacoes = pd.read_csv("bitcoin_purchase.csv", parse_dates=['date']) # convertendo os dados da coluna 'date' com o parametro do método pandas read_csv()

listaTransacoes = [] # cria lista  para inserir os adress em transações
listaDatas = [] # cria lista  para inserir as dates em transações
listaDatasTransacoes = [] # cria lista  para inserir os Restriction_date em transações

for index1 in range(len(transacoes)): # criação do iterador que percorrerá o df 'transacoes'
    bitcoinAdressTransacoes = transacoes["bitcoin_address"].iloc[index1] # retorna valor dentro da coluna "bitcoin_address" dentro de transações; numero da linha é o index1
    for index2 in range(len(fraudes)): # criação do iterador que percorrerá o df 'fraudes'
        bitcoinAdressFraudes = fraudes["bitcoin_address"].iloc[index2] # retorna valor dentro da coluna "bitcoin_address" dentro de fraudes; numero da linha é o index1
        if bitcoinAdressTransacoes == bitcoinAdressFraudes: #criação do filtro
            dateTransacoes = transacoes['date'].iloc[index1] # retorna data das transações filtradas
            dateFraudes = fraudes['Restriction_date'].iloc[index2] # retorna data das fraudes filtradas
            if dateTransacoes > dateFraudes: #criando o filtro para comparar as datas 
                listaTransacoes.append(bitcoinAdressTransacoes) # adicionando resultado do if a lista
                listaDatas.append(dateTransacoes) # adicionando resultado do if a lista
                listaDatasTransacoes.append(dateFraudes) # adicionando resultado do if a lista

fraudeResult = pd.DataFrame() # criando um novo df
fraudeResult["bitcoin_address"] = "" # criando nova coluna vazia
fraudeResult["data_compra"] = "" # criando nova coluna vazia
fraudeResult["data_bloqueios"] = "" # criando nova coluna vazia 
fraudeResult["data_compra"] = listaDatas # adicionando lista a coluna
fraudeResult["bitcoin_address"] = listaTransacoes # adicionando lista a coluna
fraudeResult["data_bloqueios"] = listaDatasTransacoes # adicionando lista a coluna

print(fraudeResult)
