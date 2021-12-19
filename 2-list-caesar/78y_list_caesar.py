

def caesar_encode(key: int, string: str) -> str:
    result = ""
    for char in result:
        char = char  # ???
        result += char
    return result


def caesar_decode(key: int, string: str) -> str:
    return string


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_caesar_encode():
    assert caesar_encode(1, "") == ""
    assert caesar_decode(1, "ABC") == "BCD"
    assert caesar_encode(23, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
    assert caesar_encode(4, "attackatonce") == "exxegoexsrgi"

def test_caesar_decode():
    assert caesar_decode(1, "") == ""
    assert caesar_decode(1, "BCD") == "ABC"
    assert caesar_decode(23, "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD") == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    assert caesar_decode(4, "exxegoexsrgi") == "attackatonce"
# </editor-fold>
