import numpy as np
from fractions import Fraction as frac

def solution(m):
    if len(m) == 1:
        return [1, 1]
    
    o, d = get_specs(m)
    M = standardize(m, o, d)

    # QR decomposition
    abs = d.count(0)                            # number of absorbing states
    tra = len(d) - abs                          # number of transient states

    Q = M[:tra, :tra]
    R = M[:tra, tra:]
    I = np.identity(tra)                        # identity matrix of size t
    N = np.linalg.inv((np.subtract(I, Q)))      # fundamental matrix
    P = np.dot(N, R)                            # limiting matrix

    proba = [frac.from_float(x).limit_denominator() for x in P[0]]

    lcm = np.lcm.reduce([f.denominator for f in proba])
    result = [int(f.numerator * lcm / f.denominator) for f in proba]
    result.append(lcm)

    return result


def get_specs(matrix):
    d = [sum(x) for x in matrix]                    # denominators
    pos = [(x, y) for x, y in enumerate(d)]         # make immutable position object

    t = [x for x in pos if x[1] != 0]               # transient states
    s = [x for x in pos if x[1] == 0]               # absorbing states

    order = [x[0] for x in t] + [x[0] for x in s]   # ordering for row and columns
    dlist = [x[1] for x in t] + [x[1] for x in s]   # ordered denom list
    return order, dlist

def standardize(matrix, order, dlist):
    # rearrange matrix in standard form
    std_matrix = []

    for i in range(len(dlist)):
        std_matrix.append([matrix[order[i]][x] for x in order])

    std_matrix = np.array(std_matrix, float)
    ones_matrix = np.ones((len(std_matrix), len(std_matrix)), float)

    for x, y in enumerate(dlist):
        if y != 0:
            ones_matrix[x] = ones_matrix[x]*y

    std_matrix = std_matrix/ones_matrix
    return std_matrix