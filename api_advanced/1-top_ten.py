#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints titles or None if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get("data")
        children = data.get("children")

        for i in range(min(10, len(children))):
            print(children[i].get("data").get("title"))
    except (AttributeError, ValueError):
        print(None)
