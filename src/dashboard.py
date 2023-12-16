import streamlit as st
import os
import random

st.title("GAN Demo")
st.text("gan with 3 disentangled features")

# pick disentangled features
# options = st.multiselect(
#     'Select Disentangled features',
#     ['Grey hair', 'Red Lips', 'Mustache'],
#     ['Grey hair', 'Red Lips', 'Mustache'],
# )

if st.button('Generate'):
    random_idx = random.randint(1, 2)
    num_features = 3
    
    # st.image(f'/mount/src/spatialattganx/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png')
    
    input_path = f'/mount/src/spatialattganx/src/outputs/disentangled_features/{num_features}/input_{random_idx}.png'
    output_path = f'/mount/src/spatialattganx/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png'
    st.text("Original Image from GAN")
    st.image(input_path)
    st.text("GAN with Multiple Distangled features ['Grey hair', 'Red Lips', 'Mustache']")
    st.text(f"Total: {num_features} disentangled features")
    st.image(output_path)
