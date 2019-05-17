import datetime
import os
import requests
import requests-oauthlib
from uuid import uuid4

def auth_request():
    client_id = ''
    state = str(uuid4())
    redirect_uri = 'http://localhost:8080'
    duration = 'temporary'
    scope = 'read'

    auth_url = 'https://www.reddit.com/api/v1/authorize?client_id={}&response_type=code&state={}&redirect_uri={}&duration={}&scope={}'.format(client_id,state,redirect_uri,duration,scope)
