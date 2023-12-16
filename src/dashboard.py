import streamlit as st
import os
import random

st.title("GAN Demo [WIP]")
st.text("gan with disentangled features")

# pick disentangled features
options = st.multiselect(
    'Select Disentangled features',
    ['Grey hair', 'Red Lips', 'Mustache'],
    ['Grey hair', 'Red Lips', 'Mustache'],
)

if st.button('Generate'):
    random_idx = random.randint(1, 2)
    num_features = len(options)
    print(os.getcwd())
    st.image(f'src/outputs/disentangled_features/{num_features}/output_{random_idx}.png')
    st.text("Original Image from GAN")
    input_path = f'src/outputs/disentangled_features/{num_features}/input_{random_idx}.png'
    st.text("GAN with Multiple Distangled features")
    st.text(f"Total: {num_features} disentangled features")
    output_path = f'src/outputs/disentangled_features/{num_features}/output_{random_idx}.png'
    st.image(input_path)
    st.image(output_path)
