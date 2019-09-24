#### 1920_3 霍英涛
#### 本文件在python 3.6.7中编译通过
#### 需安装numpy，opencv，matplotlib库
#### 所有结果图均在spyder编译器中截图所得


import numpy as np 
import sys
from BmpRGB import ReadBMPFile
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import pylab

#filePath = sys.argv[1]
parser = argparse.ArgumentParser()
parser.parse_args()



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
    cv2.imwrite("ColorCh.bmp",merged)



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

    #print(gray)
    #cv2.imshow('gray',gray)
    cv2.imwrite("grayCh.bmp",gray)
    
def OneColorGradient():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.cm.get_cmap('Blues')
    norm = mpl.colors.Normalize(vmin=0, vmax= 10)
    
    cb1 = mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,orientation='horizontal')
    cb1.set_label('OneColor Gradient')
    fig.show
    #cv2.imwrite("OneColorGra.bmp",cmap)

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
    bmpFile = ReadBMPFile(filePath) #解析BMP文件
    ColorToGray(bmpFile)            #将原始彩色图转化为灰度图，并将灰度值映射到64-127之间
    ColorScale()                    #生成包含七种颜色的渐变彩色图
    GrayScale()                     #生成有白到黑的渐变色图
    OneColorGradient()              #生成由白到蓝的色彩渐变图