import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

usage_instructions: str = """
Usage: twitter-feed app requires two extra arguments - two files:
-- First is the user.txt followed by tweet.txt
-- The argument should resemble a file path e.g /path/to/user.txt and /path/to/twitter.txt
-- running the application could be: twitter_feed /path/to/user.txt /path/to/twitter.txt
"""


def main() -> None:
    """The main entrypoint for this script used in the setup.py file."""
    input_data: Tuple[Dict, List[List[str]]] = parse_args()
    format_output(users=input_data[0], tweets=input_data[1])


def is_files(file_paths: List[str]) -> bool:
    for file_path in file_paths:
        if not Path(file_path).is_file():
            return False
    return True


def parse_file_inputs(file_paths: List[str]) -> Tuple[Dict, List]:
    """
    This function gets the data within the input files and reformats it into:
    users  -> Dict[str, Set[str]] - a dict of users and the people they follow
    tweets -> List[List[str]] - a list of tweets and their sender
    """

    users_dict: Dict[str, Set[str]] = dict()
    tweets_list: List[List[str]] = list()
    with open(file_paths[0], 'r', encoding='utf8') as user_file:
        for line in user_file.readlines():
            line: str = line.strip()
            line: str = line.split(' follows ')  # get the user and those followed by the user

            user: str = line[0]
            followed_by: List[str] = line[1].split(', ')

            if user in users_dict.keys():
                users_dict[user].update(followed_by)
            else:
                users_dict[user] = set()
                users_dict[user].update(followed_by)

            for user in followed_by:
                if user not in users_dict.keys():
                    users_dict[user] = set()

    with open(file_paths[1], 'r', encoding='utf8') as tweet_file:
        for line in tweet_file.readlines():
            line: str = line.strip()
            line: str = line.split('> ')

            user: str = line[0]
            tweet: str = line[1]

            tweets_list.append([user, tweet])
    return users_dict, tweets_list


def format_output(users: Dict[str, Set[str]], tweets: List[List[str]]) -> None:
    """
    This function prints out a simulated twitter feed given a dict of users including the people
    they follow and finally a list of tweets including the sender
    """
    sorted_users: List[str] = sorted(users.keys())
    for user in sorted_users:
        users_followed: List[str] = users[user]
        print(user)

        for item in tweets:
            if item[0] in [user] + list(users_followed):  # user in the list of people they follow including themself
                tweet: str = item[1]
                print(f'\t@{item[0]}: {tweet}')


def parse_args() -> List[str]:
    print(sys.argv)
    if len(sys.argv) != 3:
        print(usage_instructions)
        exit()

    if len(sys.argv) == 3 and is_files(sys.argv[1:]):
        return parse_file_inputs(sys.argv[1:])
    else:
        sys.argv.pop(0)
        return sys.argv


if __name__ == '__main__':
    main()
