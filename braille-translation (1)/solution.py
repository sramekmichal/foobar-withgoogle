import string

# Braille space character
braille_space = '000000'
# Braille capital mark
braille_capital = '000001'
# Braille alphabet letters
braille_letters = [
    '100000', # a
    '110000', # b
    '100100', # c
    '100110', # d
    '100010', # e
    '110100', # f
    '110110', # g
    '110010', # h
    '010100', # i
    '010110', # j
    '101000', # k
    '111000', # l
    '101100', # m
    '101110', # n
    '101010', # o
    '111100', # p
    '111110', # q
    '111010', # r
    '011100', # s
    '011110', # t
    '101001', # u
    '111001', # v
    '010111', # w
    '101101', # x
    '101111', # y
    '101011', # z
]

# A single list of alphabet letters, capital marks and space characters
braille_list = braille_letters + [braille_capital + s for s in braille_letters] + [braille_space]
# A single ascii list of lowercase, uppercase and space characters
ascii_list = list(string.ascii_lowercase + string.ascii_uppercase + " ")

# Translastion table
translation_table = dict(zip(ascii_list, braille_list))

def solution(plaintext):
    characters = list(plaintext)
    braille = [translation_table[v] for v in characters if v in characters]
    return ''.join(braille)
