#
#A program to correct the spelling of a text
#By Daniel Graham
#


def make_dict():
    fin = open('spellingWords.txt', 'r')
    correct_dictionary = {}
    for line in fin:
        line_list = line.split()
        correct_dictionary[line_list[0]] = line_list[1]
    return correct_dictionary




def check_word(word, dictionary):
    
    corrected_word = dictionary.get(word, word)

    return corrected_word



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
    
    
