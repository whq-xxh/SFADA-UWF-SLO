from PIL import Image
import os

def combine_patches_to_image(folder_path, patch_size=(260, 256)):
# Dict, used to store the patches information of each original image
    images_patches = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            name, ext = os.path.splitext(filename)
            original_name, patch_number = name.rsplit('_', 1)
            
# Store patch information in a dict
            if original_name not in images_patches:
                images_patches[original_name] = []
            images_patches[original_name].append(filename)
    
# For each original image, combine its patches
    for original_name, patches in images_patches.items():
# Sort patches to ensure correct order
        patches.sort(key=lambda x: int(x.rsplit('_', 1)[1].split('.')[0]))
        
# Use the first patch to determine the mode of the new image
        first_patch = Image.open(os.path.join(folder_path, patches[0]))
        mode = first_patch.mode

        original_image = Image.new(mode, (3900, 3072))
        for patch_filename in patches:
            with Image.open(os.path.join(folder_path, patch_filename)) as patch:
# Calculate the position of the patch in the original image from the patch number
                _, patch_number = patch_filename.rsplit('_', 1)
                patch_number = int(patch_number.split('.')[0])
                row = (patch_number - 1) // (3900 // patch_size[0])
                col = (patch_number - 1) % (3900 // patch_size[0])
                x, y = col * patch_size[0], row * patch_size[1]
                original_image.paste(patch, (x, y))
        
# Save the combined original image
        original_image.save(os.path.join(folder_path, original_name + '.png'))
        print(f"Saved combined image: {original_name}.png")

        for patch_filename in patches:
            os.remove(os.path.join(folder_path, patch_filename))
            print(f"Deleted patch: {patch_filename}")

folder_path = '/home/whq/HKUST/Seg/' 
combine_patches_to_image(folder_path)
