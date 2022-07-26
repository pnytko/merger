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
    #Data presentation
    #print(image_separated)
    #print(len(image_separated))
    
    return image_separated, image_paths

def regex_solution(word):
    corner_values = []
    for i in range(len(word)):
        string_analyse = (re.findall('[0-9]+', word[i]))
        corner_values.append(string_analyse)
    #Data presentation
    #print(corner_values)
    #print(len(corner_values))

    return corner_values

def dictionary_fitting(k, v):
    dict = {k[i]: v[i] for i in range(len(k))}
    #print(dict)
    
    return dict
    
#filtered_list = load_images(formatted_input)
#c_value = regex_solution(filtered_list)
#dict_to_analyse = dictionary_fitting(filtered_list, c_value)

#Multireturn defining - IMPORTANT
image_separated, image_paths = load_images(formatted_input)
c_value = regex_solution(image_separated)
dict_to_analyse = dictionary_fitting(image_paths, c_value)

print(dict_to_analyse)
#opened_images = [Image.open(j) for j in image_paths]
