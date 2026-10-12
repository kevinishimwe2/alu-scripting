#!/usr/bin/python3
"""Module that recursively counts keywords in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None, weights=None):
    """Print a sorted count of keywords found in hot post titles."""
    if weights is None:
        weights = {}
        for word in word_list:
            key = word.lower()
            weights[key] = weights.get(key, 0) + 1
        counts = {}
    if not subreddit or not isinstance(subreddit, str):
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return
        data = res.json().get("data", {})
    except (requests.RequestException, ValueError):
        return
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in weights:
                counts[token] = counts.get(token, 0) + weights[token]
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts, weights)
    for word, num in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, num))
