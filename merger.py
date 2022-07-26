from PIL import Image
import numpy as np
import argparse
import glob
import os
import re
import itertools
import warnings

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
    corners_list = []
    group_paths = []
    for input_ele in input_dict:
        if [input_ele['corners'][0]] not in corners_list:
            corners_list.append([input_ele['corners'][0]])
            group_paths.append([])
    for i in range (len(corners_list)):
        for input_ele in input_dict:
            if corners_list[i][0] == input_ele['corners'][0]:
                group_paths[i].append(input_ele['path'])

    return group_paths

def merge_v_images(v_input):
    h_imgs = []
    for group in v_input:
        opened_images = [Image.open(img) for img in group]
        # opened_images = [Image.open(img) for i in range(len(v_input)) for img in v_input[i]]
        imgs_comb = np.hstack( (np.asarray(img) for img in opened_images))
        imgs_comb = Image.fromarray(imgs_comb)
        h_imgs.append(imgs_comb)
    out_image = np.vstack( (np.asarray(img) for img in h_imgs))
    out_image = Image.fromarray(out_image)
    out_image.save('out.jpg')


#Multireturn defining - IMPORTANT
image_separated, image_paths = load_images(formatted_input)
c_value = regex_solution(image_separated)
dict_to_analyse = dictionary_fitting(image_paths, c_value)
grouped_analysis = dictionary_analysis(dict_to_analyse)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    merge_v_images(grouped_analysis)
