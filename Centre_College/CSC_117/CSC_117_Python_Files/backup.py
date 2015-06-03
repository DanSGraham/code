fout = open('backup.txt', 'w')
fin = open('jabberwocky.txt', 'r')
for line in fin:
    fout.write(line)
fout.close()
fin.close()
