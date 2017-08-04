from PIL import Image

ice_cream = Image.open("ice_cream.jpg")
print ice_cream.getdata()[200]

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def getAverage(pixel):
    num = getRed(pixel)+getGreen(pixel)+getBlue(pixel)
    avg = num/3
    new_pixel = (avg, avg, avg)
    return new_pixel


new_pixels = []
size = ice_cream.width * ice_cream.height
old_pixels = ice_cream.getdata()
tops = []
bottoms = []
middles = []
lefts = []
rights = []

# flipping the thirds of the image
# for i in range(size):
#     old_pixel = old_pixels[i]
#     if (i < size / 3):
#         tops.append(old_pixel)
#     elif (i>size*2/3):
#         bottoms.append(old_pixel)
#     else:
#         middles.append(old_pixel)
# new_pixels=tops+middles+tops

# flipping the image (right side with left side)
# for i in range(size):
#     old_pixel = old_pixels[i]
#     if (i/(ice_cream.width/2)<1):
#         lefts.append(old_pixel)
#     else:
#         rights.append(old_pixel)
# new_pixels=rights+lefts

# making the top and bottom thirds grayscale
# for i in range(size):
#     old_pixel=old_pixels[i]
#     if (i<size/3):
#         new_pixels.append(getAverage(old_pixel))
#     elif (i>size*2/3):
#         new_pixels.append(getAverage(old_pixel))
#     else:
#         new_pixels.append(old_pixel)


#for pixel in ice_cream.getdata():
    #red_pixel = (255,0,0)
    #new_pixels.append(pixel)
    #red_value = getRed(pixel)
    #green_value = getGreen(pixel)
    #blue_value = getBlue(pixel)
    #new_pixel = (0,green_value,blue_value)
    #new_pixel = ((255-red_value),(255-green_value),(255-blue_value) )
    #new_pixel = (20+green_value,20+green_value,20+blue_value)
    #new_pixel = getAverage(pixel)
    #new_pixels.append(new_pixel)


#print new_pixels[200]

new_image = Image.new("RGB",ice_cream.size)
new_image.putdata(new_pixels)
new_image.show()
