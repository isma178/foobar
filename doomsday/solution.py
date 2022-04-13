def solution(m):
    import numpy as np
    from fractions import Fraction as frac
    
    den = [sum(x) for x in m]
    
    m = np.array(m)
    o = np.ones((len(m), len(m)))
    s = den.count(0)                                # absorbing states
    t = len(den) - s                                # transient states

    for x, y in enumerate(den):
        o[x] = o[x]*y
    
    m = m/o

    # assuming the matrix is arranged perfectly...

    Q = m[:t, :t]
    R = m[:t, t:]
    I = np.identity(t)                              # identity matrix of size t
    N = np.linalg.inv((np.subtract(I, Q)))          # fundamental matrix
    P = np.dot(N, R)                                # limiting matrix

    solutions = [frac(x).limit_denominator() for x in P[0]]
    print(solutions)

    lcm = np.lcm.reduce([f.denominator for f in solutions])
    res = [int(f.numerator * lcm / f.denominator) for f in solutions]
    res.append(lcm)

    return res
