#
#Dictionary testing
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


