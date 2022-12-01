import re


def is_palindrome(text: str,
                  case_sensitive: bool = False,
                  only_alphanum: bool = True) -> bool:
    if text == '':
        raise ValueError

    if not case_sensitive:
        text = text.lower()

    if only_alphanum:
        text = re.sub('[^0-9a-zA-Z]+', '', text)

    return text == text[::-1]


if __name__ == '__main__':
    strings = ['ABBA', 'Anna', 'Karel', 'A Man, a Plan, a Canal: Panama']
    for s in strings:
        if is_palindrome(s):
            print(f'{s} is palindrome!')
        else:
            print(f'{s} is not palindrome!')
