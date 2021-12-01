import click

@click.command()
@click.option('--letters', prompt='Letter Combinations',
              help="""Each letter combination should be a new space.
                    Example of the first and third possible letters of a word: abcde  abfghe""")
def runMain(letters):
    """Gets the user input and runs the main method.

    Args:
        letters (str): Each letter combination should be a new space.
                        Example of the first and third possible letters of a word: abcde  abfghe

    Returns:
        list: A list of possible solutions based on the letters input
    """
    result = lettersCalculator(letters)
    return result

def lettersCalculator(customer_letters):
    """Takes a string of letters with spaces. Each space is considered the next letter in a word.
        For example: 'abc  deft' would match the word 'after' because 'a' is the first letter of
        the word, and 't' is the third letter of the word. We looked at the third letter because
        there were two spaces between the strings.

    Args:
        customer_letters (str): Letters that are clumped together. Each space resembles the
        next character in the matching string that are trying to be matched up.

    Returns:
        list: List of possible solutions to the requested query compared
        to the possible letters list.
    """
    letters_list = [
        'about',
        'after',
        'again',
        'below',
        'could',
        'every',
        'first',
        'found',
        'great',
        'house',
        'large',
        'learn',
        'never',
        'other',
        'place',
        'plant',
        'point',
        'right',
        'small',
        'sound',
        'spell',
        'still',
        'study',
        'their',
        'there',
        'these',
        'thing',
        'think',
        'three',
        'water',
        'where',
        'which',
        'world',
        'would',
        'write'
    ]

    customer_letters = customer_letters.split(' ')
    print(customer_letters)
    my_letters_list = []
    for test_word in letters_list:
        # Now we test the word against our potential letters
        all_exist = True
        for i, potential_letters in enumerate(customer_letters):
            if potential_letters == '':
                # Skip inputs that were just spaces. User intended to be empty
                continue
            if not isLettersAtIndex(test_word, i, potential_letters):
                all_exist = False
                break
        if all_exist:
            my_letters_list.append(test_word)

    if len(my_letters_list) == 1:
        print(f"Answer is: {my_letters_list[0]}")
    else:
        print(f'The options are: {my_letters_list}')

    return my_letters_list

def isLettersAtIndex(word, index, letters):
    """Checks if a list of letters exists at the index of a word.

    Args:
        word (str): A word to compare letters against
        index (int): An index of where to compare a letter against the word's index
        letters (list): letters that may match at a word's index

    Returns:
        bool: True if any letters match the word's index, False otherwise
    """
    for letter in letters:
        if letter == word[index]:
            return True
    return False

if __name__ == '__main__':
    runMain()
