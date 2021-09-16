# text injection
with open('./assets/TheMan.jpg', 'ab') as a: # put your image in 'assets' and change the path
  a.write(b" ---- ") # your text inside of string