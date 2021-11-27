from bombManual import complicatedWires

def test_class_setup():
    my_wires = complicatedWires.wireClass('y', 'n', 'y', 'n')
    assert my_wires.red == True
    assert my_wires.blue == False
    assert my_wires.star == True
    assert my_wires.led == False

def test_DResult():
    result = complicatedWires.createWireRun('y', 'y', 'y', 'y')
    assert result == 'D'

def test_SResult():
    result = complicatedWires.createWireRun('y', 'y', 'n', 'n')
    assert result == 'S'

def test_PResult():
    result = complicatedWires.createWireRun('n', 'y', 'n', 'y')
    assert result == 'P'

def test_BResult():
    result = complicatedWires.createWireRun('y', 'n', 'y', 'y')
    assert result == 'B'

def test_CResult():
    result = complicatedWires.createWireRun('n', 'n', 'y', 'n')
    assert result == 'C'

def test_printPretty():
    assert complicatedWires.printPretty('B') == 'Cut wire if bomb has two or more batteries'