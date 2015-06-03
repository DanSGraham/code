#A program to write stock data to a text document
#By Daniel Graham


def stock_writer(header, stock_list):

    """A function to write stocks to a text document"""
    
    for stock1 in stock_list:
        filename = stock1.getCompany() + 'StockSalePrices.txt'
        try:
            fin = open('data/' + filename, 'r')
            
            if not header in fin.read():
                header_write = True
            else:
                header_write = False
            fin.close()
        #Tests if a file exists already or not. Need to know if header must be written. If beginning of the file, a header is written to the file.
        except:
            header_write = True
        
        fout = open('data/' + filename, 'a')
        if header_write:
            fout.write(header)
        string_to_write = stock1.getPrice() + ' @ ' + stock1.getTime() + '\n'
        fout.write(string_to_write)
        fout.close()
