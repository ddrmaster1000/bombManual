import click
from dataclasses import dataclass

@dataclass
class wireClass():
    red: str
    blue: str
    star: str
    led: str

    def __post_init__(self):
        self.red = self.convertYesNo(self.red)
        self.blue = self.convertYesNo(self.blue)
        self.star = self.convertYesNo(self.star)
        self.led = self.convertYesNo(self.led)

    def convertYesNo(self, yes_no):
        """Converts a y or n to true or false"""
        if isinstance(yes_no, bool):
            return yes_no 

        new_yes_no = yes_no.strip()
        if new_yes_no == 'y':
            return True
        elif new_yes_no == 'n':
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
    result = createWireRun(red, blue, star, led)
    return result

def createWireRun(red, blue, star, led):
    my_wire = wireClass(red, blue, star, led)
    result = complicatedWires(my_wire)
    print(f'\nResult: \"{printPretty(result)}\"\n')
    return result

def printPretty(my_char):
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
    """ Does the logic of the wire description to the correct action """
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


if __name__ == '__main__':
    runMain()