from dataclasses import dataclass
from typing import get_args
import click

@dataclass
class currentMemory():
    display: int
    label: int
    position: int

def getDisplay():
    display = click.prompt('Display', type=int)
    return display

def stage1(display):
    # Need position, label
    match display:
        case 1:
            position = 2
            label = click.prompt('What is the Label in the 2nd postion', type=int)
            printCommandToUser('Press the button in the 2nd position')
        case 2: 
            position = 2
            label = click.prompt('What is the Label in the 2nd postion', type=int)
            printCommandToUser('Press the button in the 2nd position.')
        case 3:
            position = 3
            label = click.prompt('What is the Label in the 3rd postion', type=int)
            printCommandToUser('Press the button in the 3rd position.')
        case 4:
            position = 4
            label = click.prompt('What is the Label in the 4th postion', type=int)
            printCommandToUser('Press the button in the 4th position.')

    memory = currentMemory(display, label, position)
    return memory

def stage2(main_memory, display):
    # Need label, position
    match display:
        case 1:
            label = 4
            position = click.prompt('What is the position of Label 4', type=int)
            printCommandToUser('Press the button with Label 4')
        case 2:
            position = main_memory[1-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in position {position}')
        case 3: 
            position = 1
            label = click.prompt('What is the Label in the 1st postion', type=int)
            printCommandToUser('Press the button in the 1st position')
        case 4:
            position = main_memory[1-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in position {position}')
    
    memory = currentMemory(display, label, position)
    return memory

def stage3(main_memory, display):
    # Need Display, Label
    match display:
        case 1:
            label = main_memory[2-1].label
            # position = click.prompt('What is the Position of label {label}', type=int)
            printCommandToUser(f'Press the button with label: {label}')
        case 2:
            label = main_memory[1-1].label
            # position = click.prompt('What is the Position of label {label}', type=int)
            printCommandToUser(f'Press the button with label: {label}')
        case 3: 
            label = click.prompt('What is the Label in the 3rd postion', type=int)
            printCommandToUser('Press the button in the 3rd position')
        case 4:
            label = 4
            # position = click.prompt('What is the Position of the button labeled 4', type=int)
            printCommandToUser(f'Press the button labeled 4')
    
    memory = currentMemory(display, label, None)
    return memory

def stage4(main_memory, display):
    # Need Display, Label
    match display:
        case 1:
            position = main_memory[1-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in the {position} position')
        case 2:
            label = click.prompt('What is the Label in the 1st postion', type=int)
            printCommandToUser(f'Press the button in the 1st position')
        case 3: 
            position = main_memory[2-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in the {position} position')
        case 4:
            position = main_memory[2-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in the {position} position')
    
    memory = currentMemory(display, label, None)
    return memory

def stage5(main_memory, display):
    # Need nothing
    match display:
        case 1:
            printCommandToUser(f'Press the button with the label {main_memory[1-1].label}')
        case 2:
            printCommandToUser(f'Press the button with the label {main_memory[2-1].label}')
        case 3: 
            printCommandToUser(f'Press the button with the label {main_memory[4-1].label}')
        case 4:
            printCommandToUser(f'Press the button with the label {main_memory[3-1].label}')
    return 

def printCommandToUser(my_string):
    print(f'\n{my_string}\n')
    return

def handleMain():
    main_memory = []

    print("Stage 1")
    display = getDisplay()
    memory = stage1(display)
    main_memory.append(memory)

    print("Stage 2")
    display = getDisplay()
    memory = stage2(main_memory, display)
    main_memory.append(memory)

    print("Stage 3")
    display = getDisplay()
    memory = stage3(main_memory, display)
    main_memory.append(memory)

    print("Stage 4")
    display = getDisplay()
    memory = stage4(main_memory, display)
    main_memory.append(memory)

    print("Stage 5")
    display = getDisplay()
    memory = stage5(main_memory, display)
    return

if __name__ == '__main__':
    handleMain()
