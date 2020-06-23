import numpy as np

def fixed_point_iter(f, x0, k):
    x = [x0]
    for i in range(k):
        x.append(f(x[-1]))
    return x[-1], x

_, x = fixed_point_iter(lambda x: (np.sin(x) - 5)/6, -10, 10)
print(np.reshape(np.float64(x), (11, -1)))