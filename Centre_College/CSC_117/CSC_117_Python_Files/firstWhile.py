#
#A program to accept user input until -1 is entered
#By Daniel Graham

def whileloop():
    num = 0
    evens = []
    odds = []
    while num != -1:
        num = input("Please enter a positive integer. (Enter -1 when done)")
        if num == -1:
            print "Even numbers: ",evens
            print "Odd numbers: " , odds
        elif num%2 == 1:
            odds.append(num)
        elif num%2 == 0 :
            evens.append(num)
if __name__ == "__main__":
    whileloop()
        
