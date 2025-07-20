
# 📦 Classificação de Plásticos com MobileNetV2 + Otimizações

Este projeto utiliza redes neurais convolucionais (CNNs) com _transfer learning_ usando a arquitetura **MobileNetV2**, aplicada à **classificação de imagens de plásticos recicláveis** em 3 categorias. O foco está em otimizar o desempenho do modelo, melhorar generalização com `data augmentation` e garantir reprodutibilidade.

---

## ✅ Objetivos

- Classificar imagens de plásticos em três classes distintas.
- Utilizar MobileNetV2 com fine-tuning e preprocessamento adequado.
- Comparar o desempenho com outras abordagens (como CNN simples).
- Aplicar boas práticas de otimização de pipelines TensorFlow.
- Visualizar e salvar as métricas para comparações futuras.

---

## 📁 Estrutura do Notebook

### 1. **Preparação dos Dados**

- Leitura do dataset de imagens.
- Divisão em `train`, `val`, `test`.
- Visualização amostral por classe.

### 2. **Pré-processamento**

- Aplicação de `data augmentation` com:
  - Flip horizontal
  - Rotação aleatória
  - Zoom
  - Brilho (via `tf.image`)
- Normalização com `preprocess_input` da MobileNetV2.

### 3. **Pipeline otimizado**

- Cache, shuffle e `prefetch` com `AUTOTUNE`.

### 4. **Construção do Modelo**

- Uso da MobileNetV2 pré-treinada (ImageNet).
- Fine-tuning das camadas finais.
- Camadas adicionais com dropout e softmax.

### 5. **Treinamento**

- Compilação com Adam, `categorical_crossentropy`.
- Treinamento com `EarlyStopping` e `ModelCheckpoint`.

### 6. **Avaliação**

- Acurácia e perda em teste.
- Métricas: F1-score, Log Loss, tempo de treino e inferência.
- Curvas ROC multiclasses.
- Matriz de confusão.
- Amostras visuais de classificações corretas/incorretas.

### 7. **Comparação entre modelos**

- MobileNetV2 vs CNN simples.
- Tabela de métricas consolidada.
- Visualização lado a lado das curvas ROC.
- Tamanho dos modelos salvos (.keras).
- Gravação das métricas em `metrics_results.csv`.

---

## 📊 Resultados

| Modelo           | Acurácia | F1-score | Log Loss | Parâmetros | Tamanho (MB) | Tempo de Inferência (ms) |
|------------------|----------|----------|----------|-------------|----------------|---------------------------|
| MobileNetV2      | ✅ ...   | ✅ ...   | ✅ ...   | ...         | ... MB         | ... ms                    |
| CNN Simples      | ...      | ...      | ...      | ...         | ... MB         | ... ms                    |

> 📌 *Resultados reais são preenchidos ao final do notebook automaticamente.*

---

## 🧪 Reproduzindo o Projeto

1. Clonar o repositório ou abrir o notebook `09_cnn_mobileNetV2-otimizado.ipynb`.

2. Certifique-se de ter as bibliotecas:

```bash
pip install tensorflow numpy pandas matplotlib scikit-learn seaborn
```

3. Execute as células em ordem.


---

## 🧠 Tecnologias

- Python 3.10+
- TensorFlow / Keras
- scikit-learn
- Matplotlib & Seaborn

---

## 📁 Arquivos Gerados

- `models/mobilenetv2_model.keras` — modelo salvo.
- `metrics_results.csv` — comparação entre modelos.
- Gráficos de curva ROC, confusão, predições visuais.

---

## ✍️ Autora

**Graciliana Kascher**  
🔗 [LinkedIn](https://www.linkedin.com/in/gracilianakascher/) 