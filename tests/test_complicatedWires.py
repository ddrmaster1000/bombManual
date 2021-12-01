from bombManual import complicatedWires

def test_class_setup():
    """Checks class setup
    """
    my_wires = complicatedWires.wireClass('y', 'n', 'y', 'n')
    assert my_wires.red
    assert not my_wires.blue
    assert my_wires.star
    assert not my_wires.led

def test_DResult():
    """Checks for a 'D' result"""
    result = complicatedWires.createWireRun('y', 'y', 'y', 'y')
    assert result == 'D'

def test_SResult():
    """Checks for 'S' result"""
    result = complicatedWires.createWireRun('y', 'y', 'n', 'n')
    assert result == 'S'

def test_PResult():
    """Checks for 'P' result"""
    result = complicatedWires.createWireRun('n', 'y', 'n', 'y')
    assert result == 'P'

def test_BResult():
    """Checks for 'B' result"""
    result = complicatedWires.createWireRun('y', 'n', 'y', 'y')
    assert result == 'B'

def test_CResult():
    """Checks for 'C' result"""
    result = complicatedWires.createWireRun('n', 'n', 'y', 'n')
    assert result == 'C'

def test_printPretty():
    """Checks prettyPrint example for 'B' """
    assert complicatedWires.printPretty('B') == 'Cut wire if bomb has two or more batteries'
