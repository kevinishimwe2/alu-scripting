#!/usr/bin/python3
"""Module to query Reddit API recursively and count keywords in titles."""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_counts=None):
    """Recursively query Reddit API and count keywords in hot article titles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        hot_list (list): List to accumulate titles.
        after (str): Pagination token.
        word_counts (dict): Dictionary to store word counts.

    Returns:
        dict: Dictionary of word counts or None if invalid subreddit.
    """
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            word_counts[word.lower()] = 0

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
            title = child.get("data").get("title").lower()
            words = title.split()
            for word in words:
                clean_word = word.strip('.,!?_')
                if clean_word in word_counts:
                    word_counts[clean_word] += 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, hot_list, after, word_counts)

        # Filter out words with zero count
        filtered_counts = {k: v for k, v in word_counts.items() if v > 0}

        # Sort by count descending, then alphabetically ascending
        sorted_counts = sorted(filtered_counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

        return word_counts
    except (AttributeError, ValueError):
        return None
