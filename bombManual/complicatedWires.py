from dataclasses import dataclass
import click

@dataclass
class wireClass():
    """Converts a user input into a cleaned user input of booleans if needed.

    Raises:
        Exception: Value was not yes/no or boolean
    """
    red: str
    blue: str
    star: str
    led: str

    def __post_init__(self):
        """Cleans user input from 'y'/'n' into boolean True/False.
        """
        self.red = self.convertYesNo(self.red)
        self.blue = self.convertYesNo(self.blue)
        self.star = self.convertYesNo(self.star)
        self.led = self.convertYesNo(self.led)

    def convertYesNo(self, yes_no):
        """Converts a string 'y' to True, 'n' to False

        Args:
            yes_no (str): A expected value of 'y' or 'n'

        Raises:
            Exception: Value was neither a 'y' or 'n'

        Returns:
            bool: 'y' -> True, 'n' -> False
        """
        if isinstance(yes_no, bool):
            return yes_no
        elif yes_no.strip() == 'y':
            return True
        elif yes_no.strip() == 'n':
            return False
        else:
            raise Exception(f'Value is not "y" or "n". Value was {yes_no}')


@click.command()
@click.option('--red', prompt='Red Coloring (y/n)',
              help='Wire has red coloring.')
@click.option('--blue', prompt='Blue Coloring (y/n)',
              help='Wire has blue coloring.')
@click.option('--star', prompt='Star (y/n)',
              help='Has Star symbol.')
@click.option('--led', prompt='LED On (y/n)',
              help='Yes if LED is on.')
def runMain(red, blue, star, led):
    """Runs the main function, works as a wrapper since it is using click to get user input.

    Args:
        red (str): Does the wire have red. 'y' if red.
        blue (str): Does the wire have blue. 'y' if blue.
        star (str): Does the wire have a star. 'y' if there is a Star.
        led (str): Does the wire have a LED. 'y' if there is an LED.

    Returns:
        str: A character which designates what to do with the wire
    """
    result = createWireRun(red, blue, star, led)
    return result

def createWireRun(red, blue, star, led):
    """Determines based on user input what the user should do with a designated wire.

    Args:
        red (str): Does the wire have red. 'y' if red.
        blue (str): Does the wire have blue. 'y' if blue.
        star (str): Does the wire have a star. 'y' if there is a Star.
        led (str): Does the wire have a LED. 'y' if there is an LED.

    Returns:
        str: A character which designates what to do with the wire
    """
    my_wire = wireClass(red, blue, star, led)
    result = complicatedWires(my_wire)
    print(f'\nResult: \"{printPretty(result)}\"\n')
    return result

def printPretty(my_char):
    """Pretty prints the result into an understandable string

    Args:
        my_char (str): A resulting string from the complicatedWires method

    Returns:
        str: A full description of what the resulting string means
    """
    match my_char:
        case 'C':
            return 'Cut the wire'
        case 'D':
            return 'Do NOT cut the wire'
        case 'B':
            return 'Cut wire if bomb has two or more batteries'
        case 'P':
            return 'Cut wire if bomb has a parallel port'
        case 'S':
            return 'Cut wire if last digit of serial number is EVEN'

def complicatedWires(my_wire):
    """Does the logic of the wire description to the correct action

    Args:
        my_wire (complicatedWires): An object representing the wire

    Returns:
        str: A representation of what to do to the wire
    """
    if (
        not my_wire.red and not my_wire.blue and not my_wire.led or
        my_wire.red and not my_wire.blue and my_wire.star and not my_wire.led
        ):
        # C	(!R!B!L)+(R!BS!L)
        # Cut the wire
        return 'C'
    elif (
        not my_wire.red and not my_wire.blue and not my_wire.star and my_wire.led or
        not my_wire.red and my_wire.blue and my_wire.star or
        my_wire.red and my_wire.blue and my_wire.star and my_wire.led
        ):
        # D	(!r!b!sl)+(!RBS)+(RBSL)
        # Do NOT cut the wire
        return 'D'
    elif (
        not my_wire.red and not my_wire.blue and my_wire.star and my_wire.led or
        my_wire.red and not my_wire.blue and my_wire.led
        ):
        # B	!R!BSL+R!BL
        # Batteries Method
        # Cut wire if bomb has two or more batteries
        return 'B'
    elif (
        not my_wire.red and my_wire.blue and my_wire.led or
        my_wire.red and my_wire.blue and my_wire.star and not my_wire.led
        ):
        # P	(!RBL)+(RBS!L)
        # Parallel Port Method
        # Cut wire if bomb has a parallel port
        return 'P'
    elif (
        not my_wire.red and my_wire.blue and not my_wire.star and not my_wire.led or
        my_wire.red and my_wire.blue and not my_wire.star or
        my_wire.red and not my_wire.star and not my_wire.led
        ):
        # S	(!RB!S!L)+(RB!S)+(R!S!L)
        # Cut wire if last digit of serial number is EVEN
        return 'S'
    else:
        return ''

if __name__ == '__main__':
    runMain()
