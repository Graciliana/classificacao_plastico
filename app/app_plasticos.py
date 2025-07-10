import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Carregar modelo treinado
model = tf.keras.models.load_model("../modelos/modelos/modelo_cnn_simples_plasticos.keras")

# Nome das classes
class_names = ["HDPE", "LDPA", "Other", "PET", "PP", "PS", "PVC"]

# Título
st.title("🧪 Classificador de Plásticos com CNN")
st.write("Envie uma imagem para prever o tipo de plástico.")

# Upload de imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abrir imagem com PIL
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagem enviada", use_column_width=True)

    # Pré-processamento
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    
    img_array = img_array / 255.0  # normalização
    img_array = np.expand_dims(img_array, axis=0)  # (1, 224, 224, 3)

    # Previsão
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    st.subheader("🔍 Previsão")
    st.markdown(f"**Classe predita:** `{predicted_class}`")
