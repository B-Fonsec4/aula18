import pandas as pd 
import numpy as np

#obter dados
try:
    print('Obtendo dados...')
    ENDERECO_DADOS ='https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    #Encondings: utf-8 iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    #delimitando somente as variavei do Exemplo1: munic,roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    print('\n Calculando informações sobre padrão de roubo de veiculos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    # print(array_roubo_veiculo)
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)
    print(f'distancia: {distancia:.2f}')
    print(f'A media de roubo de veiculos é {media_roubo_veiculo:.2f}')
    print(f'A mediana de roubo de veiculos é {mediana_roubo_veiculo:.2f}')
    # descobrindo as amplitudes
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo
    # print(f'maximo:{maximo} ')
    # print(f'minimo:{minimo} ')
    print(f'amplitude:{amplitude} ')
    # calculando os quartis
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
    iqr = q3 - q1
    limite_superior = q3 +(1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)
    print(30* '-')
    print("Mínimo:", minimo)
    print(f'Limite inferior: { limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print('IQR: ',iqr)
    print(f'Limite superior: {limite_superior}')
    print('Máximo:', maximo)
    print('Filtrando os outliers!!!')
    df_roubo_veiculo_outliers_inferiores =df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo']< limite_inferior]
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo']> limite_superior]
    print('\ Municipios com numeros inferiores: ')
    print(30*'-' )
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending= True))
    print('\nMunicipios com outliers superiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) ==0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))
    
except Exception as e:
    print(f'Erro ao obter as informações sobre padrão de roubo de veiculos: {e}')
    exit()