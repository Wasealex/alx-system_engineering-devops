#!/usr/bin/python3
""" gets a top ten """
import requests


def top_ten(subreddit):
    """ """
    allpost = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10')

    if allpost.status_code >= 300:
        print('None')
    else:
        allresult = allpost.json()
        for posts in allresult.get("data").get("children"):
            print(posts.get("data").get("title"))
