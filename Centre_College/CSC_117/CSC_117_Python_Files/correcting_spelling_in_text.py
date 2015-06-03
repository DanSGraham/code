#
#A program to correct the spelling of a text
#By Daniel Graham
#
from dictionarylab import*

def correct(list_of_string, dictionary):
    list_of_words = ''
    for item in list_of_string:
        correct_word = check_word(item,dictionary)
        list_of_words += (" " +correct_word)
    return list_of_words

def main():
    fin = open('paragraph.txt', 'r')
    text = fin.read()
    print text
    list_of_words = text.split()
    print correct(list_of_words, make_dict())

    
main()
    
    
