import numpy as np
import cv2
import matplotlib.pyplot as plt

def makeMaze(filename):
    img = cv2.imread(filename)
    maze = np.ones((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j][0] < 100:
                maze[i, j] = 0
    return maze

maze = makeMaze('2.jpg')


plt.imshow(maze)
plt.show()

np.savez_compressed('Maze1.npz', R = maze)
