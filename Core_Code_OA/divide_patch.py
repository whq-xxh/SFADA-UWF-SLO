from PIL import Image
import os


# def resize_and_split_image(image_path, output_dir, new_width=4096, new_height=3072, patch_size=256):

#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     with Image.open(image_path) as img:
#         resized_img = img.resize((new_width, new_height))    

#         base_name = os.path.basename(image_path)
#         name, ext = os.path.splitext(base_name)
        
#         patch_number = 1
#         for i in range(0, new_height, patch_size):
#             for j in range(0, new_width, patch_size):

#                 box = (j, i, j + patch_size, i + patch_size)
#                 patch = resized_img.crop(box)
        
#                 patch_filename = f"{name}_{patch_number}{ext}"
#                 patch_path = os.path.join(output_dir, patch_filename)
#                 patch.save(patch_path)
#                 print(f"Saved patch: {patch_path}")
                
#                 patch_number += 1

# image_path = '/home/whq/' 
# output_dir = '/home/whq'
# resize_and_split_image(image_path, output_dir)
# print("okkk")




from PIL import Image
import os
def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))

def is_original_image(filename):

    return not any(part.isdigit() for part in filename.split('_'))

def resize_and_split_image(image_path, output_dir, patch_size=(260, 256)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with Image.open(image_path) as img:
        original_width, original_height = img.size

        num_patches_x = original_width // patch_size[0]
        num_patches_y = original_height // patch_size[1]
        
        base_name = os.path.basename(image_path)
        name, ext = os.path.splitext(base_name)
        
        patch_number = 1
        for i in range(num_patches_y):
            for j in range(num_patches_x):
                left = j * patch_size[0]
                upper = i * patch_size[1]
                right = left + patch_size[0]
                lower = upper + patch_size[1]
                box = (left, upper, right, lower)
                patch = img.crop(box)
                
                patch_filename = f"{name}_{patch_number}{ext}"
                patch_path = os.path.join(output_dir, patch_filename)
                patch.save(patch_path)
                print(f"Saved patch: {patch_path}")          
                patch_number += 1

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if is_image_file(filename) and is_original_image(filename):
            file_path = os.path.join(folder_path, filename)
            
            resize_and_split_image(file_path, folder_path)
            
            os.remove(file_path)
            print(f"Deleted original image: {file_path}")


folder_path = '/home/whq/HKUST/Seg/'  
process_images_in_folder(folder_path)
print(len(os.listdir(folder_path)))

