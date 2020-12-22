from PIL import Image,ImageDraw,ImageFont
image= Image.open("ImagesArchive/Data.jpeg")
print(image.filename)
print(image.format)
print(image.size)
print(image.width)
print(image.height)
print(image.mode)
print('----'*10)
infile = "ImagesArchive/BrainHand.jpeg"
with Image.open(infile) as img:
    draw= ImageDraw.Draw(img)
    textstr='This is something good'
    txtfont=ImageFont.truetype("TTF.ttf",size=150)
    txtsize=draw.textsize(textstr, font=txtfont)
    location=(20,img.height-txtsize[1])
    draw.text(location,textstr,(255,255,255),font=txtfont)
    savefile="ImagesArchive/BrainHand_text.jpeg"
    img.save(savefile,'JPEG')
