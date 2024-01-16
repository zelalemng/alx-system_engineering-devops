#!/usr/bin/python3
"""recursive function that queries the reddit API"""
import requests
import sys
after = None
count_dic = []

def count_words(subreddit, word_list):
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    url = "htts://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
            params=parameters)
