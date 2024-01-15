import numpy as np
import matplotlib.pyplot as plt
from colbarlib import example

# Generate random numbers
random_numbers = np.random.rand(15, 10)


# Plot the random numbers using segmented colormap
plt.imshow(random_numbers, cmap=example.segmented)
