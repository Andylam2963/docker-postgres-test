import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import getEmail, getID

firstname = 'Foo'
lastname = 'Bar'


def test_getEmail():
    expected = 'foo_bar@domain.com'
    ans = getEmail(firstname, lastname)

    assert ans == expected


def test_getID():
    expected = 83880501
    ans = getID(firstname, lastname)

    assert ans == expected
