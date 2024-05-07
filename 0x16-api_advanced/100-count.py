#!/usr/bin/python3
""" gets sorted count of given keywords"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, count=Counter()):
    """ returns count"""
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json")

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if len(posts) == 0:
            return None

        for post in posts:
            title = post["data"]["title"].lower()
            words = title.split()
            count.update(words)

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after=after, count=count)
        else:
            filtered_count = {word: count[word]
                              for word in word_list if count[word] > 0}
            sorted_count = sorted(filtered_count.items(),
                                  key=lambda x: (-x[1], x[0]))
            for word, count in sorted_count:
                print(f"{word}: {count}")
    else:
        return None
