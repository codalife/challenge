def answer(plaintext):
    # your code here
    pangram = "the quick brown fox jumped over the lazy dog"

    braille = {}

    braille['capital'] = '000001'

    pangramBraille = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"

    for i in range(len(pangram)):
        braille.setdefault(pangram[i], pangramBraille[i*6: i*6 + 6])

    res = ''
    for j in plaintext:
        char = j
        if char.isupper():
            res = res + braille.get('capital')
            char = char.lower()
        res = res + braille.get(char)

    return(res)

print(answer('The quick brown fox jumped over the lazy dog'))
