import datetime
import os
import requests
import json

user_agent = 'Reddit-Scraper v1.0 default'

def make_config(user_agent=user_agent,subreddits=["buildapcsales","hardwareswap"],search_term='[USA-WA]',limit=1,sort='new'):
    with open('config.json', 'r') as config_in:
        config = json.load(config_in)
    with open('config.json', 'w') as config_out:
        config.update({'user_agent':user_agent,'subreddits':subreddits,'search_term':search_term,'limit':limit,'sort':sort})
        json.dump(config, config_out)

def make_request():  
    """
    Takes a string or list of strings for subreddits requested, defaulting to buildapcsales and hardwareswap.
    Also takes in a string or list of strings for search term, defaulting to '[USA-WA]' for the US state of Washington, a limit
    on the data requested and a sorting that can be one of the following: hot, new, comments, relevance or top.
    """
    with open('config.json') as config_json:
        config = json.load(config_json)
    
    user_agent = config['user_agent']
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
    make_config()
    make_request()