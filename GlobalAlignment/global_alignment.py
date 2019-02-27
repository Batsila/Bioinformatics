import numpy as np
d = 1

def init_matrix(x, y):
    f = np.zeros((len(x) + 1, len(y) + 1), int)
    for i in range(len(x) + 1):
        f[i][0] = -i * d
    for i in range(len(y) + 1):
        f[0][i] = -i * d
    return f

def g(x, y):
    if x == y:
        return d
    else:
        return -d

def global_alignment(x, y):
    f = init_matrix(x, y)
    p = np.zeros((len(x), len(y)), str)
    for i in range(1, len(x) + 1, 1):
        for j in range(1, len(y) + 1, 1):
            match = f[i - 1][j - 1] + g(x[i - 1], y[i - 1])
            delete = f[i - 1][j] - d
            insert = f[i][j - 1] - d
            max_v = max(match, insert, delete)
            if max_v == delete:
                p[i - 1][j - 1] = "d"
            elif max_v == insert:
                p[i - 1][j - 1] = "i"
            else:
                p[i - 1][j - 1] = "m"
            f[i][j] = max_v
    return (f[-1][-1], p)

def restore(p):
    i = len(p[:,1]) - 1
    j = len(p[1,:]) - 1
    way = ""
    while i > 0 and j > 0:
        way += p[i][j]
        if p[i][j] == "m":
            i -= 1
            j -= 1
        elif p[i][j] == "d":
            j -= 1
        elif p[i][j] == "i":
            i -= 1
    return way[::-1]

x = "ACGTGATGCTAGCAT"
y = "ACGTGATGCTAGCAT"
score, p = global_alignment(x, y)
way = restore(p)
print("Score: " + str(score))
print("Way: " + way)
