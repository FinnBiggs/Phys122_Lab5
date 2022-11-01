import os
import numpy as np

offsets = np.linspace(0.1, 100, 8)
angles = np.linspace(0.001, 0.24, 500)
eccies = np.linspace(0.0, 1.0, 20)

with open("data12.txt", "w") as f:
    f.write("")

num = "1"
idx = "1.0"
surf = "1.5 0 150 "

os.system("python raytracing/par_2d.py")
with open("data.txt", 'r') as f:
    for line in f.readlines():
        #print(line)
        if "Rays intersect at" in line:
            data.append("{}".format(line))