# Python program to implement Morse Code Translator


from dataclasses import dataclass
import click

@dataclass
class morseCode():
    """Morse code converter
    # Needlessly scraped from:
    # https://www.geeksforgeeks.org/morse-code-translator-python/
    """
    message: str

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
        self.decrypt(self.message)

    # Function to decrypt the string
    # from morse to english
    def decrypt(self, message):
        """Converts morse code into a string

        Args:
            message (str): Morse code string
        """

        # extra space added at the end to access the
        # last morse code
        message += ' '

        self.decipher = ''
        citext = ''
        for letter in message:

            # checks for space
            if letter != ' ':

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
    """Runs the main function of accepting the morse code and returning a frequency to select

    Args:
        morse (str): morse code values, ex: ... ..- -.-

    Returns:
        float: The MHz frequency that was discovered from the morse code
    """

    result = morseCodeToFrequency(morse)
    return result

def morseCodeToFrequency(morse):
    """Converts morsecode into a string result. Converts this string into a float from the

    Args:
        morse (str): The morse code that is found by following the flashing light from in-game.
         Start recording morse after the long pause in game.

    Raises:
        KeyError: The decoded morse does not match up with one of the lookup tables.
        Might need to get good.

    Returns:
        str: The frequency the user should input in game.
    """
    result_word = morseCode(morse).decipher
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
