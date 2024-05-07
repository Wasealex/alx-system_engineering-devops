#!/usr/bin/python3
""" module that gets tittles of hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns the tilte for hot article"""
    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json")

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if len(posts) == 0:
            return None

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
    else:
        return None
