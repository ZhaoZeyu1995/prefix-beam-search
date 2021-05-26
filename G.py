import numpy as np


def yyn(prefix: str):
    word_list = prefix.strip('>').strip().split(' ')
    # make sure that the spelling is correct
    for word in word_list:
        if word not in ['yes', 'no']:
            return 0
    if len(word_list) == 1:
        return 1
    elif len(word_list) == 2:
        if word_list == ['no', 'no']:
            return 0
        else:
            return 1
    else:
        gram3 = word_list[-3:]
        if gram3 in [['yes', 'yes', 'no'],
                     ['yes', 'no', 'yes'],
                     ['no', 'yes', 'yes']]:
            return 1
        else:
            return 0
def ynn(prefix: str):
    word_list = prefix.strip('>').strip().split(' ')
    # make sure that the spelling is correct
    for word in word_list:
        if word not in ['yes', 'no']:
            return 0
    if len(word_list) == 1:
        return 1
    elif len(word_list) == 2:
        if word_list == ['yes', 'yes']:
            return 0
        else:
            return 1
    else:
        gram3 = word_list[-3:]
        if gram3 in [['yes', 'no', 'no'],
                     ['no', 'no', 'yes'],
                     ['no', 'yes', 'no']]:
            return 1
        else:
            return 0

if __name__ == '__main__':
    print(yyn('yes no no '))
    print(yyn('yes yes no yes yes no'))
