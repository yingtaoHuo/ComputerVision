import numpy as np 
import sys
from BmpRGB import ReadBMPFile
import cv2

filePath = sys.argv[1]

bmpFile = ReadBMPFile(filePath)
R = bmpFile.R
G = bmpFile.G
B = bmpFile.B

b = np.array(B, dtype=np.uint8)
g = np.array(G, dtype=np.uint8)
r = np.array(R, dtype=np.uint8)

merged = cv2.merge([b,g,r])
cv2.imshow("Merged:",merged)
cv2.imwrite("a.bmp",merged)
