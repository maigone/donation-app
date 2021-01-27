import math
from scipy.integrate import quad
from numpy import inf


def gamma(num: float) -> float:
    if num <= 0:
        raise ValueError("math domain error")

    return quad(integrand, 0, inf, args=(num))[0]


def integrand(x: float, z: float) -> float:
    return math.pow(x, z - 1) * math.exp(-x)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
