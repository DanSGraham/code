#Misc. functions
#By Daniel Graham


def squareCopy(list_nums):
    list1 = []
    for num in list_nums:
        num **=2
        list1.append(num)
    return list1

def squareIt(list_nums = None):
    for i in range(len(list_nums)):
        list_nums[i] **=2
    if list_nums != None:
        return list_nums
    else:
        return None

def minList(list_nums):
    if list_nums == []:
        print "ERROR: Empty list"
    else:
        lowestnum = list_nums[0]
        for i in range(len(list_nums)):
            if lowestnum > list_nums[i]:
                lowestnum = list_nums[i]
    return lowestnum
def span(list_nums):
    if list_nums == []:
        print "ERROR: Empty list"
    else:
        lowestnum = list_nums[0]
        for i in range(len(list_nums)):
            if lowestnum > list_nums[i]:
                lowestnum = list_nums[i]
        highestnum = list_nums[0]
        for i in range(len(list_nums)):
            if highestnum < list_nums[i]:
                highestnum = list_nums[i]
    return highestnum - lowestnum
    
def counter(list_nums):
    neg_num = 0
    pos_num = 0
    zero = 0
    for i in range(len(list_nums)):
            if list_nums[i] < 0 :
                neg_num += 1
            if list_nums[i] == 0:
                zero += 1
            if list_nums[i] > 0:
                pos_num += 1
    return pos_num,zero,neg_num

        
        
