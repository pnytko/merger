from PIL import Image
import numpy as np
import argparse
import glob
import os
import re
import warnings
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("--path", type = str, required = True)
args = parser.parse_args()

formatted_input = args.path + '\*.*'

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
        corner0 = re.findall('_[0-9]+', word[i])[-2]
        corner1 = re.findall('_[0-9]+', word[i])[-1]
        corner_values.append([int(corner0.replace('_', '')), int(corner1.replace('_', ''))])
        #Type conversion
    # for j in corner_values:
    #     j[0] = int(corner0[0].replace('_', ''))
    #     j[1] = int(corner1[1].replace('_', ''))

    return corner_values

def dictionary_fitting(k, v):
    #Dict structure - IMPORTANT
    dict = [(k[i], v[i][0], v[i][1]) for i in range(len(k))]
    return dict

def dictionary_analysis(input_dict):
    corners_list = []
    group_paths = []
    for input_ele in input_dict:
        if [input_ele[1]] not in corners_list:
            corners_list.append([input_ele[1]])
            group_paths.append([])
    for i in range (len(corners_list)):
        for input_ele in input_dict:
            if corners_list[i][0] == input_ele[1]:
                group_paths[i].append(input_ele[0])

    return group_paths

def merge_v_images(v_input):
    h_imgs = []
    for group in v_input:
        opened_images = [Image.open(img) for img in group]
        imgs_comb = np.hstack((np.asarray(img) for img in opened_images))
        imgs_comb = Image.fromarray(imgs_comb)
        h_imgs.append(imgs_comb)
    out_image = np.vstack((np.asarray(img) for img in h_imgs))
    out_image = Image.fromarray(out_image)
    out_image.save('out.tif')


#Multireturn defining - IMPORTANT
image_separated, image_paths = load_images(formatted_input)
c_value = regex_solution(image_separated)
dict_to_analyse = dictionary_fitting(image_paths, c_value)

sorted_tup = sorted(dict_to_analyse,key=itemgetter(2))
sorted_tup = sorted(sorted_tup,key=itemgetter(1))

grouped_analysis = dictionary_analysis(sorted_tup)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    merge_v_images(grouped_analysis)
