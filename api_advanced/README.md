# API advanced

## Description
This project explores the Reddit API: querying endpoints with no
authentication required, handling pagination, recursively gathering
results across multiple pages, and parsing/sorting JSON data.

## Requirements
- Python 3.4.3 on Ubuntu 14.04 LTS
- PEP 8 style
- All files start with `#!/usr/bin/python3`
- All files end with a new line
- All files are executable
- Uses the `requests` module for all HTTP calls
- Sets a custom `User-Agent` header and disables redirect-following
  (`allow_redirects=False`) so invalid subreddits (which Reddit
  redirects to a search page) are correctly detected as invalid
  instead of silently succeeding.

## Files

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` — returns subscriber count, or `0` if invalid |
| `1-top_ten.py` | `top_ten(subreddit)` — prints the titles of the first 10 hot posts, or `None` if invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` — recursively paginates through all hot posts and returns a list of their titles, or `None` if invalid |
| `3-count.py` | `count_words(subreddit, word_list, word_count=None, after=None)` — recursively counts keyword occurrences across all hot post titles and prints a sorted count |

## Notes on `3-count.py`
- Matching is case-insensitive but exact: titles are split on
  whitespace and lowercased, so `java.`, `java!`, or `java_` will
  **not** match the keyword `java`.
- If the same keyword (case-insensitive) appears more than once in
  `word_list`, the final printed count for that keyword is the raw
  match count multiplied by how many times it was supplied
  (e.g. supplying `["JavA", "java"]` doubles the final count).
- Results are printed sorted by count (descending), then
  alphabetically (ascending) for ties. Keywords with zero matches
  are not printed.

## Author
Kevin Ishimwe Karagire