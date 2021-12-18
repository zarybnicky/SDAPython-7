import string
alphabet_up = string.ascii_uppercase
alphabet_low = string.ascii_lowercase

def caesar_encode(key: int, string: str) -> str:
    result = ""
    if string == "":
        return result
    if string[0] in alphabet_up:
        for char in string:
            if char == " ":
                result += " "
                continue
            elif alphabet_up.index(char) + key > 25:
                key_2 = ((alphabet_up.index(char) + key) % 25) - 1
                result += alphabet_up[key_2]
                continue
            else:
                result += alphabet_up[alphabet_up.index(char) + key]

    elif string[0] in alphabet_low:
        for char in string:
            if char == " ":
                result += " "
                continue
            elif alphabet_low.index(char) + key > 25:
                key_2 = ((alphabet_low.index(char) + key) % 25) - 1
                result += alphabet_low[key_2]
                continue
            else:
                result += alphabet_low[alphabet_low.index(char) + key]

    return result


def caesar_decode(key: int, string: str) -> str:
    result = ""
    if string == "":
        return result
    if string[0] in alphabet_up:
        for char in string:
            if char == " ":
                result += " "
                continue
            elif alphabet_up.index(char) - key < 0:
                key_2 = 25 - (abs(alphabet_up.index(char) - key) - 1)
                result += alphabet_up[key_2]
                continue
            else:
                result += alphabet_up[alphabet_up.index(char) - key]

    elif string[0] in alphabet_low:
        for char in string:
            if char == " ":
                result += " "
                continue
            elif alphabet_low.index(char) - key < 0:
                key_2 = 25 - (abs(alphabet_up.index(char) - key) - 1)
                result += alphabet_low[key_2]
                continue
            else:
                result += alphabet_low[alphabet_low.index(char) - key]

    return result


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_caesar_encode():
    assert caesar_encode(1, "") == ""
    assert caesar_encode(1, "ABC") == "BCD"
    assert caesar_encode(23, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
    assert caesar_encode(4, "attackatonce") == "exxegoexsrgi"

def test_caesar_decode():
    assert caesar_decode(1, "") == ""
    assert caesar_decode(1, "BCD") == "ABC"
    assert caesar_decode(23, "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD") == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    assert caesar_decode(4, "exxegoexsrgi") == "attackatonce"
# </editor-fold>
