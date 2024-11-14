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


try:
    array_recupera_veiculo = np.array(df_recuperacao_veiculo['recuperacao_veiculos'])
    media_recupera = np.mean(array_recupera_veiculo)
    mediana_recupera = np.median(array_recupera_veiculo)
    distancia = abs((media_recupera - mediana_recupera)/ mediana_recupera) * 100

    maximo = np.max(array_recupera_veiculo)
    minimo = np.min(array_recupera_veiculo)
    amplitude_total = maximo - minimo

    q1 = np.quantile(array_recupera_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_recupera_veiculo, 0.50, method='weibull')
    q3 = np.quantile(array_recupera_veiculo, 0.75, method='weibull')
    iqr = q3 - q1
    limite_superior = q3 +(1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)
    print(30* '-')
    print("Mínimo:", minimo)
    print(f'Limite inferior: { limite_inferior}')
    print(f'Q1: {q1}')
    # print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print('IQR: ',iqr)
    print(f'Limite superior: {limite_superior}')
    print('Máximo:', maximo)
    print(f'Amplitude total:{amplitude_total:.2f}')

    print( 'Resultados!!!')
    print(f'Essa é a media: {media_recupera:.2f}')
    print(f'Essa é a mediana: {mediana_recupera:.2f}')
    print(f'Essa é a distancia: {distancia:.2f}')

    print(30*'-')
    df_outiliers_sup = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] > limite_superior]
    print('\n DPs com recuperações superiores as demais: ')
    print(30*'-')
    if len(df_outiliers_sup)==0:
        print('Não existe DPs com valores discrepantes superiores')
    else:
        print(df_outiliers_sup.sort_values(by='recuperacao_veiculos', ascending=False))
    
    df_outiliers_inf = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] < limite_inferior]
    print('\n DPs com recuperações inferiores as demais: ')
    print(30*'-')
    if len(df_outiliers_inf) == 0:
        print('\n Não existe DPs com valores discrepantes inferiores')
    else:
        print(df_outiliers_inf.sort_values(by='recuperacao_veiculos', ascending=True))

 
except ImportError as e:
    print(f'Erro: {e}')