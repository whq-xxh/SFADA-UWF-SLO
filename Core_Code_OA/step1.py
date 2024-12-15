# Step 1
#Split the image containing Uncertainty values into small patches (C1 Uncertainty), and then select them in Step 1
import os
from PIL import Image
import numpy as np

def select_and_save_top_images(input_folder, output_txt, top_percentage=0.1):
    image_sums = []
    
    # Iterate through all files in a folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(input_folder, filename)
            with Image.open(file_path) as img:
                img_sum = np.array(img).sum()
                image_sums.append((filename, img_sum))
    
    # Sort by the total number of images and select the largest 10%
    image_sums.sort(key=lambda x: x[1], reverse=True)
    top_images = image_sums[:int(len(image_sums) * top_percentage)]
    top_images_sorted = sorted(top_images, key=lambda x: x[0])
    

    with open(output_txt, 'w') as f:
        for img_name, _ in top_images_sorted:
            f.write(f"{img_name}\n")


input_folder = '/home/uncer_patch_value'  # Replace with your input folder path
output_txt = '/home/uncer_patch.txt'  # Output the name of the txt file
select_and_save_top_images(input_folder, output_txt)