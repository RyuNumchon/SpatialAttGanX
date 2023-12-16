import streamlit as st
import os
import random
import time

st.title("GAN Demo")
st.text("gan with 3 disentangled features")

# pick disentangled features
# options = st.multiselect(
#     'Select Disentangled features',
#     ['Grey hair', 'Red Lips', 'Mustache'],
#     ['Grey hair', 'Red Lips', 'Mustache'],
# )

if st.button('Generate'):
    progress_text = "Generating faces"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(2)
    my_bar.empty()

    random_idx = random.randint(1, 2)
    num_features = 3  

    input_path = f'/mount/src/spatialattganx/src/outputs/disentangled_features/{num_features}/input_{random_idx}.png'
    output_path = f'/mount/src/spatialattganx/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png'
    
    st.text("Original Image from GAN")
    st.image(input_path)
    
    st.text("GAN with Multiple Distangled features ['Grey hair', 'Red Lips', 'Mustache']")
    st.text(f"Total: {num_features} disentangled features")
    st.image(output_path)

    
