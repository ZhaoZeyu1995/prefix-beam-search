import os

def read_alphabet(file):
    alphabet = ['%']
    with open(file) as f:
        for line in f:
            lc = line.strip().split()
            if lc[0] == '<space>':
                token = ' '
            elif lc[0] == '<unk>':
                token = '*'
            else:
                token = lc[0]
            alphabet.append(token)
    alphabet.append('>')
    return alphabet
