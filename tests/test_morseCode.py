from bombManual import morseCode

def test_morseCode_shell():
    result_word = morseCode.morseCodeToFrequency('... .... . .-.. .-..')
    assert result_word == 3.505

def test_morseCode_bistro():
    result_word = morseCode.morseCodeToFrequency('-... .. ... - .-. ---')
    assert result_word == 3.552

def test_morseCode_vector():
    result_word = morseCode.morseCodeToFrequency('...- . -.-. - --- .-.')
    assert result_word == 3.595
