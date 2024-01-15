## imports
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import matplotlib as mpl
import numpy as np

## colormaps

# listed
listed_cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])

# modified viridis
viridis = mpl.colormaps['viridis'].resampled(256)

newcolors = viridis(np.linspace(0, 1, 256))
pink = np.array([248/256, 24/256, 148/256, 1])
newcolors[:25, :] = pink

cuted_viridis = ListedColormap(newcolors)

# linear neon
colors = ["darkorange", "gold", "lawngreen", "lightseagreen"]
lin_neon = LinearSegmentedColormap.from_list("Linear neon", colors)

# modified linear neon
nodes = [0.0, 0.4, 0.9, 1.0]
lin_neon_mod = LinearSegmentedColormap.from_list("Modified linear neon", list(zip(nodes, colors)))

# modified  with RGB codes

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
