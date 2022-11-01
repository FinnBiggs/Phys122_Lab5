import os
import numpy as np

offsets = np.linspace(0.1, 100, 8)
angles = np.linspace(0.001, 0.24, 500)
eccies = np.linspace(0.0, 1.0, 20)

with open("data.txt", "w") as f:
    f.write("")

num = "1"
idx = "1.0"
surf = "1.5 0 150 "

for ecc in eccies:
    s = surf + str(ecc) 
    with open("lens_10", "w") as f:
        f.write(num + '\n')
        f.write(idx + '\n')
        f.write(s)

    for  offset in offsets:
            os.system("python raytracing/par_2d.py lens_10 -150 0 0 {} >> data.txt".format(offset))
    
    with open("data.txt", "a") as d:
        d.write("\n")

data = []

with open("data.txt", 'r') as f:
    for line in f.readlines():
        #print(line)
        if "Rays intersect at" in line:
            data.append("{}".format(line))


hdr = "offset,angle,displacement"
print(hdr)
for i, ecc in enumerate(eccies):
    for j, offset in enumerate(offsets):
        sstr = data[i * len(offsets) + j].split(" ")
        print("{}, {}, {}".format(offset, ecc, sstr[5][1:-1]) )