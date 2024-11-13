import pandas as pd 
import numpy as np

#obter dados
try:
    print('Obtendo dados...')
    ENDERECO_DADOS ='https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    #Encondings: utf-8 iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    #delimitando somente as variavei do Exemplo1: munic,roubo_veiculo
    df_recuperacao_veiculo = df_ocorrencias[['cisp', 'recuperacao_veiculos']]
    df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()
    print(df_recuperacao_veiculo.head())
except ImportError as e:
    print(f'Erro: {e}')
    exit()