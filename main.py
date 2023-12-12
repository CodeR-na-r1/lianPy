import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt
from lian import Lian
from point import Cell

image = cv.imread('map.png')
gr = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gr[gr > 200] = 255
gr[gr != 255] = 0

goal = Cell(1287, 689)
# goal = Cell(410, 420)
start = Cell(165, 305)

image = np.array(gr)

t = time.time()
lian, dist = Lian(image, start, goal, 13, 15)
print('----', time.time()-t, 'seconds ----')

print("Points", len(lian))

for i in range(len(lian)-1):
    image = cv.circle(image, lian[i].index(), 1, (50, 50, 50), -1)

plt.imshow(image)
plt.show()