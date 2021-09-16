import PIL.Image
import io

img = PIL.Image.open('YourImage.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

# png founder
with open('OtherImage.jpg', 'rb') as d:
  jpg = d.read()
  jpg_offset = jpg.index(bytes.fromhex('FFD9'))

  d.seek(jpg_offset + 2)

  new_img = PIL.Image.open(io.BytesIO(d.read()))
  new_img.save("new_image.png")
