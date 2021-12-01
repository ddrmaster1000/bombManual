from bombManual import onTheSubjectOfMemory as sm

# Debugging with pytest: /env/Scripts/python.exe -m pytest --pdb
# Add an 'assert 0' if you want to produce a failure and break there

# Unit Tests
def test_stage1(mocker):
    """ Tests stage 1 """
    mocker.patch('click.prompt', return_value=3)
    result = sm.stage1(1)
    assert result == sm.currentMemory(display=1, label=3, position=2)

def test_stage2(mocker):
    """ Tests stage 2 """
    mocker.patch('click.prompt', return_value=2)
    result = sm.stage2([sm.currentMemory(display=1, label=3, position=2)], 2)
    assert result == sm.currentMemory(display=2, label=2, position=2)

def test_stage3(mocker):
    """ Tests stage 3 """
    mocker.patch('click.prompt', return_value=2)
    result = sm.stage3([sm.currentMemory(display=1, label=3, position=2),
                        sm.currentMemory(display=2, label=2, position=2)],
                        3)
    assert result == sm.currentMemory(display=3, label=2, position=None)

def test_stage4(mocker):
    """ Tests stage 4 """
    mocker.patch('click.prompt', return_value=3)
    result = sm.stage4([sm.currentMemory(display=1, label=3, position=2),
                        sm.currentMemory(display=2, label=2, position=2),
                        sm.currentMemory(display=3, label=2, position=1)],
                        1)
    assert result == sm.currentMemory(display=1, label=3, position=None)

def test_stage5(mocker):
    """ Tets stage 5 """
    mocker.patch('click.prompt', return_value=3)
    result = sm.stage4([sm.currentMemory(display=1, label=3, position=2),
                        sm.currentMemory(display=2, label=2, position=2),
                        sm.currentMemory(display=3, label=2, position=1),
                        sm.currentMemory(display=1, label=3, position=None)],
                        1)
    assert result == sm.currentMemory(display=1, label=3, position=None)

# Full Test
def test_fullTest(mocker):
    """ Runs a full test based on the stages below
        The labels going from 0 position -> 4 position.
        Each line is the next stage
        Stage1: 1 3 4 2
        Stage2: 2 4 1 2
        Stage3: 4 3 2 1
        Stage4: 1 4 2 3
        Stage5: 3 2 1 4
    """

    memory = []
    mocker.patch('click.prompt', return_value=2)
    result = sm.stage1(4)
    memory.append(result)
    assert result == sm.currentMemory(display=4, label=2, position=4)

    mocker.patch('click.prompt', return_value=2)
    result = sm.stage2(memory, 2)
    memory.append(result)
    assert result == sm.currentMemory(display=2, label=2, position=4)

    mocker.patch('click.prompt', return_value=3)
    result = sm.stage3(memory, 4)
    memory.append(result)
    assert result == sm.currentMemory(display=4, label=4, position=None)

    mocker.patch('click.prompt', return_value=3)
    result = sm.stage4(memory, 1)
    memory.append(result)
    assert result == sm.currentMemory(display=1, label=3, position=None)

    mocker.patch('click.prompt', return_value=2)
    result = sm.stage5(memory, 2)
    memory.append(result)
    assert result == sm.currentMemory(display=2, label=2, position=None)
