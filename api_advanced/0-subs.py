#!/usr/bin/python3
import requests
# import sys

def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}

    response = requests.get(
        url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        return data.get("subscribers")
    except (AttributeError, ValueError):
        return 0