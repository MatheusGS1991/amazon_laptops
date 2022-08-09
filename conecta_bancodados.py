# Álgebra linear, matrizes...
import numpy as np

# Manipulação de dados em tabela
import pandas as pd

# Visualização gráfica e plotagens - simples/"personalizadas"
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Tamanho dos gráficos (polegadas) - Proporção Áurea
mpl.rcParams['figure.figsize'] = 16.18, 10.00
sns.set(rc={'figure.figsize': (16.18, 10.00)})

# Opções para melhor visualização dos dados
pd.set_option('display.max_rows', None) # Linhas Máx
pd.set_option('display.max_columns', None) # Colunas Máx
pd.set_option('display.max_colwidth', None) # Largura Cols
pd.set_option('display.width', None)  # Largura
pd.set_option('display.float_format', '{:.2f}'.format) # 2 casas decimais

df = pd.read_csv('data/input_data/data.csv', sep=';')
print(df.head(10))

for col in df.columns:
    if len(df[col].unique()) < 10:
        print(f'{col} --> {df[col].unique()}')


