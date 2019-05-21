import datetime
import os
import requests
import json
    
def make_request(*args):  
    """
    Takes a string or list of strings for subreddits requested, defaulting to buildapcsales and hardwareswap.
    Also takes in a string or list of strings for search term, defaulting to '[USA-WA]' for the US state of Washington, a limit
    on the data requested and a sorting that can be one of the following: hot, new, comments, relevance or top.
    """
    with open('config.json') as config_json:
        config = json.load(config_json)
    
    user_agent = {'user-agent':config['user_agent']}
    subreddits = config['subreddits']
    search_term = config['search_term']
    limit = config['limit']
    sort = config['sort']

    for subreddit in subreddits:
        print(subreddit)
        base_url = 'https://www.reddit.com/r/{}/search.json?restrict_sr=1&q={}&limit={}&sort={}'.format(subreddit, search_term, limit, sort) 

        try:
            print(base_url)
            api_request = requests.get(base_url, headers = user_agent)
            print(api_request.json())
        except Exception as e:
            print('Could not complete request:{}'.format(e))


if __name__ == '__main__':
    make_request()