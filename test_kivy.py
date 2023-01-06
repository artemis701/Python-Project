import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import filedialog as fd

# x1 = [0.0, 2.0, 5.0, -1.5, 4.5, 0.0]
# y1 = [0.0, 5.5, 2.0, 1.5, 3.0, 0.0]
x = []
y = []

filename = fd.askopenfilename()

with open('lineString.txt') as file:
    while (line := file.readline().rstrip()):
        x.append(float(line.replace(" ","").split(',')[0]))
        y.append(float(line.replace(" ","").split(',')[1]))
        
plt.xlim(-2, 7), plt.ylim(-1.0, 7)
plt.plot(x, y, label = "line 1")

plt.legend()
plt.show()