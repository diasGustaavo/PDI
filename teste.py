import numpy as np
import pandas as pd
import cv2 as cv
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
import os
import pathlib
import time 

dirAtual = str(pathlib.Path().absolute())

def convertToYIQUpdate(rgbImage):
    rgbImage = rgbImage.astype(float)
    for i in range(len(rgbImage)):
        for j in range(len(rgbImage[0])):
            #print(rgbImage[i][j])
            Y = (0.299*rgbImage[i][j][0]) + (0.5876*rgbImage[i][j][1]) + (0.114*rgbImage[i][j][2])
            I = (0.596*rgbImage[i][j][0]) - (0.2746*rgbImage[i][j][1]) - (0.322*rgbImage[i][j][2])
            Q = (0.211*rgbImage[i][j][0]) - (0.5236*rgbImage[i][j][1]) + (0.312*rgbImage[i][j][2])
            rgbImage[i][j] = [Y, I, Q, 255]
            #print(rgbImage[i][j])
            #print("cut")
    return(rgbImage)

def convertToRGBUpdate(rgbImage):
    for i in range(len(rgbImage)):
        for j in range(len(rgbImage[0])):
            #print(rgbImage[i][j])
            R = (rgbImage[i][j][0]) + (0.956*rgbImage[i][j][1]) + (0.621*rgbImage[i][j][2])
            G = (rgbImage[i][j][0]) - (0.272*rgbImage[i][j][1]) - (0.647*rgbImage[i][j][2])
            B = (rgbImage[i][j][0]) - (1.106*rgbImage[i][j][1]) + (1.703*rgbImage[i][j][2])
            rgbImage[i][j] = [round(R), round(G), round(B), 255]
            #print(rgbImage[i][j])
            #print("cut")
    rgbImage = rgbImage.astype(int)
    return(rgbImage)

image = io.imread(dirAtual + '/Imagens/Woman.png')
# plt.imshow(image)
# plt.show()

print(image)
print(f'-----------EM YIQ----------\n')
atualizadaYIQ = convertToYIQUpdate(image)
print(atualizadaYIQ)

print(f'-----------EM RGB----------\n')
atualizadaRGB = convertToRGBUpdate(atualizadaYIQ)
print(atualizadaRGB)

image2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# plt.imshow(image2)
# plt.show()
# image2