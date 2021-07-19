from pytesser import *

im = Image.open('cpatcha.png')
text = image_to_string(im)
print(text)