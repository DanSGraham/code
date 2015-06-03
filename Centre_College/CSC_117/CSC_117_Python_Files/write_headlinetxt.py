#A program to write a headline text document


def headline_text_writer(header, company, headline1):
    """This is like the stock text document writer"""

    
    filename = company + 'Headlines.txt'
    try:
        fin = open('data/' + filename, 'r')
        
        if not header in fin.read():
            header_write = True
        else:
            header_write = False
        fin.close()
    except:
        header_write = True
    
    fout = open('data/' + filename, 'a')
    if header_write:
        fout.write(header)  
    string_to_write = headline1.getHeadline() + ' @ ' + str(headline1.getTime()) + '\n'
    fout.write(string_to_write)
    fout.close()
    
