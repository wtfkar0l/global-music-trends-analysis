# 🎧 Análise de Features Musicais e Popularidade no Spotify

### 📊 Exploratory Data Analysis | Power BI | Tableau | Python

---

## 🧩 Project Overview
Este projeto explora o dataset público do Spotify para entender a **relação entre atributos musicais (features) e a popularidade das faixas**.
O objetivo foi identificar como características como `danceability`, `energy`, e `valence` **diferem entre os gêneros** e quais atributos têm maior correlação com a popularidade de uma música.

Ao fornecer insights quantitativos sobre "o que faz uma música ser popular", este projeto oferece uma ferramenta valiosa para produtores, selos musicais e profissionais de marketing digital que buscam otimizar suas estratégias de curadoria e promoção.

> 💡 *A análise revela como perfis de áudio específicos (ex: alta energia e dançabilidade) estão fortemente correlacionados com faixas de alta popularidade em gêneros-chave.*

---

## 🎯 Business Task
Uma consultoria musical solicitou uma visão geral de:
- A relação (correlação) entre as features musicais (`energy`, `danceability`, etc.) e a `popularity` geral.
- Quais gêneros musicais têm os maiores índices médios desses atributos.
- O "perfil de áudio" médio de um gênero (ex: "Pop" vs. "Classical").
- Quais features são os melhores indicadores de popularidade de uma faixa.

---

## 🧰 Tools & Technologies
| Tool | Purpose |
|------|----------|
| **Python (Pandas, Matplotlib)** | Data cleaning, pre-processing, and correlation analysis |
| **Power BI / Tableau** | Interactive dashboards and visual storytelling |
| **Excel / CSV** | Data validation and export |
| **GitHub** | Version control and portfolio publication |

---

## 📂 Dataset
**Source:** [Spotify Tracks Dataset — Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)  
**License:** CC0 (public use)  
**Features:**
- `track_name`, `artist_name`, `genre`
- `popularity`, `danceability`, `energy`, `valence`, `acousticness`
- `tempo`, `duration_ms`, `instrumentalness`, `liveness`, `loudness`
- `speechiness`, `key`, `mode`, `time_signature`

---

## ⚙️ Abordagem Analítica (Processo)
A análise seguiu uma metodologia de Exploração de Dados (EDA) estruturada para garantir a qualidade e a relevância dos insights:

1. **Data Cleaning:** Removed duplicates, handled null values (especialmente em `genre`), standardized genre names.
2. **Transformation:** Converted `duration_ms` para `duration_min` para melhor interpretação.
3. **Exploration (Python):** Used Python (Pandas/Seaborn) for correlation analysis between all musical features and popularity.
4. **Visualization (Tableau):** Built dynamic dashboards in Tableau to explore feature profiles by genre visually.

---

## 📈 Key Findings

A tabela abaixo resume as principais descobertas quantitativas:

| Insight | Observation |
|----------|--------------|
| 🎵 **Drivers de Popularidade** | `Danceability` e `Energy` mostraram uma correlação positiva consistente com `Popularity`. |
| ⚡ **Correlação de Features** | `Energy` e `Loudness` (volume) têm uma correlação positiva muito forte (r > 0.7). |
| 🎻 **Features Opostas** | `Acousticness` (acústica) tem uma forte correlação negativa com `Energy` e `Loudness`. |
| 😊 **Perfis de Gênero** | Gêneros como "Pop", "Latin" e "Hip-Hop" apresentam, em média, maior `Danceability` e `Valence` (positividade). |

---

### Interpretação da Correlação
A matriz de correlação gerada com Python (Seaborn) foi a principal ferramenta para validar as hipóteses do projeto.

![Matriz de Correlação](https://github.com/user-attachments/assets/4802387e-3c7d-4fc4-b6fa-1f7a1449fb0d)

A correlação extremamente forte (vermelho escuro) entre `energy` e `loudness` (r = 0.82) valida os dados. Músicas com mais energia são, de fato, mais "altas".
- **Trade-off de Produção:** `acousticness` tem uma forte correlação negativa (verde) com `energy` e `loudness`. Isso indica que faixas acústicas são inerentemente menos energéticas e mais silenciosas, um insight crucial para a curadoria de playlists.
- **O Driver da Popularidade:** Focando na linha `popularity`, os maiores valores positivos são `danceability` (0.22) e `energy` (0.23). Embora moderada, essa é a indicação mais clara de quais atributos estão ligados ao sucesso comercial de uma música.

---

## 💡 Insights Acionáveis (Análise)
Indo além dos números, os dashboards interativos revelam insights estratégicos para o negócio da música:

1.  **O Foco na Energia e Dançabilidade é Real:** O *Scatter Plot* (Popularidade vs. Atributos) confirma a descoberta da correlação. Os gêneros no quadrante superior direito (alta popularidade, alta dançabilidade) são potências comerciais. Para selos que buscam maximizar o alcance, focar em faixas com alta `danceability` e `energy` parece ser a estratégia de maior sucesso.

2.  **Cada Gênero tem um "DNA" de Áudio:** O *Heatmap* (Perfil de Áudio por Gênero) é o insight mais poderoso. Ele mostra que não se pode ter uma estratégia única.
    - **Exemplo:** "Opera" e "A Capella" têm `acousticness` altíssima (vermelho), enquanto "Electronic" e "Dance" têm baixíssima (verde). Promover uma faixa de "Pop" (alta `energy`) exige uma abordagem de marketing completamente diferente de uma faixa de "Classical" (baixa `energy`, alta `acousticness`).

3.  **Popularidade é um Jogo de Nicho vs. Massa:** O *Box Plot* (Distribuição de Atributos) mostra a variação. Enquanto a *média* de `energy` do "Pop" é alta, ainda existem faixas de "Pop" com baixa energia. Isso mostra que, embora a tendência seja de alta energia, há espaço para variação e subgêneros.

---

## 🗺️ Dashboard Preview

Este dashboard foi publicado no Tableau Public e é totalmente interativo. **Clique na imagem abaixo para acessá-lo.**

[![Preview do Dashboard](https://github.com/user-attachments/assets/59ffd5ba-58b0-4c83-82d1-101c1342460e)](https://public.tableau.com/shared/X9S2Q29ZK?:display_count=n&:origin=viz_share_link)

---

## 🧑‍💻 Author

**Ana Karolina Costa da Silva** 📍 Software Engineer & Data Science Researcher  
🎓 M.Sc. Computer Science — PUC-Rio  
💼 [LinkedIn](https://www.linkedin.com/in/karolyneehcs/) | [GitHub](https://github.com/karolyneehcs)
