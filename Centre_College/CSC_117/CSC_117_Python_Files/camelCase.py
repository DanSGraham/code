#
#A program to convert to camelCase
#Author: Daniel Graham
#

import string
changeWord=raw_input("Please insert a phrase seperated by _ instead of spaces. ")

n=changeWord.count( "_")
splitWords=changeWord.split("_")

firstWord=splitWords[0].lower()

accum=""
for j in range (1,n+1):
    restOfWords=splitWords[j].title()
    accum=accum+restOfWords


totalWord=firstWord+accum

print totalWord
