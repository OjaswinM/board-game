import numpy as np
import cv2
import matplotlib.pyplot as plt
def makeMaze(filename):
    img = cv2.imread(filename)
    img = cv2.blur(img, (2, 2))
    maze = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j][0] != 0 and img[i, j][2] != 0 and img[i, j][1] != 0:
                maze[i, j] = -1
    return maze

maze = makeMaze('1.jpg')

plt.imshow(maze)
plt.show()
