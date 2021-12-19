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

days = {1: "first", 2: "second", 3:"third", 4:"fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}

def verse(n: int) -> str:
    g = f""
    if n == 1:
        return f"On the {days[n]} day of Christmas\nMy true love sent to me\nA partridge in a pear tree.\n"
    for i in range(n - 1, 0, -1):
        g += f"{gifts[i]}\n"
    return f"On the {days[n]} day of Christmas\nMy true love sent to me\n{g}And a partridge in a pear tree.\n"

def whole_song() -> str:
    for i in range(1, 12):
        print(verse(i))



# <editor-fold defaultstate="collapsed" desc="Tests">
def test_verse():
    assert verse(1) == "On the first day of Christmas\nMy true love sent to me\nA partridge in a pear tree.\n"
    assert verse(3) == "On the third day of Christmas\nMy true love sent to me\nThree French hens,\nTwo turtle doves,\nAnd a partridge in a pear tree.\n"
# </editor-fold>

