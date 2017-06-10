from PIL import Image
img = Image.open('/Users/wangrenjie/Documents/photo/photo.jpeg')
w, h = img.size
img.thumbnail((w//2,h/2))
img.save('/Users/wangrenjie/Documents/photo/thumbphoto.jpeg','jpeg')
