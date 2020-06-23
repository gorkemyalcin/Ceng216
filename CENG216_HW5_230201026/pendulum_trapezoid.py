#Ben-Malik Tchamalam 240201110 & Ali Gorkem Yalcin 230201026
import numpy as np
import math
from matplotlib import pyplot as plot

def pendulum_trapezoid(t0, t1, h):
    t = np.arange(t0, t1 + h/2, h)
    w_1 = np.empty_like(t)
    w_2 = np.empty_like(t)  
    w_1[0] = math.pi / 2
    w_2[0] = 0
    x = np.empty_like(t)
    y = np.empty_like(t)
    
    for i, _ in enumerate(t[:-1]):
        w_1[i + 1] = w_1[i] + h*(w_2[i] + w_2[i] - h*(9.81*math.sin(w_1[i]))) /2
        w_2[i + 1] = w_2[i] + h*(-9.81*math.sin(w_1[i]) - 9.81*(w_1[i] + h*w_2[i])) / 2
        x[i + 1] = math.sin(w_1[i])
        y[i + 1] = -math.cos(w_1[i])
        
    return w_1, w_2, x, y

y_1, y_2, x, y = pendulum_trapezoid(0, 10, 0.01)

plot.plot(y_2)
plot.show()
plot.plot(x,y)
plot.show()