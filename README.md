# Morse-Decoder-
Use for fun &amp; Educational only.
# MORSE BY ONBIR
# -- --- .-. ... . / -... -.-- / --- -. -... .. .-.

MORSE_CODE = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
    '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L',
    '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R',
    '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
    '-.--':'Y', '--..':'Z', '...---...':'SOS', '/':' '
}

BANNER = """
__  __  ___  ____   _____ ____  ____  
|  \/  |/ _ \|  _ \ |  __|_   _|  _ \|  _ \ 
| |\/| | | | | |_) || |_   | | | |_) | |_) |
| |  |_| |  _ < |  _|  | |  __/|  _ < 
|_|  |_|\___/|_| \_\|_|    |_| |_|   |_| \_\
     MORSE BY ONBIR
     -- --- .-. ... . / -... -.-- / --- -. -... .. .-.
"""

def encode(text):
    text = text.upper()
    rev_dict = {v:k for k,v in MORSE_CODE.items()}
    return ' '.join(rev_dict.get(char, '') for char in text)

def decode(morse):
    words = morse.split(' / ')
    result = []
    for word in words:
        letters = word.split()
        result.append(''.join(MORSE_CODE.get(l, '?') for l in letters))
    return ' '.join(result)

print(BANNER)
print("Welcome to Morse Decoder")
print("="*40)

while True:
    choice = input("\n1. Encode 2. Decode 3. Exit\nChoose: ")
    
    if choice == '1':
        txt = input("Enter Text: ")
        print("Morse:", encode(txt))
    elif choice == '2':
        code = input("Enter Morse: ")
        print("Text:", decode(code))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
