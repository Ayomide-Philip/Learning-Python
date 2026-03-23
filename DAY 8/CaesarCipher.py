alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text_to_encode, shift_number):
    stringOfEncode = ""
    for texts in text_to_encode:
        if alphabet.count(texts) == 0:
            stringOfEncode += texts
        else:
            new_shift_index = alphabet.index(texts) + shift_number
            if len(alphabet) <= (new_shift_index):
                newIndex = (new_shift_index) % len(alphabet)
                stringOfEncode += alphabet[newIndex]
            else:
                stringOfEncode += alphabet[(new_shift_index)]

    print(stringOfEncode)


encode(text_to_encode=text, shift_number=shift)
