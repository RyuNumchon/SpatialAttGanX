import streamlit as st
import os
import random


# pick disentangled features
options = st.multiselect(
    'Select Disentangled features',
    ['Grey hair', 'Red Lips', 'Mustache'],
    ['Grey hair', 'Red Lips', 'Mustache'],
)

st.button("Generate", type="primary")

if st.button('Generate'):
    random_idx = random.randint(1, 2)
    num_features = len(options)
    input_path = os.path.join(os.getcwd(),f'SpatialAttGanX/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png')
    output_path = os.path.join(os.getcwd(),f'SpatialAttGanX/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png')
    st.image(input_path)
    st.image(output_path)
