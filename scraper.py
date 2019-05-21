import datetime
import os
import requests
from uuid import uuid4

def make_request(subreddits=['buildapcsales','hardwareswap'], search_term='[USA-WA]', limit=10, sort='new'):  
    """
    Takes a string or list of strings for subreddits requested, defaulting to buildapcsales and hardwareswap.
    Also takes in a string or list of strings for search term, defaulting to '[USA-WA]' for the US state of Washington, a limit
    on the data requested and a sorting.
    """
    base_url = ''

    for subreddit in subreddits:
        base_url = 'https://www.reddit.com/r/{}/search.json?restrict_sr=1&q={}&limit={}&sort={}'.format(subreddit, search_term, limit, sort) 
        try:
            print(base_url)
            API_request = requests.get(base_url)
            print(API_request)
        except Exception as e:
            print('Could not complete request:{}'.format(e))


if __name__ == '__main__':
    make_request()