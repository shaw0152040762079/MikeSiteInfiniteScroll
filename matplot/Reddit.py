import json
import urllib
import random
from typing import Dict, Any, Union

import praw as praw

import os


class Reddit(object):
    reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'],
                         user_agent=os.environ['user_agent'])

    posturl = ''

    art_urls: Dict[Union[int, Any], Union[str, Any]] = {0: 'Portraitart',
                                                        1: 'Art',
                                                        2: 'painting',
                                                        3: 'PixelArt',
                                                        4: 'ArtHistory',
                                                        5: 'oilpainting',
                                                        6: 'DigitalPainting',
                                                        7: 'Watercolor',
                                                        8: 'low_poly',
                                                        9: 'VaporwaveAesthetics',
                                                        10: 'Gouache',
                                                        11: 'RetroFuturism',
                                                        12: 'itookapicture',
                                                        13: 'museum',
                                                        14: 'AmateurRoomPorn',
                                                        15: 'retroanimeart',
                                                        16: 'vintagebookcovers',
                                                        17: 'ImaginaryFuturism',
                                                        18: 'PopArtNouveau',
                                                        19: 'ArchitecturePorn',
                                                        20: 'ArtNouveau',
                                                        21: 'ArtDeco',
                                                        22: 'brutalism',
                                                        23: 'EarthPorn',
                                                        24: 'AbstractArt',
                                                        25: 'CityPorn',
                                                        26: 'impressionism',
                                                        27: 'PopArt'}

    art_urls2: Dict[Union[int, Any], Union[str, Any]] = {0: 'https://www.reddit.com/r/portraitart.json',
                                                        1: 'https://www.reddit.com/r/Art.json',
                                                        2: 'https://www.reddit.com/r/painting.json',
                                                        3: 'https://www.reddit.com/r/PixelArt.json',
                                                        4: 'https://www.reddit.com/r/ArtHistory.json',
                                                        5: 'https://www.reddit.com/r/oilpainting.json',
                                                        6: 'https://www.reddit.com/r/DigitalPainting.json',
                                                        7: 'https://www.reddit.com/r/Watercolor.json',
                                                        8: 'https://www.reddit.com/r/low_poly.json',
                                                        9: 'https://www.reddit.com/r/VaporwaveAesthetics.json',
                                                        10: 'https://www.reddit.com/r/Gouache.json'}

    meme_urls = {0: 'dankmemes',
                1: 'plantmemes',
                2: 'chasersriseup',
                3: 'comedyheaven'}


def get_post(url):
    submission = reddit.submission(url=url)
    return submission


def save_url():
    return posturl


def get_url_copypasta():
    return urlcopypasta


def get_art_Urls2():
    artUrls2: Dict[Union[int, Any], Union[str, Any]] = {0: 'https://www.reddit.com/r/portraitart.json',
                                                        1: 'https://www.reddit.com/r/Art.json',
                                                        2: 'https://www.reddit.com/r/painting.json',
                                                        3: 'https://www.reddit.com/r/PixelArt.json',
                                                        4: 'https://www.reddit.com/r/ArtHistory.json',
                                                        5: 'https://www.reddit.com/r/oilpainting.json',
                                                        6: 'https://www.reddit.com/r/DigitalPainting.json',
                                                        7: 'https://www.reddit.com/r/Watercolor.json',
                                                        8: 'https://www.reddit.com/r/low_poly.json',
                                                        9: 'https://www.reddit.com/r/VaporwaveAesthetics.json',
                                                        10: 'https://www.reddit.com/r/Gouache.json'}
    return artUrls2


def getmemeUrls():
    memeUrls = {0: 'dankmemes',
                1: 'plantmemes',
                2: 'comedyheaven'}
    return memeUrls


def copypasta():
    reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'],
                         user_agent=os.environ['user_agent'])
    sub = reddit.subreddit('copypasta')

    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 19)
    random_post = posts[random_post_number]
    return random_post.selftext


def redditimage(urlKeytoValue, urlnum):
    reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'],
                         user_agent=os.environ['user_agent'])
    urlkey = random.randint(0, urlnum)
    # create random number to decide which image pulled from array
    url = (urlKeytoValue[urlkey])
    sub = reddit.subreddit(url)

    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 19)
    random_post = posts[random_post_number]
    return random_post.url


def reddit_imager(urlKeytoValue, urlnum):
    reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'],
                         user_agent=os.environ['user_agent'])
    urlkey = random.randint(0, urlnum)
    # create random number to decide which image pulled from array
    url = (urlKeytoValue[urlkey])
    sub = reddit.subreddit(url)

    posts = [post for post in sub.hot(limit=19)]

    return posts


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
