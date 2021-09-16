# text injection
with open('OtherFile.jpg', 'ab') as a: # put your image in 'assets' and change the path
  a.write(b"YourString") # your text inside of string
