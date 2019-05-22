import datetime
from os import path
import requests
import json

user_agent = 'Reddit-Scraper v1.0 default'

def make_config(user_agent=user_agent,subreddits=["buildapcsales","hardwareswap"],search_term='[USA-WA]',limit=1,sort='new'):
    """
    Takes in a user_agent, string/list of subreddits, a search_term, limit and sort type to create a config file used in
    making the Reddit API requests.
    """
    params = {'user_agent':user_agent,'subreddits':subreddits,'search_term':search_term,'limit':limit,'sort':sort}

    if path.isfile('config.json'):
        print('Config file exists, updating with input parameters.')
        with open('config.json', 'r') as config_in:
            config = json.load(config_in)
        with open('config.json', 'w') as config_out:
            config.update(params)
            json.dump(config, config_out)
    else:
        print('Config file does not exist, creating file with default parameters.')
        with open('config.json', 'w') as config_out:
            json.dump(params, config_out)

def make_request():  
    """
    Takes the config file and creates/makes requests to the Reddit API based on information provided.
    """
    with open('config.json') as config_json:
        config = json.load(config_json)
    
    user_agent = {'user-agent':config['user_agent']}
    subreddits = config['subreddits']
    search_term = config['search_term']
    limit = config['limit']
    sort = config['sort']

    for subreddit in subreddits:
        base_url = 'https://www.reddit.com/r/{}/search.json?restrict_sr=1&q={}&limit={}&sort={}'.format(subreddit, search_term, limit, sort) 

        try:
            print('GET: '+base_url)
            api_request = requests.get(base_url, headers = user_agent)
            json_response = api_request.json()
            print(json_response['data']['children'][0]['data']['url'])
        except Exception as e:
            print('Could not complete request:{}'.format(e))


if __name__ == '__main__':
    make_config()
    make_request()