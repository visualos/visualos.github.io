# Comprehensive dictionary including English letters, digits, and common punctuation.
# Note: ' ' (space) is mapped to '/' (slash) for easy word separation in the encoded output.
MORSE_CODE_FULL = {
    # Letters (English Alphabet)
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    # Digits
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    # Space and Punctuation
    ' ': '/',        # Used as a conventional word separator in Morse output
    '.': '.-.-.-',   # Period
    ',': '--..--',   # Comma
    '?': '..-..',    # Question Mark
    '/': '-..-.'     # Slash/Virgule
}