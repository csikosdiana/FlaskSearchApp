from mock import patch
import pytest

from FlaskSearchApp.data_processing import get_results, get_select_map


CONTACTS=  [
    {
    "job_history": [
      "Sibelius"
    ],
    "company": "Mattis Corporation",
    "email": "vehicula@et.com",
    "city": "Westerlo",
    "name": "David Harrington",
    "country": "Spain"
    },
    {
    "job_history": [
      "Apple Systems",
      "Chami",
      "Finale"
    ],
    "company": "Porttitor Scelerisque Neque Company",
    "email": "mollis@acliberonec.edu",
    "city": "Grande Prairie",
    "name": "Cleo Sanford",
    "country": "Comoros"
    },
    {
    "job_history": [
      "Macromedia",
      "Altavista",
      "Apple Systems"
    ],
    "company": "Posuere LLP",
    "email": "Proin.vel@accumsan.edu",
    "city": "Celle",
    "name": "Tatyana Daniels",
    "country": "Comoros"
    },
]


@patch('FlaskSearchApp.data_processing.contacts', CONTACTS)
def test_get_select_map():

    expected_select_map = {
        'Job history': {
            'sibelius': [0],
            'apple systems': [1, 2],
            'chami': [1],
            'finale': [1],
            'macromedia': [2],
            'altavista': [2]
        },
        'Company': {
            'mattis corporation': [0],
            'porttitor scelerisque neque company': [1],
            'posuere llp': [2]
        },
        'Email': {
            'vehicula@et.com': [0],
            'mollis@acliberonec.edu': [1],
            'proin.vel@accumsan.edu': [2]
        },
        'City': {
            'westerlo': [0],
            'grande prairie': [1],
            'celle': [2]
        },
        'Name': {
            'david harrington': [0],
            'cleo sanford': [1],
            'tatyana daniels': [2]
        },
        'Country': {
            'spain': [0],
            'comoros': [1, 2]
        }
    }
    test_select_map = get_select_map()
    assert test_select_map == expected_select_map


@patch('FlaskSearchApp.data_processing.contacts', CONTACTS)
@pytest.mark.parametrize('test_selected, test_search_term, expected_results', [
    ('Job history', 'Altavista', (CONTACTS[2],)),
    ('Job history', 'apple systems', (CONTACTS[1], CONTACTS[2])),
    ('Job history', 'apple', None),
    ('Job history', None, CONTACTS),
    ('Company', 'Posuere LLP', (CONTACTS[2],)),
    ('Company', 'mattis corporation', (CONTACTS[0],)),
    ('Company', 'o', None),
    ('Company', None, CONTACTS),
    ('Email', 'Proin.vel@accumsan.edu', (CONTACTS[2],)),
    ('Email', 'proin.vel@accumsan.edu', (CONTACTS[2],)),
    ('Email', 'test@email.com', None),
    ('Email', None, CONTACTS),
    ('City', 'Westerlo', (CONTACTS[0],)),
    ('City', 'CELLE', (CONTACTS[2],)),
    ('City', 'London', None),
    ('City', None, CONTACTS),
    ('Name', 'Cleo Sanford', (CONTACTS[1],)),
    ('Name', 'david harrington', (CONTACTS[0],)),
    ('Name', 'John Doe', None),
    ('Name', None, CONTACTS),
    ('Country', 'comoros', (CONTACTS[1], CONTACTS[2])),
    ('Country', 'Spain', (CONTACTS[0],)),
    ('Country', 'Hungary', None),
    ('Country', None, CONTACTS),
])
def test_get_results(test_selected, test_search_term, expected_results):
    assert get_results(test_selected, test_search_term) == expected_results

