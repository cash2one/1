from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img=Image.new("RGBA", (500,250),(255,255,255))
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", 16)
font = ImageFont.load_default().font
#draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')
