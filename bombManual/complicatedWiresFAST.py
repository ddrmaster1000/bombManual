import complicatedWires
import click 

@click.command()
@click.option('--all', prompt='rbsl',
              help='Red, Blue, Star, LED.')
def runMain(all):
    red = False
    blue = False
    star = False
    led = False
    for var in list(all):
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
    while(True):
        runMain()