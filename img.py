from PIL import Image
img = Image.open('/Users/wangrenjie/Documents/photo/photo.jpeg')
w, h = img.size
print("w:%d,h:%d",(w,h))
img.thumbnail((w//2,h/2))
#w, h = img.thumbnail.size
print 
img.save('/Users/wangrenjie/Documents/photo/thumbphoto.jpeg','jpeg')
#imgt = Image.open('/Users/wangrenjie/Documents/photo/thumbphoto.jpeg')
#w,h = imgt.size
#print w,h
#def add_num(img):
#   draw = ImageDraw.Draw(img)
#    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
 #   fillcolor = "#ff0000"
  #  width, height = img.size
   # draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    #img.save('result.jpg','jpeg')

#    return 0
#if __name__ == '__main__':
 #   image = Image.open('image.jpg')
  #  add_num(image)
   # */
