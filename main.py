import numpy as np 
import sys
from BmpRGB import ReadBMPFile
import cv2
import matplotlib.pyplot as plt

#filePath = sys.argv[1]

filePath = 'a.bmp'
def SaveColor(bmpFile):
    R = bmpFile.R
    G = bmpFile.G
    B = bmpFile.B

    b = np.array(B, dtype=np.uint8)
    g = np.array(G, dtype=np.uint8)
    r = np.array(R, dtype=np.uint8)

    merged = cv2.merge([b,g,r])
    cv2.imshow("Merged:",merged)
    cv2.imwrite("b.bmp",merged)



def ColorToGray(bmpFile):
    R = bmpFile.R
    G = bmpFile.G
    B = bmpFile.B

    b = np.array(B, dtype=np.uint8)
    g = np.array(G, dtype=np.uint8)
    r = np.array(R, dtype=np.uint8)

    merged = cv2.merge([b,g,r])
    gray = np.dot(merged,(0.2989,0.5870,0.114))
    max = np.max(gray)
    min = np.min(gray)
    for i in range(bmpFile.Height):
        for j in range(bmpFile.Width):
            gray[i][j] = (127.0 - 64.0 + 1.0)/(max - min)*(gray[i][j] - min) + 64.0

    print(gray)
    cv2.imwrite("grayCh.bmp",gray)

def ColorScale():
    fig = plt.figure()
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,1,1,1,1,1,1,1,1,1])
    plt.scatter(x,y,c=y)
    plt.colorbar()

#def GrayScale():


if __name__ == "__main__":
    bmpFile = ReadBMPFile(filePath)
    #ColorToGray(bmpFile)
    ColorScale()
