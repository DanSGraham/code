from wave import *

test = open('test_music.wav','rb')

print test
print test.getnchannels()
test.rewind()
