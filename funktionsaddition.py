import math
import konstanter as k
import glob
import os as path
from PIL import Image

L = k.L

def f(x):
    return x*(x-2)**2 *math.sin(x-L)
def g(x,n):
    return f(x)*math.sin(n*math.pi*x/L)

def make_gif(dirr):
    frames = [Image.open(file) for file in glob.glob("%s*.PNG" %(dirr))]
    frame_one = frames[0]
    frames.pop(0)
    frame_one.save(k.nameofgif, format="GIF", append_images=frames, 
                save_all=True, duration=k.frames, loop=0)
