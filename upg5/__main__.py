from os import path
import math
import glob
from PIL import Image
import matplotlib.pyplot as plt
import konstanter as k
import funktionsaddition as f

xlist = []
ylist = []
Ylist = []
Xlist = []
Alist = []
Blist = []

L = k.L
m = k.m
x = k.x0
dx = k.dx
t = k.t0
B = k.B0
u0 = k.u0

if (k.condition == 'n'):
    f.make_gif(k.outpath)
else:
    while (x<=L):
        B += dx *f.h(x, 0)*2/L
        x += dx
    u0 = str(B/2)

    for n in range(m-1):
        x = k.x0
        A = k.A0
        B = k.B0
        while (x<=L):
            A += dx *f.g(x, n+1)*2/L
            B += dx *f.h(x, n+1)*2/L
            x += dx
        u0 += '+(' +str(A) +'*math.sin(2*'+str(n+1) +'*math.pi*x/L)' +'+' +str(B) +'*math.cos(2*'+str(n+1) +'*math.pi*x/L)) *math.cos(math.pi/L *' +str(n+1) +' *t)'

    x = k.x0
    while (x<=L):
        xlist.append(x)
        ylist.append(f.f(x))
        x += dx

    count = k.count
    while (t <= k.tMax):
        print('[' ,count, '/', k.antalbilder, ']')
        x = k.x0        
        while (x<=L):
            F = lambda x, t: eval(u0)
            Xlist.append(x)
            Ylist.append(F(x,t))
            x += dx

        plt.cla()
        plt.plot(xlist, ylist, c = 'grey', linestyle = 'dashed', linewidth = 0.5)
        plt.plot(Xlist, Ylist, c = 'tomato', linewidth = 1)
        plt.scatter(4, 3, c = 'white')

        plt.savefig(path.join(k.outpath, k.branding(count)))
        plt.close()
        
        Xlist.clear()
        Ylist.clear()

        t += k.dt
        count += 1

    f.make_gif(k.outpath)
