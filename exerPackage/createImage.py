from PIL import Image

class ImageInfo:
    def __init__(self,imageSize,imageFormat,imageColor,fileName):
        self.imageSize = imageSize
        self.imageFormat = imageFormat
        self.imageColor = imageColor
        self.fileName = fileName

    def create_image(self):
        img = Image.new('RGB',self.imageSize,self.imageColor)
        img.save(self.fileName,self.imageFormat)


M3 = (9999, 6666)
COLOR = (255, 255, 255)
FORMAT = "PNG"
file = "4M.PNG"
a = ImageInfo(M3,FORMAT,COLOR,file)
print(a.imageSize)
a.create_image()