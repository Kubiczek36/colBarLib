## imports
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib as mpl
import numpy as np

brown = (48, 49, 31, 255)
brown = np.array(brown)/255
dark_green = (50, 58, 57, 255)
dark_green = np.array(dark_green)/255
light_green = (122, 132, 69, 255)
light_green = np.array(light_green)/255
yellow = (179, 172, 86, 255)
yellow = np.array(yellow)/255
orange = (196, 160, 78, 255)
orange = np.array(orange)/255
red = (177, 97, 53, 255)
red = np.array(red)/255
dark_red = (125, 35, 35)
dark_red = np.array(dark_red)/255 * 1.1

segmented = LinearSegmentedColormap.from_list("segmented", [brown, light_green, yellow, orange, red, dark_red])
