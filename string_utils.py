def i_replace(string):
    new_text = string
    for letter in 'aáAeéEoóOuúU':
        new_text = new_text.replace(letter, 'i')
    return new_text


def upper_lower(string):
    new_text = ''
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_text += letter.upper()
        else:
            new_text += letter.lower()
    return new_text


dumb_words = {
    'qu': 'K',
    'cen': 'sen',
    'cion': 'sion',
    'yo': 'io',
    'te': 't',
    'de': 'D',
    'por': 'x',
    'todo': 'to2',
    '.':  ' XD ',
    'los': 'loa',
    'v': 'b',
    'ocu': 'oku',
}


def dumb_text(args):
    new_text = ' '.join(args).lower()
    for text, replace in dumb_words.items():
        new_text = new_text.replace(text, replace)
    return new_text
