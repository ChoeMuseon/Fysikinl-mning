import math

x0 = 0
dx = 1/1000
L = math.pi
    # för konvergens
ddx = 9/10
xMax = 600

m = 100
w = 1

antalbilder = 200
t0 = 0
tMax = 2*math.pi
dt = tMax/antalbilder

A0 = 0
B0 = 0

Yfunk0 = ''
Xfunk0 = ''
u0 = ''

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p" ,"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
id = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for h in range(len(letters)):
            id.append(numbers[i] +numbers[j] +letters[h])

count = 0
def branding(count):
    return 'Heart%r.PNG' %(id[count])
outpath = 'C:/python/fysikinlamning/upg5/pictures/'

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p" ,"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

