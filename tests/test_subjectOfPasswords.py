from bombManual import subjectOfPasswords

def test_aboutStress():
    """ Tests single spaces, for one word"""
    values = subjectOfPasswords.lettersCalculator('a eoqzbld o')
    assert values == ['about']

def test_doubleSpaces():
    """ Tets a double space and if it works"""
    values = subjectOfPasswords.lettersCalculator('a  o')
    assert values == ['about']

def test_isLettersAtIndex():
    """ Tests if some letters exist at an index """
    assert subjectOfPasswords.isLettersAtIndex('phat', 1, 'lgbth')
