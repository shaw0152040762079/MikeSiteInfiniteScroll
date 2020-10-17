from django.test import TestCase

# Create your tests here.
import os

from matplot import Reddit

reddit = Reddit.Reddit()
arts = ''
urls = []
if arts == '':
    for i in range(3):
        url1 = str((Reddit.reddit_image(Reddit.getartUrls2(), len(Reddit.getartUrls2()) - 1)))
        data_type = url1[-4:]
        # Check to make sure they are images
        if '.jpg' == data_type or '.png' == data_type or '.gif' == data_type:
            urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "
        # load all of the images to an HTML list
    # Add them to the arts list
    for i in range(len(urls)):
        arts += urls[i]

print(arts)
