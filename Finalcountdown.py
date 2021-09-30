import time 

number = 1000

while number > -1:
  print(number)
  number = number - 1
  time.sleep(0.01)

from PIL import Image
  
try: 
    img  = Image.open(path) 
except IOError:
    pass
filename = "explosion.jpg"
with Image.open(filename) as image:
    width, height = image.size




  


  