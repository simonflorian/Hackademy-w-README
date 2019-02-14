from PIL import Image

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    an_image.show()
    return an_image


im = Image.open("C:\\Users\\simonf\\Desktop\\Hackademy\\Images\\Wifi.jpg")
print(im.size)
print(im.format)

im = rotate_box(im)

im2 = Image.open("C:\\Users\\simonf\\Desktop\\Hackademy\\Images\\Wifi.jpg")
im2 = rotate_box(im2)
im2.show()












#box = (100,100,400,400)
#region = im.crop(box)
#transposed = region.transpose(Image.ROTATE_180)
#im.paste(transposed,box)
#im.show()


#im2 = Image.open("C:\\Users\\simonf\\Desktop\\Hackademy\\Images\\Hacked.png")
#box = (100,100,400,400)
#region = im.crop(box)
#transposed = region.transpose(Image.ROTATE_180)
#im.paste(transposed,box)
#im.show()