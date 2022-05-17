import os

import pytest

from twitter_feed import feed_module


def test_valid_read_from_file(data_regression):
    """
    Test the handling of a file input -  this also tests if the data is parsed correctly
    """

    file_paths = [f'{os.path.abspath(os.getcwd())}/sample/user.txt', f'{os.path.abspath(os.getcwd())}/sample/tweet.txt']
    actual = feed_module.parse_file_inputs(file_paths)
    data_regression.check(actual)


def test_invalid_read_from_file():
    """
    Test the handling of a file input -  this also tests if the data is parsed correctly
    """

    file_paths = [f'{os.path.abspath(os.getcwd())}/sample/user.txt']
    with pytest.raises(Exception) as exc_info:
        feed_module.parse_file_inputs(file_paths)
    assert str(exc_info.value) == 'This function expects only two valid file paths!'


def test_valid_formatted_feed(data_regression):
    users_dict = {'Ward': {'Alan', 'Martin'}, 'Alan': {'Martin'}, 'Martin': set()}
    tweets_list = [
        ['Alan', 'If you have a procedure with 10 parameters, you probably missed some.'],
        [
            'Ward',
            'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1'
            ' errors.',
        ],
        ['Alan', 'Random numbers should not be generated with a method chosen at random.'],
    ]
    actual = feed_module.format_output(users=users_dict, tweets=tweets_list)
    data_regression.check(actual)
