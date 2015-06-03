#A reading note companion
#By Daniel Graham


#This program is to be kept open when reading. If any thought or notion should come to you\
#Enter it into this program and it will store it in a text document.

import datetime

def read_companion():
    header = '%02d/%02d/%02d\n' % (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
    book = raw_input("What book are you reading?")
    file_name = book + "_notes.txt"
    fout = open(file_name, 'a')
    fout.write(header + "\n")
    while True:
        to_append = raw_input("Any thoughts? (x to close)")
        if to_append == 'x':
            break
        fout.write(to_append + '\n\n')
    fout.close()
read_companion()
