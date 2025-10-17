#!/usr/bin/env python3

"""

github user activity cli TOOL
shows:Github user activity using built in python

"""

import sys
import json
from urllib.request import urlopen,Request
from urllib.error import HTTPError,URLError
from datetime import datetime

def print_usage():
    # Print usage instructions.
    print("Usage: python github-activity.py <github-username>")
    print("Example:")
    print("python github-activity.py abydow") 

def main():
    #important function(main)
    #checks command line arg
    if len(sys.argv) != 2:
        print("WRONG!!!")
        print_usage()
        sys.exit(1)

    username = sys.argv[1]

    #Validation check<username>
    if not username  or not username.replace('-','').replace('_','').isalnum():
        print("ERROR:")
        print("Please Enter a valid USername")
        sys.exit(1)
    print("┌"+"─" * 35 + "┐")
    print(f"| Fetching activity for github user |")
    print("└"+"─" * 35 + "┘")

def fetch_user_activity(username):
    #fetches useractivity from the api<:
    url = f"https://api.github.com/users/{username}'/events"
    #header
    headers = {'User-Agent':'github-user-activity-cli'}
    request = Request(url,headers=headers)
    #to handle errors during request
    try:
	with urlopen(request,timeout=10) as response:
             if response.status == 200:
                 data = response.read()
                 events = json.loads(data.decode('utf-8'))
                 return events
             else:
                 print(f"Error: Received status code {response.status}")
                 return None
