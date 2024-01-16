#!/usr/bin/python3
""" Function that queries the reddit API"""
import requests

def top_ten(subreddit):
    """Function that queries API if not a valid, print None"""
    req = requests.get(
            "https://ww.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
            )
    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
