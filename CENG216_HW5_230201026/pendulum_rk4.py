#Ben-Malik Tchamalam 240201110 & Ali Gorkem Yalcin 230201026
import math
import numpy as np
from matplotlib import pyplot as plot

def pendulum_rk4(t0, t1, h):
    t = np.arange(t0, t1 + h/2, h)
    w_1 = np.empty_like(t)
    w_2 = np.empty_like(t)
    w_1[0] = math.pi/2
    w_2[0] = 0

    x = np.empty_like(t)
    y = np.empty_like(t)
    x[0] = 1
    y[0] = 0
    for i, _ in enumerate(t[: -1]):
        s11 = w_2[i] 
        s21 = -9.81*math.sin(w_1[i])
       
        s12 = w_2[i] + h*s21/2
        s22 = -9.81*math.sin(w_1[i]+s11*h/2)

        s13 = w_2[i] +h* s22/2
        s23 = -9.81*math.sin(w_1[i]+h*s12/2)

        s14 = w_2[i] +h*s23
        s24 = -9.81*math.sin(w_1[i]+h*s13)
       
        w_1[i + 1] = (w_1[i] + h *(s11 + 2 * s12 + 2 * s13 + s14)/6)
        w_2[i + 1] = (w_2[i] + h * (s21 + 2 * s22 + 2 * s23 + s24)/6)
        x[i+1] = math.sin(w_1[i])
        y[i+1] = -math.cos(w_1[i])
    return w_1, w_2, x, y

y_1, y_2, x, y = pendulum_rk4(0, 10, 0.01)
plot.plot(y_2)
plot.show()
plot.plot(x,y)
plot.show()