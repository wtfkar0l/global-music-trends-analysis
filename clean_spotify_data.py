import pandas as pd

print("Iniciando o script de limpeza...")

# 1. Carregamento dos Dados
try:
    df = pd.read_csv('spotify_data.csv')
    print(f"Dados carregados: {df.shape[0]} linhas.")
except FileNotFoundError:
    print("Erro: Arquivo 'spotify_data.csv' não encontrado. Verifique o nome do arquivo.")
    exit()

# 2. Limpeza
# 2.1. Remoção de duplicatas
df_cleaned = df.drop_duplicates(subset=['track_name', 'artist_name'], keep='first')
print(f"Linhas após remoção de duplicatas: {df_cleaned.shape[0]}")

# 2.2. Tratamento de valores nulos (Focando apenas em 'genre')
df_cleaned = df_cleaned.dropna(subset=['genre'])
print(f"Linhas após remover nulos (em 'genre'): {df_cleaned.shape[0]}")

# 2.3. Padronização de Gêneros 
df_cleaned.loc[:, 'genre'] = df_cleaned['genre'].str.title() 

# 3. Transformação (Feature Engineering)
df_cleaned.loc[:, 'duration_min'] = df_cleaned['duration_ms'] / 60000

# 4. Exportação para Análise
output_file = 'spotify_cleaned_for_tableau_v2.csv'
df_cleaned.to_csv(output_file, index=False, encoding='utf-8')

print(f"\nLimpeza concluída!")
print(f"Arquivo salvo como '{output_file}'. Você está pronto para o Tableau.")