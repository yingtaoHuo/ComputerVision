import numpy as np 
import sys
from BmpRGB import ReadBMPFile
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse

#filePath = sys.argv[1]
parser = argparse.AugumentParser

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
    
def OneColorGradient():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.cm.get_cmap('Blues')
    norm = mpl.colors.Normalize(vmin=0, vmax= 10)
    
    cb1 = mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,orientation='horizontal')
    cb1.set_label('OneColor Gradient')
    fig.show

def ColorScale():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.Normalize(vmin=0, vmax= 10)
    
    cb1 = mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,orientation='horizontal')
    cb1.set_label('Color Gradient')
    fig.show

def GrayScale():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    #cmap = mpl.cm.jet
    #print(mpl.cm.jet)
    cmap = mpl.cm.get_cmap('gray_r')
    #cmap = mpl.colors.ListedColormap(['white','gray'])
    norm = mpl.colors.Normalize(vmin=0, vmax= 10)
    
    cb1 = mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,orientation='horizontal')
    cb1.set_label('Gray Gradient')
    fig.show
    



if __name__ == "__main__":
    bmpFile = ReadBMPFile(filePath)
    #ColorToGray(bmpFile)
    #ColorScale()
    GrayScale()
    ColorScale()
    OneColorGradient()