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

    # to fetch usert activity
    events = fetch_user_activity(username)

    if events is None:
        sys.exit(1)

    if not events:
        print(f"No recent activity found | User:{username}.")
        return

    # Recent activity display (limit to 10 most recent events)
    for event in events[:10]:
        formatted_event = format_event(event)
        print(formatted_event)

    if len(events) > 10:
        print(f"\n... and {len(events) - 10} more activities")

if __name__ == "__main__":
    main()    

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

    except HTTPError as e:
        if e.status == 404:
             print(f"Error: User '{username}' not found.")
        elif e.status == 403:
             print("Error: API rate limit exceeded. Please try again later.")
        else:
             print(f"HTTP Error: {e.status} - {e.reason}")
        return None

    except URLError as e:
        print(f"Network Error: {e.reason}")
        return None

    except TimeoutError:
        print("Error: Request timed out. Please try again")
        return None

    except json.JSONDecodeError:
        print("Error: Failed to parse response from github API.")
        return None



def format_event_time(event_time_str):
    """
    Iso datetime string --> readable format
    """
    try:
        dt = datetime.fromisoformat(event_time_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M')
    except:
        return event_time_str

def format_event(event):
    # formatting the github event
    event_type = event.get('type', 'Unknown')
    repo_name = event.get('repo',{}).get('name', 'Unknown repo')
    created_at = event.get('created at', '')
    formatted_time = format_event_time(created_at)

    if event_type == 'PushEvent':
        payload = event.get('payload',{})
        commit_count = payload.get('size',0)
        return f"- Pushed {commit_count} commit(s) to {repo_name} at {formatted time}"

    elif event_type == 'IssuesEvent':
        payload = event.get('payload', {})
        action = payload.get('action', 'unknown')
        issue_title = payload.get('issue', {}).get('title', '')
        return f"- {action.capitalize()} issue '{issue_title}' in {repo_name} at {formatted_time}"
    
    elif event_type == 'PullRequestEvent':
        payload = event.get('payload', {})
        action = payload.get('action', 'unknown')
        pr_title = payload.get('pull_request', {}).get('title', '')
        return f"- {action.capitalize()} pull request '{pr_title}' in {repo_name} at {formatted_time}"
    
    elif event_type == 'WatchEvent':
        return f"- Starred {repo_name} at {formatted_time}"
    
    elif event_type == 'ForkEvent':
        return f"- Forked {repo_name} at {formatted_time}"
    
    elif event_type == 'CreateEvent':
        payload = event.get('payload', {})
        ref_type = payload.get('ref_type', 'repository')
        return f"- Created {ref_type} in {repo_name} at {formatted_time}"
    
    elif event_type == 'DeleteEvent':
        payload = event.get('payload', {})
        ref_type = payload.get('ref_type', 'branch')
        ref = payload.get('ref', '')
        return f"- Deleted {ref_type} '{ref}' in {repo_name} at {formatted_time}"
    
    else:
        return f"- {event_type} in {repo_name} at {formatted_time}"    