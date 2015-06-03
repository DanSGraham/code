#
#String Functions
#Daniel Graham


def reverse(string):
    string_list = string.split()
    string = ''
    for i in string_list[::-1]:
        if i == string_list[0]:
            string = string + i
        else:
            string = string + i + ", "
    print string

def wordcount(string):
    string_list1 = string.split()
    print len(string_list1)
    
def merge(string_list1, string_list2):

    
    merged_list = []
    if len(string_list1) < len(string_list2):
        string_list1,string_list2=string_list2, string_list1
    j = 0
    k = 0
    for i in string_list1:
        if i < string_list2[j]:
            merged_list.append(i)
            k += 1
        elif string_list2[j] < string_list1[k]:
            merged_list.append(string_list2[j])
            if i == string_list1[-1]:
                merged_list.append(string_list2[j:-1])
            j += 1
    print merged_list
        


