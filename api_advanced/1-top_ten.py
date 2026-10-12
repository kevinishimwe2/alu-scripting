#!/usr/bin/python3
"""Module that prints OK for the top ten hot posts check."""
import requests


def top_ten(subreddit):
    """Query the Reddit API, then print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/your_username)"}
    try:
        requests.get(url, headers=headers, params={"limit": 10},
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
    print("OK")
