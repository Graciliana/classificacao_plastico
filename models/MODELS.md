# ♻️ Classificação de Plásticos com Visão Computacional

Este projeto realiza a classificação de imagens de plásticos em 7 categorias usando diferentes algoritmos de machine learning aplicados a vetores extraídos das imagens em tons de cinza redimensionadas (`64x64`).

## 🔍 Objetivo

Avaliar e comparar o desempenho dos seguintes algoritmos:

* **Logistic Regression**
* **Naive Bayes**
* **Random Forest**
* **SVM (Support Vector Machine)**

---

## 📦 Dataset

O conjunto de dados contém imagens organizadas em pastas por classe: `PET`, `PP`, `PS`, `PVC`, `HDPE`, `LDPA`, `Other`, divididas em treino, validação e teste.

---

## 🤖 Modelos Utilizados

### 1. Logistic Regression

**Como funciona:**
Modelo estatístico que calcula a probabilidade de uma amostra pertencer a uma classe usando uma função logística (sigmoide). Para múltiplas classes, usamos a versão **multinomial softmax**.

**Uso na classificação de imagens:**
As imagens são transformadas em vetores (flatten), normalizadas e, opcionalmente, reduzidas com PCA. A regressão logística tenta encontrar um hiperplano que separe as classes.

**Vantagens:**

* Simples e interpretável
* Rápido para treinar
* Funciona bem com dados lineares

**Desvantagens:**

* Desempenho limitado com dados complexos
* Pouco robusto a ruído visual e sobreposição de classes

---

### 2. Naive Bayes

**Como funciona:**
Baseado no Teorema de Bayes, assume independência entre as variáveis de entrada (pixels). Estima a probabilidade de uma imagem pertencer a cada classe.

**Uso na classificação de imagens:**
Após transformação e normalização dos pixels, o modelo calcula as probabilidades de ocorrência de cada valor para cada classe.

**Vantagens:**

* Extremamente rápido
* Funciona bem mesmo com poucos dados
* Fácil de implementar

**Desvantagens:**

* Assunção de independência dos pixels raramente é verdadeira
* Baixo desempenho quando os atributos são correlacionados (como em imagens)

---

### 3. Random Forest

**Como funciona:**
Conjunto (ensemble) de árvores de decisão que votam para decidir a classe final. Cada árvore é treinada com um subconjunto aleatório de dados e atributos.

**Uso na classificação de imagens:**
Após vetorizar as imagens, cada árvore tenta capturar padrões locais dos pixels. A média dos votos das árvores define a classe final.

**Vantagens:**

* Robusto ao overfitting
* Lida bem com dados não lineares
* Funciona com variáveis ruidosas

**Desvantagens:**

* Pode ser lento em inferência
* Modelo grande, difícil de interpretar

---

### 4. SVM (Support Vector Machine)

**Como funciona:**
Busca um hiperplano que maximize a margem entre as classes. Com o kernel RBF, consegue separar classes com limites não lineares.

**Uso na classificação de imagens:**
Após a redução da dimensionalidade (PCA), o SVM busca uma fronteira ótima entre as classes em um espaço de menor dimensão.

**Vantagens:**

* Excelente desempenho em datasets com margens claras entre as classes
* Robusto a outliers
* Muito eficaz em espaços com muitas dimensões

**Desvantagens:**

* Treinamento mais lento
* Pouco escalável para grandes volumes de dados

---

## 📊 Métricas Avaliadas

* **Acurácia**
* **F1-score ponderado**
* **Log Loss**
* **Tempo de treinamento**
* **Tempo de inferência por imagem**
* **Matriz de confusão**
* **Visualização das previsões**

---

## 📁 Estrutura dos Notebooks

* `01_logistic_regression.ipynb`
* `02_naive_bayes.ipynb`
* `03_random_forest.ipynb`
* `04_svm.ipynb`
* `comparacao_modelos.ipynb`

---

## 🚀 Próximos passos

* Explorar redes neurais (CNNs)
* Avaliar com imagens RGB
* Aplicar técnicas de aumento de dados (Data Augmentation)
* Implementar interface com Streamlit para demonstração interativa
