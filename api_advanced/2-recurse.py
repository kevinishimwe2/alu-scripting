#!/usr/bin/python3
"""Module to query Reddit API recursively and get all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query Reddit API and return list of hot article titles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to accumulate titles.
        after (str): Pagination token.

    Returns:
        list: List of hot article titles or None if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data")
        children = data.get("children")

        for child in children:
            hot_list.append(child.get("data").get("title"))

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except (AttributeError, ValueError):
        return None
