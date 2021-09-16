import PIL.Image
import io

img = PIL.Image.open('YourImage.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

# png injection
with open('OtherImage.jpg', 'ab') as c:
  c.write(byte_arr.getvalue())
