from django.test import TestCase

# Create your tests here.
import os

from matplot import Reddit

reddit = Reddit.Reddit()
print(reddit.memeUrls)
print(url1 = str((Reddit.redditimage(reddit.memeUrls, len(reddit.memeUrls) - 1))))

