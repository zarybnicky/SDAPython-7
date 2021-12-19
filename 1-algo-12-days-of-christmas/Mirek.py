gifts = [
    'A partridge in a pear tree',
    'Two turtle doves',
    'Three French hens',
    'Four calling birds',
    'Five gold rings',
    'Six geese a laying',
    'Seven swans a swimming',
    'Eight maids a milking',
    'Nine ladies dancing',
    'Ten lords a leaping',
    'Eleven pipers piping',
    'Twelve drummers drumming',
]

def verse(n: int) -> str:
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelveth"]
    stacked_gifts = ""
    for gift in range(n-1, -1, -1):
        stacked_gifts += f"{gifts[gift]}\n"
    verse = (f"On the {days[n-1]} day of Christmas\n" +
        "My true love sent to me\n"
        f"{stacked_gifts}")
    return verse

def whole_song() -> str:
    pass

# <editor-fold defaultstate="collapsed" desc="Tests">
def test_verse():
    assert verse(1) == "On the first day of Christmas\nMy true love sent to me\nA partridge in a pear tree\n"
    assert verse(3) == "On the third day of Christmas\nMy true love sent to me\nThree French hens\nTwo turtle doves\nA partridge in a pear tree\n"
# </editor-fold>
