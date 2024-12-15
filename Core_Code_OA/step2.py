# Step 2 
# Assuming you already have a txt file with image patch names and a folder with those image patchs
# The following code will read the image patch names in the txt file, calculate the pixel sum of each image patch, and then select the half of the image patchs with the largest sum
# The sorted image names will be saved to a new txt file
import os
from PIL import Image
import numpy as np

def process_images_and_save_top_half(input_txt, input_folder, output_txt):
    image_sums = []
    
# Read the image patch name from the txt file
    with open(input_txt, 'r') as file:
        image_names = file.read().splitlines()
    print(len(image_names))
# Calculate the sum of pixel values ​​for each image pacth
    for img_name in image_names:
        img_path = os.path.join(input_folder, img_name)
        with Image.open(img_path) as img:
            img_sum = np.array(img).sum()
            image_sums.append((img_name, img_sum))
    
    image_sums.sort(key=lambda x: x[1], reverse=True)
    percentage = 0.5 
    top_percentage_images = image_sums[:int(len(image_sums) * percentage)]
    top_percentage_images.sort()

    with open(output_txt, 'w') as f:
        for img_name, _ in top_percentage_images:
            f.write(f"{img_name}\n")


input_txt = '/home/'  # Enter the C1 selected txt file path
input_folder = '/home/'  # The path to the folder where the image patch is located (value for Predominance)
output_txt = '/home/'  # Output txt file path
process_images_and_save_top_half(input_txt, input_folder, output_txt)