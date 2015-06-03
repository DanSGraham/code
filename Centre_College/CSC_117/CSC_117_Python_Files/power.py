#
#A program to practice functions
#By Daniel Graham


def power_of_two():
    for j in range(5):
        print 2**(j+1)

def power5(num_to_square):
    for j in range(5):
        print num_to_square**(j+1)
def power(num_square, num_to_square):
    for j in range(num_square):
        print num_to_square**(j+1)


num_to_square = input("What number would you like to raise to increasing powers? ")
num_Square123 = input("How many times would you like to raise it to a power? ")
power(num_Square123, num_to_square)
