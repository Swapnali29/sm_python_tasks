# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".


# 1) An example of using the compress method on a simple string


import gzip

s = b'Music industry hails passage of the Music Modernization Act'
s = gzip.compress(s)
#print(s)

# using gzip.decompress(s) method
t = gzip.decompress(s)
print(t)