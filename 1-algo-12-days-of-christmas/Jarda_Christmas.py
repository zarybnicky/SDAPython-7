gifts = [
    'A partridge in a pear tree.',
    'Two turtle doves,',
    'Three French hens,',
    'Four calling birds,',
    'Five gold rings,',
    'Six geese a laying,',
    'Seven swans a swimming,',
    'Eight maids a milking,',
    'Nine ladies dancing,',
    'Ten lords a leaping,',
    'Eleven pipers piping,',
    'Twelve drummers drumming,',
]

numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
           "eighth", "ninth", "tenth", "eleventh", "twelft"]


def verse(n: int) -> str:
    text = []
    text.append(f"On the {numbers[n]} day of Christmas, my true love sent to me \n")
    for _ in range(n+1):
        text.append(gifts[_])

    print(text)

def whole_song() -> str:

    for _ in range(12):
        verse(_)

# <editor-fold defaultstate="collapsed" desc="Tests">
def test_verse():
    assert verse(1) == "On the first day of Christmas\nMy true love sent to me\nA partridge in a pear tree\n"
    assert verse(3) == "On the third day of Christmas\nMy true love sent to me\nThree French hens\nTwo turtle doves\nA partridge in a pear tree\n"
# </editor-fold>

whole_song()
