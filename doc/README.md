# documentação do que foi realizado

- Carregar o conjunto de dados Plastic_Classification

- O pré-processamento

Abaixo está um **guia estruturado** com as **principais etapas** de pré-processamento, focado no seu caso de imagens de plásticos:

---

## 🧪 Etapas de Pré-Processamento para Classificação de Plásticos

---

### 1. **Padronização dos Arquivos**

🔹 **✔️ O que você já fez:**

- ✅ Renomeou imagens (ex: `image_1.jpg`, ...)
- ✅ Padronizou as extensões para `.jpg`
- ✅ Verificou e corrigiu o formato real para `JPEG`

🔹 **Boa prática:**

- Remover arquivos corrompidos, duplicados ou de extensão indesejada ('.avif', '.webp', etc.)

---

### 2. **Padronização de Dimensões**

📏 **Tornar todas as imagens do mesmo tamanho**, ex: `224x224` ou `256x256`.

🔧 Isso é essencial para:

- Treinar CNNs (como ResNet, VGG, MobileNet, etc.)
- Aumentar performance do treinamento

```python
img = img.resize((224, 224))
```

---

### 3. **Conversão de Canais de Cor**

🎨 Padronizar para `RGB` (3 canais)

Você já fez isso com:

```python
img = img.convert('RGB')
```

---

### 4. **Normalização de Pixels**

📊 Converter os valores dos pixels para uma escala entre `0 e 1` (ou `-1 a 1`, dependendo do modelo).

```python
img_array = np.array(img) / 255.0
```

> Alguns modelos como `ResNet50` usam normalização específica: `preprocess_input(img_array)`.

---

### 5. **Balanceamento de Classes**

⚠️ Se algumas classes têm muito menos imagens (ex: `PS`), você deve:

- **Usar aumento de dados (data augmentation)** para gerar mais imagens dessa classe
- Ou aplicar **reweighting** no treino com `class_weight` (em Keras ou PyTorch)

---

### 6. **Data Augmentation (opcional, mas recomendado)**

📈 Aumenta a variedade e robustez do modelo:

```python
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1
)
```

> Use apenas no **conjunto de treino**!

---

### 7. **Separação dos dados**

📂 Certifique-se de que o dataset esteja organizado assim:

```python
Plastic_Classification/
    ├── train/
    │   ├── PET/
    │   ├── PS/
    ├── validation/
    ├── test/
```

---

### 8. **Geradores de Imagens para Treinamento**

✅ Use geradores como `ImageDataGenerator` ou `tf.keras.utils.image_dataset_from_directory()`:

```python
train_gen = datagen.flow_from_directory(
    '.../train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
```

---

### 9. **Codificação de Rótulos**

🎯 Se o modelo usa `categorical_crossentropy`, codifique os rótulos com `OneHotEncoder` ou `to_categorical`.

---

### 10. **Divisão entre Treino, Validação e Teste**

🧪 Se ainda não tiver separado, pode usar:

```python
from sklearn.model_selection import train_test_split
```

Mas como seu dataset já está em pastas, você pode manter essa estrutura.

---

### ✅ Checklist final antes de treinar

| Etapa                               | Status |
| ----------------------------------- | ------ |
| ✔️ Formato e extensão padronizados  | ✅      |
| ✔️ Redimensionamento                | 🚧     |
| ✔️ RGB                              | ✅      |
| ✔️ Normalização                     | 🚧     |
| ✔️ Balanceamento das classes        | 🚧     |
| ✔️ Augmentation                     | 🚧     |
| ✔️ Separação treino/teste/validação | ✅      |

---


