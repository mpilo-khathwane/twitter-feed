import sys
from typing import Dict, List, Tuple
from twitter_feed.feed_module import parse_args,format_output


sys.argv.append('./sample/user.txt')
sys.argv.append('./sample/tweet.txt')

input_data: Tuple[Dict, List[List[str]]] = parse_args()
format_output(users=input_data[0], tweets=input_data[1])
