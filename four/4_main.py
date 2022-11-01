import os
import numpy as np

angles = np.linspace(0.001, 0.24, 500)

with open("data.txt", "w") as f:
    f.write("")

for  angle in angles:
        os.system("python raytracing/point_2d.py lens_4 -150 0 0 {} 150 >> data.txt".format(angle))

data = []

with open("data.txt", 'r') as f:
    for line in f.readlines():
        #print(line)
        if "+y" in line:
            data.append("{}".format(line))

hdr = "ang,disp"
print(hdr)
for angle, line in zip(angles, data):
    sstr = line.split(" ")
    print("{}, {}".format(angle, sstr[6][:-2]) )