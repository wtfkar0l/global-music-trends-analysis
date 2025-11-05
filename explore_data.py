import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('spotify_cleaned_for_tableau_v2.csv')
    print("Arquivo limpo carregado.")
except FileNotFoundError:
    print("Arquivo 'spotify_cleaned_for_tableau_v2.csv' não encontrado.")
    exit()

# 1. Selecionar apenas as colunas numéricas de features para a correlação
features = [
    'popularity', 'acousticness', 'danceability', 'duration_min', 
    'energy', 'instrumentalness', 'liveness', 'loudness', 
    'speechiness', 'tempo', 'valence'
]
df_features = df[features]

# 2. Calcular a Matriz de Correlação
corr_matrix = df_features.corr()

# 3. Imprimir a correlação com 'Popularidade' (para seus Key Findings)
print("\nCorrelação de todas as features com 'Popularity':")
print(corr_matrix['popularity'].sort_values(ascending=False))

# 4.Salvar um Heatmap de Correlação
plt.figure(figsize=(12, 14))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdYlGn_r', vmin=-1, vmax=1)
plt.title('Matriz de Correlação de Features do Spotify')
plt.savefig('correlation_heatmap.png')
print("\nHeatmap de correlação salvo como 'correlation_heatmap.png'")