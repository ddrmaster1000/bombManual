from bombManual import morseCode

def test_morseCode_shell():
    """Tests the word shell"""
    result_word = morseCode.morseCodeToFrequency('... .... . .-.. .-..')
    assert result_word == 3.505

def test_morseCode_bistro():
    """Tests the word bistro"""
    result_word = morseCode.morseCodeToFrequency('-... .. ... - .-. ---')
    assert result_word == 3.552

def test_morseCode_vector():
    """Tests the word vector"""
    result_word = morseCode.morseCodeToFrequency('...- . -.-. - --- .-.')
    assert result_word == 3.595
