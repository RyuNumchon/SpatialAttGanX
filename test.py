import os
import random
print(os.getcwd())
random_idx = random.randint(1, 2)
num_features = len([1,2,3])
input_path = os.path.join(os.getcwd(),f'/src/outputs/disentangled_features/{num_features}/input_{random_idx}.png')
output_path = os.path.join(os.getcwd(),f'/src/outputs/disentangled_features/{num_features}/output_{random_idx}.png')
print(input_path)
print(output_path)