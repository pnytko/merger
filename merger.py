from PIL import Image
import numpy as np
from itertools import product
import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("--dir_in", type = str, required = True)
args = parser.parse_args()

formatted_input = args.dir_in + '\*.*'

def load_images(img_path):
    image_paths = glob.glob(img_path)
    image_filenames = list(map(os.path.basename, image_paths))
    image_splitted = list(map(os.path.splitext, image_filenames))
    image_separated = []
    for i in range(len(image_splitted)):
        print(image_splitted[i][0])  
    opened_images = [Image.open(i) for i in image_paths]

load_images(formatted_input)

#os.path.splitext
