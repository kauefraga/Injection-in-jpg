# text founder
with open('./assets/TheMan.jpg', 'rb') as b:
  content = b.read()
  offset = content.index(bytes.fromhex('FFD9'))

  b.seek(offset + 2)
  print(b.read())