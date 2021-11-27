from bombManual import subjectOfPasswords

def test_aboutStress():
    values = subjectOfPasswords.lettersCalculator('a eoqzbld o')
    assert values == ['about']

def test_doubleSpaces():
    values = subjectOfPasswords.lettersCalculator('a  o')
    assert values == ['about']

def test_isLettersAtIndex():
    assert subjectOfPasswords.isLettersAtIndex('phat', 1, 'lgbth')