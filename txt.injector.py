# text injection
with open('OtherImage.jpg', 'ab') as a: # put your image in 'assets' and change the path
  a.write(b"YourString") # your text inside of string
