# Algoritmos de aprendizado profundo

Na **visão computacional**, diversos algoritmos são utilizados para **classificação de objetos em imagens**, dependendo da complexidade do problema, da disponibilidade de dados e da capacidade computacional. Esses algoritmos podem ser divididos em duas categorias principais:

---

## 🧠 **1. Modelos baseados em aprendizado profundo (Deep Learning)**

Esses são os mais utilizados atualmente para tarefas de classificação de objetos, devido à sua alta precisão e capacidade de aprender diretamente dos dados.

## ✅ **Redes Neurais Convolucionais (CNNs)**

Usadas para extrair automaticamente padrões espaciais e texturas em imagens.

* **Modelos clássicos**:

  * **LeNet** – usado em imagens simples como dígitos.
  * **AlexNet** – pioneiro no uso de ReLU e dropout.
  * **VGG16 / VGG19** – usa várias camadas convolucionais com kernel 3x3.
  * **ResNet (ResNet50, ResNet101...)** – usa conexões residuais para redes muito profundas.
  * **Inception / GoogLeNet** – usa convoluções de diferentes tamanhos paralelamente.
  * **MobileNet / EfficientNet** – versões leves para dispositivos móveis.
  * **DenseNet** – cada camada é conectada a todas as anteriores.

### ✅ **Transformers Visuais (Vision Transformers - ViT)**

Modelos recentes que substituem CNNs por mecanismos de atenção:

* Exemplo: **ViT**, **Swin Transformer**.

#### ✅ **YOLO (You Only Look Once)**

Usado para **detecção e classificação simultânea** de objetos (não só a classe, mas também a posição):

* **YOLOv5, YOLOv6, YOLOv8** – muito populares por sua velocidade.
* Também fazem **classificação de múltiplos objetos em uma imagem.**

---

### 📊 **2. Algoritmos de Machine Learning tradicionais**

São úteis quando as imagens são previamente **transformadas em vetores de características (feature extraction manual)**, por exemplo com HOG, SIFT, LBP etc.

### ✅ **Algoritmos comuns**:

* **SVM (Support Vector Machine)** – muito usado com boas extrações de características.
* **KNN (K-Nearest Neighbors)** – simples, baseado em similaridade.
* **Random Forest** – conjunto de árvores de decisão, robusto a ruídos.
* **Gradient Boosting (XGBoost, LightGBM)** – muito precisos em datasets estruturados.
* **Logistic Regression / Naive Bayes** – para problemas mais simples.

> Obs: Esses algoritmos **não operam diretamente com imagens brutas**. É necessário usar alguma técnica de **extração de características** antes (como PCA, HOG ou autoencoders).

---

### 🔍 Exemplos de aplicações com algoritmos

| Tarefa                         | Algoritmo Comum                   |
| ------------------------------ | --------------------------------- |
| Classificação de imagem única  | CNNs (ex: ResNet, MobileNet)      |
| Classificação em tempo real    | YOLOv8, MobileNet                 |
| Classificação com poucos dados | SVM + HOG, ou fine-tuning com CNN |
| Classificação multi-label      | CNNs com sigmoid na saída         |
| Classificação + Localização    | YOLO, Faster R-CNN                |

---