from PIL import Image
import numpy as np
import argparse
import glob
import os
import re

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
        entry = image_splitted[i][0]
        image_separated.append(entry)
    return image_separated

filtered_list = load_images(formatted_input)
temp_entry = (filtered_list[1])

def regex_solution(word):
    corner_values = []
    for i in range(len(word)):
        string_analyse = re.findall('[0-9]+', word[i])
        print(string_analyse)

regex_solution(filtered_list)

#TODO - dictionary

#opened_images = [Image.open(j) for j in image_paths]
