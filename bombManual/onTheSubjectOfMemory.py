from dataclasses import dataclass
import click

@dataclass
class currentMemory():
    """Basic Class that has the display, label, and position of the current stage's result.
    """
    display: int
    label: int
    position: int

def getDisplay():
    """Gets the current display integer from the user.

    Returns:
        int: The display value from the user.
    """
    display = click.prompt('Display', type=int)
    return display

def stage1(display):
    """Stage 1 of the subject of memory.

    Args:
        main_memory (List(currentMemory())): A list of the currentMemory Object.
        A running list of previous stages
        display (int): Current display from the Subject of Memory game for this stage.

    Returns:
        currentMemory: The currentMemory result object with what was selected.
    """
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
    """Stage 2 of the subject of memory.

    Args:
        main_memory (List(currentMemory())): A list of the currentMemory Object.
        A running list of previous stages
        display (int): Current display from the Subject of Memory game for this stage.

    Returns:
        currentMemory: The currentMemory result object with what was selected.
    """
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
    """Stage 3 of the subject of memory.

    Args:
        main_memory (List(currentMemory())): A list of the currentMemory Object.
        A running list of previous stages
        display (int): Current display from the Subject of Memory game for this stage.

    Returns:
        currentMemory: The currentMemory result object with what was selected.
    """
    # Need Display, Label
    match display:
        case 1:
            label = main_memory[2-1].label
            printCommandToUser(f'Press the button with label: {label}')
        case 2:
            label = main_memory[1-1].label
            printCommandToUser(f'Press the button with label: {label}')
        case 3:
            label = click.prompt('What is the Label in the 3rd postion', type=int)
            printCommandToUser('Press the button in the 3rd position')
        case 4:
            label = 4
            printCommandToUser('Press the button labeled 4')

    memory = currentMemory(display, label, None)
    return memory

def stage4(main_memory, display):
    """Stage 4 of the subject of memory.

    Args:
        main_memory (List(currentMemory())): A list of the currentMemory Object.
        A running list of previous stages
        display (int): Current display from the Subject of Memory game for this stage.

    Returns:
        currentMemory: The currentMemory result object with what was selected.
    """
    # Need Display, Label
    match display:
        case 1:
            position = main_memory[1-1].position
            label = click.prompt(f'What is the Label in the {position} postion', type=int)
            printCommandToUser(f'Press the button in the {position} position')
        case 2:
            label = click.prompt('What is the Label in the 1st postion', type=int)
            printCommandToUser('Press the button in the 1st position')
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
    """Stage 5 of the subject of memory.

    Args:
        main_memory (List(currentMemory())): A list of the currentMemory Object.
        A running list of previous stages
        display (int): Current display from the Subject of Memory game for this stage.

    Returns:
        currentMemory: The currentMemory result object with what was selected.
    """
    # Need nothing
    match display:
        case 1:
            label = main_memory[1-1].label
            printCommandToUser(f'Press the button with the label {label}')
        case 2:
            label = main_memory[2-1].label
            printCommandToUser(f'Press the button with the label {label}')
        case 3:
            label = main_memory[4-1].label
            printCommandToUser(f'Press the button with the label {label}')
        case 4:
            label = main_memory[3-1].label
            printCommandToUser(f'Press the button with the label {label}')
    return currentMemory(display, label, None)

def printCommandToUser(my_string):
    """Pretty Print a result to the user

    Args:
        my_string (str): The string to pretty print to the user.
    """
    print(f'\n{my_string}\n')

def handleMain():
    """Iterates over each stage of the subject of memory quest.
    """
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

if __name__ == '__main__':
    handleMain()
