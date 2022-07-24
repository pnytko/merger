from os import listdir
from os.path import isfile, join
from PIL import Image
from itertools import product
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--dir_in", type = str, required = True)
args = parser.parse_args()

formatted_input = args.dir_in + '\*.*'

def merge(dir_in):
    list_dir = glob.glob(dir_in)
    imgs = [Image.open(i) for i in list_dir]
    imgs.show()
merge(formatted_input)
