MORSE_CODE = (
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


def reverse_morse_code(morse_code):
    reversed_text = morse_code

    for key, value in MORSE_CODE:
        reversed_text = reversed_text.replace(value, key)

    reversed_text = reversed_text.replace('  ', '+')
    reversed_text = reversed_text.replace(' ', '')
    reversed_text = reversed_text.replace('+', ' ')

    return reversed_text


def make_morse_code(input_text):
    MORSE_CODE_DICT = dict(MORSE_CODE)

    result_morse_code = list()
    for text in input_text:
        if text == ' ':
            result_morse_code.append('*')
        else:
            result_morse_code.append(MORSE_CODE_DICT.get(text.upper()))

    return ' '.join(result_morse_code).replace('*', '')


if __name__ == "__main__":
    INPUT_DATA = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
    print(INPUT_DATA)

    text = reverse_morse_code(INPUT_DATA)
    print(text)

    morse_code = make_morse_code(text)
    print(morse_code)
