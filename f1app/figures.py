import matplotlib.pyplot as plt
import numpy as np

def my_figure():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y)
    return fig