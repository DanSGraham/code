"""

    >>> from scipy import array, matrix

    >>> from pybrain.auxiliary.pca import makeCentered

    >>> data = array([[2.5, 2.4],
    ...               [0.5, 0.7],
    ...               [2.2, 2.9],
    ...               [1.9, 2.2],
    ...               [3.1, 3.0],
    ...               [2.3, 2.7],
    ...               [2.0, 1.6],
    ...               [1.0, 1.1],
    ...               [1.5, 1.6],
    ...               [1.1, 0.9]])

    >>> makeCentered(data)
    array([[ 0.69,  0.49],
           [-1.31, -1.21],
           [ 0.39,  0.99],
           [ 0.09,  0.29],
           [ 1.29,  1.09],
           [ 0.49,  0.79],
           [ 0.19, -0.31],
           [-0.81, -0.81],
           [-0.31, -0.31],
           [-0.71, -1.01]])


Tests for regular PCA
---------------------

    >>> from pybrain.auxiliary.pca import pca, reduceDim

    >>> pca(data, 1)
    array([[-0.6778734 , -0.73517866]])

    >>> reduceDim(data, 1)
    matrix([[-0.82797019],
            [ 1.77758033],
            [-0.99219749],
            [-0.27421042],
            [-1.67580142],
            [-0.9129491 ],
            [ 0.09910944],
            [ 1.14457216],
            [ 0.43804614],
            [ 1.22382056]])

    >>> reduceDim(data, 2)
    matrix([[-0.82797019, -0.17511531],
            [ 1.77758033,  0.14285723],
            [-0.99219749,  0.38437499],
            [-0.27421042,  0.13041721],
            [-1.67580142, -0.20949846],
            [-0.9129491 ,  0.17528244],
            [ 0.09910944, -0.3498247 ],
            [ 1.14457216,  0.04641726],
            [ 0.43804614,  0.01776463],
            [ 1.22382056, -0.16267529]])

    >>> data2 = matrix([
    ... [2.4, 2.5],
    ... [0.7, 0.5],
    ... [2.9, 2.2],
    ... [2.2, 1.9],
    ... [3.0, 3.1],
    ... [2.7, 2.3],
    ... [1.6, 2.0],
    ... [1.1, 1.0],
    ... [1.6, 1.5],
    ... [0.9, 1.1]])

    >>> reduceDim(data2, 2)
    matrix([[ 0.17511531,  0.82797019],
            [-0.14285723, -1.77758033],
            [-0.38437499,  0.99219749],
            [-0.13041721,  0.27421042],
            [ 0.20949846,  1.67580142],
            [-0.17528244,  0.9129491 ],
            [ 0.3498247 , -0.09910944],
            [-0.04641726, -1.14457216],
            [-0.01776463, -0.43804614],
            [ 0.16267529, -1.22382056]])

    >>> data3 = matrix([
    ... [7.0, 4.0, 3.0],
    ... [4.0, 1.0, 8.0],
    ... [6.0, 3.0, 5.0],
    ... [8.0, 6.0, 1.0],
    ... [8.0, 5.0, 7.0],
    ... [7.0, 2.0, 9.0],
    ... [5.0, 3.0, 3.0],
    ... [9.0, 5.0, 8.0],
    ... [7.0, 4.0, 5.0],
    ... [8.0, 2.0, 2.0]])

    >>> reduceDim(data3, 1)
    matrix([[-2.15142276],
            [ 3.80418259],
            [ 0.15321328],
            [-4.7065185 ],
            [ 1.29375788],
            [ 4.0993133 ],
            [-1.62582148],
            [ 2.11448986],
            [-0.2348172 ],
            [-2.74637697]])

Tests for probabilistic PCA
---------------------------

    >>> from pybrain.auxiliary.pca import pPca

    >>> pc = pPca(data, 1)
    >>> x, y = pc[0, 0], pc[0, 1]
    >>> x / y
    0.92...

"""


__author__ = 'Justin Bayer, bayerj@in.tum.de'

from pybrain.tests import runModuleTestSuite

if __name__ == "__main__":
    runModuleTestSuite(__import__('__main__'))

