# June 13
# Converts JPG to PNG
# takes two arguments, folder with jpg images and new folder with png 

import sys
import os
from PIL import Image

# python3 JPEGtoPNGconverter.py Pokedex/ new/

# first and second arguments through sys
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through files in folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]  # removes '.jpg' from filename
    img.save(f'{output_folder}{clean_name}.png', 'png')








