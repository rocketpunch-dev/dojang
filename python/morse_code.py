_CODE = (
    ('B', '-...'),
    ('C', '-.-.'),
    ('F', '..-.'),
    ('H', '....'),
    ('J', '.---'),
    ('L', '.-..'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('V', '...-'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('W', '.--'),
    ('U', '..-'),
    ('D', '-..'),
    ('G', '--.'),
    ('K', '-.-'),
    ('O', '---'),
    ('R', '.-.'),
    ('S', '...'),
    ('I', '..'),
    ('M', '--'),
    ('A', '.-'),
    ('N', '-.'),
    ('E', '.'),
    ('T', '-'),
)

MORSE_CODE = dict([(x, y) for x, y in _CODE])
MORSE_CODE_REVERSE = dict([(y, x) for x, y in _CODE])


def reverse_morse_code(input_code):
    result_morse_code = list()

    for code in input_code.split(' '):
        result_morse_code.append(MORSE_CODE_REVERSE.get(code) or ' ')

    return ''.join(result_morse_code)


def make_morse_code(input_text):
    result_morse_code = list()

    for _text in input_text:
        result_morse_code.append(MORSE_CODE.get(_text.upper()) or '')

    return ' '.join(result_morse_code)


if __name__ == "__main__":
    INPUT_DATA = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
    print(INPUT_DATA)

    text = reverse_morse_code(INPUT_DATA)
    print(text)

    morse_code = make_morse_code(text)
    print(morse_code)
