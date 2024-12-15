import shutil
import os

def move_images_based_on_txt(txt_file, source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    with open(txt_file, 'r') as file:
        image_names = file.read().splitlines()

    for img_name in image_names:
        source_path = os.path.join(source_folder, img_name)
        target_path = os.path.join(target_folder, img_name)      
        shutil.move(source_path, target_path)
        print(f"Moved {img_name} to {target_folder}")


txt_file = '/home/'  # The path to the txt file containing the names of the image patchs to be moved
source_folder = '/home/'  
target_folder = '/home/'  

move_images_based_on_txt(txt_file, source_folder, target_folder)
