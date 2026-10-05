# Morse Code Decoder

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9', '/': ' '
}

def decode(morse_code):
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

print("=== MORSE DECODER ===")
print("নিয়ম: . = dot, - = dash, Space = letter, / = word")
while True:
    code = input("\nMorse code likho: ")
    if code == 'exit':
        break
    print("Decoded:", decode(code))