import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 2

y_min = 0
y_max = 4


def f(x):
    return x ** 2


if __name__ == "__main__":
    x = np.linspace(-0.1, 2, 100)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.axhline(y=y_min, color='k', linestyle="--")
    ax.axhline(y=y_max, color='k', linestyle="--")
    ax.axvline(x=a, color='k', linestyle="--")
    ax.axvline(x=b, color='k', linestyle="--")

    fill_x = np.linspace(a, b, 100)
    fill_y = f(fill_x)
    ax.fill_between(fill_x, fill_y, color='yellow', alpha=0.5)

    plt.grid(True)
    plt.show()
