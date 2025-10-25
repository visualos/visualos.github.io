from m_code import MORSE_CODE_FULL

def to_morse(word):
    print(f'Transcribing {word}...')
    morse_code = ''
    for letter in word:
        char = letter.upper()
        if char in MORSE_CODE_FULL:
            morse_code +=  MORSE_CODE_FULL[char] + ' '
        else:
            morse_code += '# '
    return morse_code


user_input = (input('enter a word:'))
final_morse = to_morse(user_input)


print('Your morse code is:', final_morse, f'({user_input})')
