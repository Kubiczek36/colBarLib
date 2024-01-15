# colBarLib

## Description

colBarLib is a Python software library that provides functionality for creating color bar plots. It is designed to be easy to use and customizable.

## Installation

To install colBarLib, you can use pip:

    ```bash
    pip install -e .
    ```

## Usage

    ```python
    import colBarLib as cbl
    import numpy as np
    import matplotlib.pyplot as plt

    # Create a color bar plot
    fig, ax = plt.subplots()
    plt.imshow(np.random.rand(10, 10), cmap=cbl.example.segmented)
    plt.show()
    ```
