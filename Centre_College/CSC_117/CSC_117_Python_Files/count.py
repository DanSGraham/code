fout = open('textedit.txt', 'w')
fin = open('jabberwocky.txt', 'r')
import string
lineCount=0
numba_characters=0
wordCount=0
for line in fin:
    fout.write(line)
    lineCount=lineCount +1
    wordCount= wordCount + len(line.split())
    numba_characters=numba_characters+len(line)
print "There are ",lineCount, "lines."
print "There are", wordCount, "words."
print "There are", numba_characters, "characters."

fout.close()
fin.close()
