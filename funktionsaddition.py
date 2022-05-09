import math
import konstanter as k
import glob
import os as path
from PIL import Image

L = k.L

def f(x):
    return -(math.sqrt(abs(math.cos(x-math.pi/2)))*math.cos(100*(x-math.pi/2))  -3 -math.sqrt(abs(x-math.pi/2))) 
def g(x,n):
    return f(x)*math.sin(2*n*math.pi*x/L)
def h(x,n):
    return f(x)*math.cos(2*n*math.pi*x/L)



def make_gif(dirr):
    frames = [Image.open(file) for file in glob.glob("%s*.PNG" %(dirr))]
    frame_one = frames[0]
    frames.pop(0)
    frame_one.save("Hjärt.gif", format="GIF", append_images=frames, 
                save_all=True, duration=100, loop=0)
