from dataclasses import dataclass
import click

@click.command()
@click.option('--letters', prompt='Letter Combinations',
              help="""Each letter combination should be a new space. 
                    Example of the first and third possible letters of a word: abcde  abfghe""") 
def runMain(letters):
    result = lettersCalculator(letters)
    return result

def lettersCalculator(customer_letters):
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
    for letter in letters:
        if letter == word[index]:
            return True
    return False

if __name__ == '__main__':
    runMain()