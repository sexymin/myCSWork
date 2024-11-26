'''
LSCP wants to make a name-calculator which finds vowel(s) in the word and returns 
the sum calculated by using the data set, {'a': 66, 'e': 72, 'i': 89, 'o': 73, 'u': 19}.
'''

vowels = {'a': 66, 'e': 72, 'i': 89, 'o': 73, 'u': 19}
names = ["daeju", "seoyoung", "taeyoon", "hwanmin", "beomkyu", "sieon"]


def str2num(word:str) -> int:
    '''
    return the sum of the values for the vowels corresponding to the data set.
    For instance, 'daeju' has three vowels and its sum is 157. 
    '''
    for each in str:
        if each in vowels:
            print(each, vowels[each])


def findBiggest(temp:list) -> str:
    '''
    return the word which has the biggest value in the list, vowels.
    '''
    total = 0
    for each in temp:
        if each in vowels:
            total = total + vowels[each]
    
    return total

findBiggest(names)

def findSmallest(temp:list) -> str:
    '''
    reutrn the word which has the smallest value in the list, vowels.
    '''
    target = ""
    save = 9999999999
    for each in temp:
        if save > str2num(each):
            target = each
            save = str2num(each)
    return target
    