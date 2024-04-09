import winsound
import time

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', '?': '..--..',
    '!': '---.', ',': '--..--', '-': '-....-', '_': '..--.-',
}


def to_morse(word):
    encrypted = ''
    for letter in word:
        if letter != ' ':
            encrypted += MORSE_DICT[letter] + ' '
        else:
            encrypted += '  '
    return encrypted


def to_word(morse_list):
    decipher = ""
    morse_keys = list(MORSE_DICT.keys())
    morse_values = list(MORSE_DICT.values())

    for code in morse_list:
        if code in morse_values:
            decipher += morse_keys[morse_values.index(code)]

    return decipher


def morse_sound(word):
    for x in word:
        if x == ' ':
            time.sleep(1.3)
        elif x == '.':
            winsound.Beep(1000, 100)
        elif x == '-':
            winsound.Beep(1000, 600)


choice = input("Do you want to change to encrypt or decrypt morse code? type Encrypt or Decrypt: ").upper()
if choice == "ENCRYPT":
    phrase = input("What word or phrase do you want to convert to morse code? ").upper()
    morse = to_morse(phrase)
    print(morse)
    morse_sound(morse)
elif choice == "DECRYPT":
    morse_input = input("What is the code to decipher? ").upper()
    morse_split = morse_input.split()
    print(to_word(morse_split))
