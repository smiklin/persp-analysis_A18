import numpy

def get_r(K, L, alpha, Z, delta):
    r = alpha*Z*(L/K)**(1-alpha)-delta
    return r
