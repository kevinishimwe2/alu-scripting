#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    if not subreddit or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return hot_list if hot_list else None
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list if hot_list else None
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
