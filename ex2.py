import numpy as np
import scipy.integrate as spi

from ex2_plt import f, a, b, y_max, y_min


def monte_carlo(f, a, b, y_min, y_max, n):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(y_min, y_max, n)
    under_curve = np.sum(y < f(x))
    print(under_curve)
    area = (b - a) * (y_max - y_min) * (under_curve / n)
    return area


if __name__ == "__main__":
    # result, err = integrate.quad(f, a, b)  # noqa
    mc_result = monte_carlo(f, a, b, y_min, y_max, 10_000)
    result, err = spi.quad(f, a, b)
    print(f'Monte Carlo result: {mc_result: .5f}, Scipy result: {result: .5f}')
