import complicatedWires
import click

@click.command()
@click.option('--all_input', prompt='rbsl',
              help='Red, Blue, Star, LED.')
def runMain(all_input):
    """Runs the complicatedWires module in quicker fashion.


    Args:
        all_input (str): A string of the features discovered. [
            Red = 'r',
            Blue = 'b',
            Star = 's',
            LED = 'l',
        ]
        So for example, a string of 'bl' means to execute program that
        had a 'Blue' and 'LED' signature.

    Returns:
        str: A string result of what to do to the wire.
    """
    red = False
    blue = False
    star = False
    led = False
    for var in list(all_input):
        if var == 'r':
            red = True
        elif var == 'b':
            blue = True
        elif var == 's':
            star = True
        elif var == 'l':
            led = True

    result = complicatedWires.createWireRun(red, blue, star, led)
    return result

if __name__ == '__main__':
    runMain()
