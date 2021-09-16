import PIL.Image
import io

img = PIL.Image.open('./assets/TheWoman.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

# png injection
with open('./assets/TheMan.jpg', 'ab') as c:
  c.write(byte_arr.getvalue())
