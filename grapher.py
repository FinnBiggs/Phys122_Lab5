import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("real_data.txt")

ax = plt.axes(projection = "3d")
fig = ax.get_figure()

ax.scatter3D(df["offset"], df["angle"], df["displacement"] )
# fig.savefig("y_img.png", format="png")
plt.show()