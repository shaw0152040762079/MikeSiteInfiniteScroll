import base64
import io
import os
import this
import urllib
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pandas_datareader import data
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render



def experiment(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'experiment.html', {'numbers': numbers})


@csrf_exempt
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def add(request):
    # TODO make the top nav make sense fuckface
    # TODO read up on CSS standalone classes for good practice
    crypto = request.GET['crypto']
    background = request.GET['back']
    type = request.GET['chart']
    crypto = crypto + '-USD'

    average = request.GET['rolling average']

    # Start datareader parse at 120 days ago
    startparse_ = datetime.today() - timedelta(days=int(120))

    # Use today
    endparse_ = datetime.today()

    plt.style.use(background)

    crypto_data_frame = data.DataReader(crypto, 'yahoo', startparse_, endparse_)

    if type == 'Moving Average':
        crypto_data_frame['Close'].loc[startparse_:endparse_].rolling(window=int(average)).mean().plot(
            label='Moving Average 10 rolling')

    crypto_data_frame['Close'].loc[startparse_:endparse_].plot(label=crypto + ' Price')

    plt.title("Your data plotted")
    fig = plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'result.html', {'data2': uri})


self.arts = ''


def art(request):
    from matplot import Reddit
    reddit = Reddit.Reddit()

    urls = []

    for i in range(4):
        url1 = str((Reddit.redditimage(Reddit.getartUrls(), len(Reddit.getartUrls()) - 1)))
        data_type = url1[-4:]

        while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
            url1 = str((Reddit.redditimage(Reddit.getartUrls(), len(Reddit.getartUrls()) - 1)))
            data_type = url1[-4:]

        urls += "<ol> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </ol> "

    for i in range(len(urls)):
        self.arts += urls[i]

    return render(request, 'art.html', {'art': self.arts})


self.memes = ''


def meme(request):
    from matplot import Reddit
    reddit = Reddit.Reddit()
    urls = []

    for i in range(4):
        url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
        data_type = url1[-4:]

        while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
            print(url1)
            url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
            data_type = url1[-4:]

        urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "

    for i in range(len(urls)):
        self.memes += urls[i]

    return render(request, 'meme.html', {'memes': self.memes})


# Create your views here.

self.ensemble = ''


def story(request):
    from matplot import Reddit
    reddit = Reddit
    stories = []
    _story = "<li>" + str(Reddit.copypasta()) + "</li> <br>"
    stories += _story

    for i in range(len(stories)):
        self.ensemble += stories[i]

    return render(request, 'story.html', {'story': self.ensemble})


def definitions(request):
    return render(request, 'definitions.html')
