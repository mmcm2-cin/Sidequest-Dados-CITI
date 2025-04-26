import pandas as pd

def ordenar_a_coluna(arquivo, coluna): # Função para ordenar as colunas de forma decrescente (Em strings Z > Y > X > ... > A)
    return arquivo.sort_values(by = coluna, ascending = False)

arquivo = pd.read_csv('Base_padronizada.csv') 

arquivo = ordenar_a_coluna(arquivo, 'sexo') # Ordena com base no sexo dos participantes
arquivo.to_csv('Base_ordenada_sexo.csv', index = False) # Cria o arquivo ordenadado com base no sexo

arquivo = ordenar_a_coluna(arquivo, 'aprovado') # Ordena com base nos Aprovados
arquivo.to_csv('Base_ordenada_aprov.csv', index = False) # Cria o arquivo ordenado com base se foi aprovado ou não

arquivo = ordenar_a_coluna(arquivo, 'Media') # Ordena de forma decrescente de acordo com as médias
arquivo.to_csv('Base_ordenada_media.csv', index = False) # Cria o arquivo ordenado pelas médias da maior para menor

arquivo = ordenar_a_coluna(arquivo, 'frequencia') # Ordena de forma descrente de acordo com as frequências
arquivo.to_csv('Base_ordenada_freq.csv', index = False) # Cria o arquivo ordenado pelas frequências da maior para menor