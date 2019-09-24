####19210_3 霍英涛
####本文件用于解析BMP文件
####通过unpack解析二进制文件，保存bmp文件的各类信息


from struct import unpack

class ReadBMPFile:
    def __init__(self, filePath):
        file = open(filePath,'rb')
        ### bmp头文件
        self.Type = unpack('<h',file.read(2))[0]
        self.Size = unpack('<i',file.read(4))[0]
        self.Reserved1 = unpack('<h',file.read(2))[0]
        self.Reserved2 = unpack('<h',file.read(2))[0]
        self.Offbits = unpack('<i',file.read(4))[0]

        ### 位图信息头
        self.Size = unpack('<i',file.read(4))[0]
        self.Width = unpack('<i',file.read(4))[0]
        self.Height = unpack('<i',file.read(4))[0]
        self.Planes = unpack('<h',file.read(2))[0]
        self.BitCount = unpack('<h',file.read(2))[0]
        self.Compree = unpack('<i',file.read(4))[0]
        self.ImageSize = unpack('<i',file.read(4))[0]
        self.XpelsPermeter = unpack('<i',file.read(4))[0]
        self.YpelsPermeter = unpack('<i',file.read(4))[0]
        self.ColoeIndex = unpack('<i',file.read(4))[0]
        self.ColorImp = unpack('<i',file.read(4))[0]
        
        ### 位图数据
        self.BmpData = []
        for height in range(self.Height):
            BmpDataRow = []
            count = 0
            for width in range(self.Width):
                BmpDataRow.append([unpack('<B',file.read(1))[0],unpack('<B',file.read(1))[0],unpack('<B',file.read(1))[0]])
                count = count + 3

            while count % 4 != 0:
                file.read(1)
                count = count + 1
            self.BmpData.append(BmpDataRow)
        self.BmpData.reverse()
        file.close()
        self.R = []
        self.G = []
        self.B = []

        for row in range(self.Height):
            R_row = []
            G_row = []
            B_row = []
            for col in range(self.Width):
                B_row.append(self.BmpData[row][col][0])
                G_row.append(self.BmpData[row][col][1])
                R_row.append(self.BmpData[row][col][2])
            self.B.append(B_row)
            self.G.append(G_row)
            self.R.append(R_row)

















