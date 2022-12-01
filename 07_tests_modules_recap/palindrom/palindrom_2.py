import re


strings = [
    'ABBA',
    'Anna',
    'A Man, a Plan, a Canal: Panama',
]


def is_palindrome(text, case_sensitive=True, only_alphanum=True):
    if not case_sensitive:
        text = text.lower()

    if only_alphanum:
        text = re.sub('[^0-9a-zA-Z]+', '', text)

    for i in range(len(text)):
        if text[i] != text[-(i + 1)]:
            return False

    return True


if __name__ == '__main__':
    for s in strings:
        if is_palindrome(s):
            print('"{}" is palindrome!'.format(s))
        else:
            print('"{}" is not palindrome!'.format(s))
