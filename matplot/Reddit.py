import json
import urllib
import random
from typing import Dict, Any, Union

import praw as praw
from self import self


import os


class Reddit(object):
    self.reddit = praw.Reddit(client_id=os.environ('client_id'), client_secret=os.environ['client_secret'],
                              user_agent=os.environ['user_agent'])

    self.posturl = ''

    def __init__(self):
        self.artUrls: Dict[Union[int, Any], Union[str, Any]] = {0: 'Portraitart',
                    1: 'Art',
                    2: 'painting',
                    3: 'PixelArt',
                    4: 'ArtHistory',
                    5: 'oilpainting',
                    6: 'DigitalPainting',
                    7: 'Watercolor',
                    8: 'low_poly',
                    9: 'VaporwaveAesthetics',
                    10: 'Gouache'}

        self.memeUrls = {0: 'dankmemes',
                     1: 'plantmemes',
                     2: 'chasersriseup',
                     3: 'comedyheaven'}






def getpost(url):
    submission = self.reddit.submission(url=url)
    return submission


def saveurl():
    return self.posturl


def geturlcopypasta():
    return self.urlcopypasta


def getartUrls():
    return self.artUrls


def getmemeUrls():
    return self.memeUrls


def copypasta():
    sub = self.reddit.subreddit('copypasta')

    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 19)
    random_post = posts[random_post_number]
    self.posturl = random_post.url
    return random_post.selftext


def redditimage(urlKeytoValue, urlnum):
    urlkey = random.randint(0, urlnum)
    # create random number to decide which image pulled from array
    url = (urlKeytoValue[urlkey])
    sub = self.reddit.subreddit(url)

    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 19)
    random_post = posts[random_post_number]
    self.posturl = random_post.url
    return random_post.url


def fetch():
    reddit = praw.Reddit(client_id='mJsxJuhrpiWMrw', client_secret='Noarg0lqItC2a7hvDe_8pxbgVLc', user_agent='cry.bot')
    sr = reddit.subreddit("pewdiepiesubmissions").random()
    if not sr.is_self:  # We only want to work with link posts
        slink = sr.url


# Take a url dictionary of reddit.json links and the size of it returns the image of a random post from one of 8
# random posts in the hot section
def reddit_image(urlKeytoValue, urlnum):
    urlkey = random.randint(0, urlnum)
    # create random number to decide which image pulled from array
    imagekey = random.randint(0, 8)
    # Problems occur when not making the http request through mozilla
    req = urllib.request.Request(urlKeytoValue[urlkey], headers={'User-Agent': 'Mozilla/5.0'})
    aesthetica = json.loads(urllib.request.urlopen(req).read())
    return aesthetica['data']['children'][imagekey]['data']['url_overridden_by_dest']


def reddit_text(urlkeytovalue, urlnum):
    d = {1: 'hot', 0: 'new'}
    urlkey = random.randint(0, urlnum)
    copypasta_key = random.randint(0, 15)
    copypasta_hot_or_not = random.randint(0, 1)
    actualurlcopypasta = urlkeytovalue[urlkey] + d[copypasta_hot_or_not] + ".json"
    req = urllib.request.Request(actualurlcopypasta, headers={'User-Agent': 'Mozilla/5.0'})
    json_text = json.loads(urllib.request.urlopen(req).read())
    return json_text['data']['children'][copypasta_key]['data']['selftext']
