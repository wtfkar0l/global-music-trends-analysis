# 🎧 Análise de Features Musicais e Popularidade no Spotify

### 📊 Exploratory Data Analysis | Power BI | Tableau | Python

---

## 🧩 Project Overview
Este projeto explora o dataset público do Spotify para entender a **relação entre atributos musicais (features) e a popularidade das faixas**.
O objetivo foi identificar como características como `danceability`, `energy` e `valence` **diferem entre os gêneros** e quais atributos têm maior correlação com a popularidade de uma música — fornecendo insights para produtores e selos musicais.

> 💡 *A análise revela como perfis de áudio específicos (ex.: alta energia e dançabilidade) estão fortemente correlacionados com faixas de alta popularidade em gêneros-chave.*

---

## 🎯 Business Task
Uma consultoria musical solicitou uma visão geral de:
- A relação (correlação) entre as features musicais (`energy`, `danceability`, etc.) e a `popularity` geral.
- Quais gêneros musicais têm os maiores índices médios desses atributos.
- O "perfil de áudio" médio de um gênero (ex.: "Pop" vs. "Classical").
- Quais features são os melhores indicadores de popularidade de uma faixa.

---

## 🧰 Tools & Technologies
| Tool | Purpose |
|------|----------|
| **Python (Pandas, Matplotlib)** | Data cleaning and pre-processing |
| **Power BI / Tableau** | Interactive dashboards and visual storytelling |
| **Excel / CSV** | Data validation and export |
| **GitHub** | Version control and portfolio publication |

---

## 📂 Dataset
**Source:** [Spotify Tracks Dataset — Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)  
**License:** CC0 (public use)  
**Size:** ~600,000 tracks  
**Features:**
- `track_name`, `artist_name`, `genre`
- `popularity`, `danceability`, `energy`, `valence`, `acousticness`
- `tempo`, `duration_ms`, `instrumentalness`, `liveness`, `loudness`
- `speechiness`, `key`, `mode`, `time_signature`

---

## ⚙️ Process

1. **Data Cleaning:** remove duplicatas, handle para null values (especialmente em `genre`), padronização de gêneros musicais.
2. **Transformation:** Convertido `duration_ms` para `duration_min` para melhor interpretação.
3. **Exploration:** Python e Tableau para observar a correlação entre todas as features musicais e popularidade.
4. **Visualization:** Construção de dashboards dinâmicas em Tableau para explorar os diferentes perfis de gênero.
---

## 📈 Key Findings

| Insight | Observation |
|----------|--------------|
| 🎵 **Drivers de Popularidade** | `Danceability` e `Energy` mostraram uma correlação positiva consistente com `Popularity`. |
| ⚡ **Correlação de Features** | `Energy` e `Loudness` (volume) têm uma correlação positiva muito forte (r > 0.7). |
| 🎻 **Features Opostas** | `Acousticness` (acústica) tem uma forte correlação negativa com `Energy` e `Loudness`. |
| 😊 **Perfis de Gênero** | Gêneros como "Pop", "Latin" e "Hip-Hop" apresentam, em média, maior `Danceability` e `Valence` (positividade). |
| 🎹 **Instrumental** | `Instrumentalness` (ser instrumental) mostrou uma correlação negativa com `Popularity` na maioria dos gêneros. |

---

## 🗺️ Dashboard Preview
**Tableau Dashboard:** `Análise de Features Musicais e Popularidade`  
Includes:
- **Gráfico de Dispersão (Scatter Plot):** Popularidade vs. Danceability (colorido por Gênero)
- **Heatmap:** Média de Atributos (Energy, Valence, etc.) por Gênero
- **Gráfico de Caixa (Box Plot):** Distribuição de `Energy` por Gênero
- **Filtros Interativos:** Permite ao usuário filtrar por Gênero para analisar perfis específicos.

IN PROGRESS  

---

## 🧑‍💻 Author

**Ana Karolina Costa da Silva** 📍 Software Engineer & Data Science Researcher  
🎓 M.Sc. Computer Science — PUC-Rio  
💼 [LinkedIn](https://www.linkedin.com/in/karolyneehcs/) | [GitHub](https://github.com/karolyneehcs)
