# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:04:43 2022

@author: caioo
"""

# importando a biblioteca pandas
import pandas as pd
import numpy as np
import datetime as dt

# lendo os arquivos CSVs
df1 = pd.read_csv(r'C:\Users\caioo\OneDrive\Documentos\DomusAutomação\00_base_dados_consumo_geral\Exportacao_Plataforma_Iot\fevereiro_2022/QIoT_dados_BI_1_fev_2022.csv')
df2 = pd.read_csv(r'C:\Users\caioo\OneDrive\Documentos\DomusAutomação\00_base_dados_consumo_geral\Exportacao_Plataforma_Iot\fevereiro_2022/QIoT_dados_BI_2_fev_2022.csv')
df3 = pd.read_csv(r'C:\Users\caioo\OneDrive\Documentos\DomusAutomação\00_base_dados_consumo_geral\Exportacao_Plataforma_Iot\fevereiro_2022/QIoT_dados_BI_3_fev_2022.csv')
df4 = pd.read_csv(r'C:\Users\caioo\OneDrive\Documentos\DomusAutomação\00_base_dados_consumo_geral\Exportacao_Plataforma_Iot\fevereiro_2022/QIoT_dados_BI_4_fev_2022.csv')
df5 = pd.read_csv(r'C:\Users\caioo\OneDrive\Documentos\DomusAutomação\00_base_dados_consumo_geral\Exportacao_Plataforma_Iot\fevereiro_2022/QIoT_dados_BI_5_fev_2022.csv')
# concatenando os arquivos
df_geral = pd.concat([df1, df2, df3, df4, df5], ignore_index = True)
# cria um copia dos dados principais
df = df_geral.copy()


# separando POR CLIENTE os dados GERAIS tratados 
df = df[df['empresa'].str.contains('SAEL', na = False)]
# exlcuindo o dia 220301 exportado a mais
df.drop(df.loc[df['data_tempo'] == '2022-03-01'].index, inplace = True)
# resetando o index 
df.reset_index(inplace = True, drop = False)
#exclui a coluna formada por regoganizar a indexacao
del df['index']
# copia para consulta dos dados brutos iniciais
df_main = df.copy()
del df1, df2, df3, df4, df5, df_geral

# renomeia as colunas
#df.rename(columns={'data_tempo': 'Data'}, inplace = True)
df.rename(columns={'empresa': 'Empresa'}, inplace = True)
df.rename(columns={'dispositivo': 'Dispositivo'}, inplace = True)
#df.rename(columns={'horas': 'Hora'}, inplace = True)
df.rename(columns={'consumo': 'Potência'}, inplace = True)


# tratando nome dos ds - GERAL
df['Dispositivo'] = df['Dispositivo'].str.replace('Showroom - ','')
df['Dispositivo'] = df['Dispositivo'].str.replace('Sala TI - AC - TI','AC TI')
df['Dispositivo'] = df['Dispositivo'].str.replace('Sala TI - ','')

#round(sum(df['Potência'])/1000, 3)

# Substituindo os valores de -255 por valores anteriores
#df255 = df.copy()
df['Potência'] = df['Potência'].replace(-255, method = 'bfill', inplace = False)
#round(sum(df255['Potência'])/1000, 3)

#df2 = df.copy()
# Excluindo dispositivos SEM AUTOMAÇÃO / SEM BI (RELATÓRIO)
df.drop(df.loc[df['Dispositivo'] == 'AC TI'].index, inplace = True)
df.drop(df.loc[df['Dispositivo'] == 'Tomadas 1 - TI'].index, inplace = True)
df.drop(df.loc[df['Dispositivo'] == 'Tomadas 2 - TI'].index, inplace = True)
# cria nova indexação para o os dados
df.reset_index(inplace = True, drop = False)
#exclui a coluna formada por regoganizar a indexacao
del df['index']






df['instante'] = df['data_tempo'] + ' ' + df['horas']
del df['data_tempo'], df['horas']
# transforma os valores da coluna em string 
df['instante'] = df['instante'].astype(str)
df['instante'] = df['instante'].str.replace('-','')
df['instante'] = df['instante'].str.replace(':','')
df['instante'] = df['instante'].str.replace(' ','')
# limita o numero de caracteres da coluna
df['instante'] = df['instante'].str[:12]


df['instante'] = pd.to_datetime(df['instante'])





df['tvalue'] = df.index
df['delta'] = (df['tvalue']-df['tvalue'].shift()).fillna(0)
df['ans'] = df['delta'].apply(lambda x: x  / np.timedelta64(1,'m')).astype('int64') % (24*60)



df['deltaT'] = df.index.to_series().diff().dt.seconds.div(60, fill_value=0)
ser_diff = df.index.to_series().diff()
ser_diff
ser_diff.dt.seconds.div(60, fill_value=0)














df['Delta_time'] = df['instante'][i].dt.days - df['instante'][i+1].dt.days



for i in df['instante']:
    df['Delta_time'] = df['instante'][i].dt.days - df['instante'][i+1].dt.days
    print(df['Delta_time'])
    
    
    datetime.timedelta(0, 8, 562000)
    seconds_in_day = 24 * 60 * 60
    divmod(difference.days * seconds_in_day + difference.seconds, 60)










type(df['instante'].values)
type(df['Potência'].values)


# criando a coluna Consumo
df['Consumo'] = 0
df['Delta_time'] = 0





# separar por dispositivo e organiza index
df_disp_ac01 = df.copy()
df_disp_ac01 = df[df['Dispositivo'].str.contains('AC 01', na = False)]
df_disp_ac01.reset_index(inplace = True, drop = False)
del df_disp_ac01['index']




# Iterando valores de Consumo de acordo com Potência

from datetime import datetime

final = datetime.strptime(df['instante'].index[0])

inicial = datetime.strptime(df['instante'].index[1])

intervalo = final - inicial

print(intervalo) 









for index, row in df_disp_ac01.iterrows():
    df_disp_ac01['Consumo'] = (df_disp_ac01['Potência'])*((df_disp_ac01['Hora']) - (df_disp_ac01['Hora']))
    

    


























# seleciona o intervalo de datas Ex: 01/02/2022 a 28/02/2022
#df_sael = df_sael[df_sael['data'].between(20220201, 20220228)]

# início do tratamento de dados de PONTA (17:30 às 20:30)
# faz a cópia dos dados gerais dá tratados
df_sael_p = df_sael.copy()
# transforma os valores da coluna horas em inteiro
df_sael_p['Hora'] = df_sael_p['Hora'].astype(int)   
# seleciona os valores entre 1730 e 2030 - horário de ponta
df_sael_p = df_sael_p[df_sael_p['Hora'].between(1730, 2030)]

# início do tratamento de dados FORA PONTA
# faz a cópia dos dados gerais dá tratados
df_sael_fp = df_sael.copy()
# transforma os valores da coluna horas em inteiro
df_sael_fp['Hora'] = df_sael_fp['Hora'].astype(int)   
# exclui os valores entre 1730 e 2030 - horário FORA PONTA
df_sael_fp.drop(df_sael_fp.loc[df_sael_fp['Hora'].between(1730,2030)].index, inplace = True)



# EXPORTANDO arquivos POR CLIENTE os dados GERAIS tratados 
df_sael.to_excel("df_sael03.xlsx")

# EXPORTANDO arquivos POR CLIENTE dos dados NA PONTA tratados 
df_sael_p.to_excel("df_ponta_sael03.xlsx")

# EXPORTANDO arquivos POR CLIENTE dos dados FORA PONTA tratados 
df_sael_fp.to_excel("df_fora_ponta_sael03.xlsx")
