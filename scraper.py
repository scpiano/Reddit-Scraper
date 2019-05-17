import datetime
import os
import requests
from uuid import uuid4

def auth_request(): # Authorization required
    client_id = '' # need to find better way to store this
    state = str(uuid4())
    redirect_uri = 'http://localhost:8080'
    duration = 'temporary' # just for initial testing, need to change to permanent
    scope = 'read'

    auth_url = 'https://www.reddit.com/api/v1/authorize?client_id={}&response_type=code&state={}&redirect_uri={}&duration={}&scope={}'.format(client_id,state,redirect_uri,duration,scope)
    print(auth_url) # testing
    # requests.get(auth_url)

if __name__ == '__main__'
    auth_request()