#!/usr/bin/python3
"""Function to query subscribers on a given reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        results = response.json()
        subscribers = results["results"]["subscribers"]
        return subscribers
    else:
        return 0
