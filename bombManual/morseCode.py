# Python program to implement Morse Code Translator
 

from dataclasses import dataclass
import click

@dataclass
class morseCode():
    message: str
    desire_decrypt: bool

    '''
    VARIABLE KEY
    'cipher' -> 'stores the morse translated form of the english string'
    'decipher' -> 'stores the english translated form of the morse string'
    'citext' -> 'stores morse code of a single character'
    'i' -> 'keeps count of the spaces between morse characters'
    'message' -> 'stores the string to be encoded or decoded'
    '''
    
    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}
    
    def __post_init__(self):
        # Run the main encrypt/decrypt sequence
        if self.desire_decrypt: 
            self.decrypt(self.message)
        else:
            self.encrypt(self.message)

    # Function to encrypt the string
    # according to the morse code chart
    def encrypt(self, message):
        self.cipher = ''
        for letter in message:
            if letter != ' ':
    
                # Looks up the dictionary and adds the
                # correspponding morse code
                # along with a space to separate
                # morse codes for different characters
                self.cipher += self.MORSE_CODE_DICT[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                self.cipher += ' '
    
        return self.cipher
    
    # Function to decrypt the string
    # from morse to english
    def decrypt(self, message):
    
        # extra space added at the end to access the
        # last morse code
        message += ' '
    
        self.decipher = ''
        citext = ''
        for letter in message:
    
            # checks for space
            if (letter != ' '):
    
                # counter to keep track of space
                i = 0
    
                # storing morse code of a single character
                citext += letter
    
            # in case of space
            else:
                # if i = 1 that indicates a new character
                i += 1
    
                # if i = 2 that indicates a new word
                if i == 2 :
    
                    # adding space to separate words
                    self.decipher += ' '
                else:
                    try:
                        # accessing the keys using their values (reverse of encryption)
                        self.decipher += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT
                        .values()).index(citext)]
                        citext = ''
                    except ValueError: 
                        self.decipher += '*'
        
        self.decipher = self.decipher.lower()

@click.command()
@click.option('--morse', prompt='Morse code with \'.\' and \'-\'',
              help='Know morse code. Do spaces and . and -') 
def runMain(morse):
    result = morseCodeToFrequency(morse)
    return result

def morseCodeToFrequency(morse):
    result_word = morseCode(morse, 'd').decipher
    print(f'Result Word:\t\t{result_word}')
    frequency_lookup = {
        'shell': 3.505,
        'halls': 3.515,
        'slick': 3.522,
        'trick': 3.532,
        'boxes': 3.535,
        'leaks': 3.542,
        'strobe': 3.545,
        'bistro': 3.552,
        'flick': 3.555,
        'bombs': 3.565,
        'break': 3.572,
        'brick': 3.575,
        'steak': 3.582,
        'sting': 3.592,
        'vector': 3.595,
        'beats': 3.600
    }
    try:
        result_frequency = frequency_lookup[result_word]
    except KeyError:
        raise KeyError(f'The key "{result_word}" was not found! Good luck player.')
    print(f'Result Frequency is:\t{result_frequency}MHz')
    return result_frequency

if __name__ == '__main__':
    values = runMain()