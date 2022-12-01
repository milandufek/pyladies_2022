import pytest
# from palindrom import is_p as is_palindrome
from palindrom_3 import is_palindrome


def test_palindrome():
    with pytest.raises(ValueError):
        is_palindrome('')


def test_palindrome_no_case():
    assert is_palindrome('Anna', case_sensitive=False)
    assert not is_palindrome('Anna', case_sensitive=True)


def test_palindrome_onl_alnum():
    assert is_palindrome('A Man, a Plan, a Canal: Panama',
                         case_sensitive=False, only_alphanum=True)
    assert not is_palindrome('A Man, a Plan, a Canal: Panama',
                             case_sensitive=True, only_alphanum=False)
    assert not is_palindrome('A Man, a Plan, a Canal: Panama',
                             case_sensitive=True, only_alphanum=True)
    assert not is_palindrome('A Man, a Plan, a Canal: Panama',
                             case_sensitive=False, only_alphanum=False)
