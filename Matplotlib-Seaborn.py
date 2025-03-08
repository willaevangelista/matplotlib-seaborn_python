# Importações
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importando a base de dados
df = pd.read_csv('/content/netflix_titles_nov_2019.csv')

# Verificando se a DataFrame foi realmente importada corretamente
print(df.head(10).to_string() + "\n")
df.info()

# Exercício 1: Exploração inicial
# Quantas linhas e colunas tem o dataset?
num_linhas = df.shape[0]  # eixo X = 0 (horizontal) -> linhas
num_colunas = df.shape[1]  # eixo Y = 1 (vertical) -> colunas

print(f'O Catálogo da Netflix tem {num_linhas} linhas e {num_colunas} colunas.')

# Quais são os tipos das variáveis e se há valores ausentes?
valores_ausentes = df.isnull().sum()
print(f'O Catálogo da Netflix tem os seguintes valores ausentes:\n\n{valores_ausentes}')

print('\n\nO Catálogo da Netflix tem os seguintes tipos de variáveis:')
df.info()

# Exercício 2: Análises de frequência
# Qual a proporção de filmes vs. séries no catálogo?
movies = df.loc[df['type'] == 'Movie'].shape[0]
tv_shows = df.loc[df['type'] == 'TV Show'].shape[0]

print(f'O Catálogo da Netflix tem {movies} filmes e {tv_shows} TV Shows.')

# Qual o gênero mais frequente?
# Dado que cada obra tem mais de um gênero listado na mesma coluna, é necessário separar as informações
separacao_generos = df['listed_in'].str.split(', ').explode()  # o explode() transforma essas informações aglomeradas em linhas separadas

conta_genero = separacao_generos.value_counts()  # verificação do somatório de aparições de determinado gênero no catálogo

mais_frequente = conta_genero.idxmax()
print(f'\nO gênero mais frequente do Catálogo da Netflix é: {mais_frequente}.')

# Exercício 3: Análises estatísticas
# Qual a média, mediana e moda do tempo de duração dos filmes?
# Filtrando apenas os filmes, removendo "min" da duração e convertendo para float para permitir cálculos
duracao = df.loc[df['type'] == 'Movie', 'duration'].str.replace('min', '').astype(float)

tempo_media = duracao.mean()
tempo_mediana = duracao.median()
tempo_moda = duracao.mode()[0]

print(f'Duração dos Filmes do Catálogo da Netflix: \n\nMédia: {tempo_media:.2f}\nMediana: {tempo_mediana:.2f} \nModa: {tempo_moda:.2f}')

# Qual o filme mais curto e mais longo?
duracao_max = duracao.max()
duracao_min = duracao.min()

print(f'O filme mais curto tem {duracao_min:.2f} minutos de duração.')
print(f'O filme mais longo tem {duracao_max:.2f} minutos de duração.')

# Exercício 4: Visualização de dados
# Criar um gráfico de barras para mostrar a quantidade de títulos por gênero.
# Ordenação dos dados do menor para o maior
conta_genero_ordenado = conta_genero.sort_values(ascending=False)

# Definindo x e y
x = conta_genero_ordenado.index  # Gêneros dos títulos ordenados
y = conta_genero_ordenado.values  # Quantidade de títulos por gênero ordenada

# Definindo o estilo do gráfico
sns.set(style="whitegrid")  # Estilo de fundo com grid branco

# Criando o gráfico de barras horizontal
plt.figure(figsize=(10, 8))  # Ajusta o tamanho da figura para mais espaço
sns.barplot(x=y, y=x, palette="viridis")  # Usando o seaborn para criar o gráfico com uma paleta de cores agradável

# Adicionando título e rótulos
plt.xlabel('Quantidade de Títulos')
plt.ylabel('Gênero')
plt.title('Quantidade de Títulos por Gênero')

plt.tight_layout()  # Ajusta automaticamente o layout para evitar sobreposição
plt.show()

# Criar um histograma para analisar a distribuição da duração dos filmes.
# Filtrando apenas os filmes, removendo "min" da duração e convertendo para float
duracao = df.loc[df['type'] == 'Movie', 'duration'].str.replace('min', '').astype(float)

# Definindo o estilo do gráfico
sns.set(style="whitegrid")  # Estilo de fundo com grid branco

# Criando o histograma com Seaborn
plt.figure(figsize=(10, 6))  # Ajusta o tamanho da figura para melhor visualização
sns.histplot(duracao, bins=1000, kde=True, color='blue', edgecolor='pink', linewidth=1.5)  # 'kde=True' adiciona a linha de densidade

# Adicionando título e rótulos
plt.xlabel('Duração dos Filmes (minutos)')
plt.ylabel('Quantidade de Filmes')
plt.title('Histograma de Distribuição da Duração dos Filmes')

# Exibindo o gráfico
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()

# Exercício 5: Atividade extra
# Quais são os 5 países que possuem mais produções no catálogo?
# Sado que muitas produções possuem mais de um país envolvido nela, é necessário separar essas informações
separacao_paises = df['country'].str.split(', ').explode()  # O explode() transforma essas informações aglomeradas em linhas separadas

conta_paises = separacao_paises.value_counts()  # Verificação do somatório de aparições de determinado país no catálogo
print(f'Os 5 países que possuem mais produções no Catálogo da Netflix são:\n\n{conta_paises.head(5)}')

# Criação de Gráfico de Barras

# Definindo x e y
x = conta_paises.head(5).values  # Nome dos países
y = conta_paises.head(5).index  # Quantidade de produções

# Definindo o estilo do gráfico
sns.set(style="whitegrid")  # Estilo de fundo com grid branco

# Criando o gráfico de barras horizontal
plt.figure(figsize=(10, 8))  # Ajusta o tamanho da figura para mais espaço
sns.barplot(x=y, y=x, palette="viridis")  # Usando o seaborn para criar o gráfico com uma paleta de cores agradável

# Adicionando título e rótulos
plt.xlabel('Países')
plt.ylabel('Quantidade de Produções')
plt.title('5 Países com Mais Produções no Catálogo')

plt.tight_layout()  # Ajusta automaticamente o layout para evitar sobreposição
plt.show()
