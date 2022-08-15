from PIL import Image
import os
import sys

FILE_TYPES = ['.png','.jpeg','.ico','.icns', '.webp']
PATH = os.path.join(os.getcwd(), "images")
print(os.path.join(PATH, sys.argv[1]))

def valid_number(string):
    if string.isdigit():
        if int(string) >= 0 and int(string) <= 4:
            return True
    return False

if len(sys.argv) > 1:
    image_path = os.path.join(PATH, sys.argv[1])
    if os.path.exists(image_path):
        string = ""
        for i in range(len(FILE_TYPES)):
            string += f"{i} - {FILE_TYPES[i]}\n"
            
        im = Image.open(image_path)
        
        format = input(f"Select the number of which file type you would like:\n\n{string}\n")
        while not valid_number(format):
            format = input(f"Please select the integer of your file type between 0-4:\n\n{string}\n")
            
        target_name = os.path.join(PATH, sys.argv[1].split('.')[0] + FILE_TYPES[int(format)])
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved at " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: ImageConverter.py <file>")