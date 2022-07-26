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
    
    return image_separated, image_paths

def regex_solution(word):
    corner_values = []
    for i in range(len(word)):
        string_analyse = (re.findall('[0-9]+', word[i]))
        corner_values.append(string_analyse)
        #Type conversion
    for j in corner_values:
        j[0] = int(j[0])
        j[1] = int(j[1])

    return corner_values

def dictionary_fitting(k, v):
    #Dict structure - IMPORTANT
    dict = [{'path': k[i], 'corners': v[i]} for i in range(len(k))]
    return dict

def dictionary_analysis(input_dict):
    for i in input_dict:
        #print(i['corners'][0])
        pass


#Multireturn defining - IMPORTANT
image_separated, image_paths = load_images(formatted_input)
c_value = regex_solution(image_separated)
dict_to_analyse = dictionary_fitting(image_paths, c_value)

analiza = dictionary_analysis(dict_to_analyse)
#print(dict_to_analyse)


#opened_images = [Image.open(j) for j in image_paths]
