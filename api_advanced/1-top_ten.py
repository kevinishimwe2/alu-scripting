#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first
10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.

    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced:v1.0.0 (by /u/custom_user)"
    }
    # Limit to 10 posts to retrieve only the necessary amount of data
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])
            for child in children[:10]:
                print(child.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")