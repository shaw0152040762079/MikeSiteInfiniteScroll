import base64
import io
import os
import urllib
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pandas_datareader import data
from self import self

from .forms import NameForm
from .models import Company


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})


@csrf_exempt
def home(request):
    from matplot import Reddit
    import requests
    reddit = Reddit
    url = (Reddit.redditimage(reddit.getmemeUrls(), len(reddit.getmemeUrls()) - 1))
    from PIL import Image
    import requests
    from io import BytesIO
    import base64
    from django.core.files import File

    output = BytesIO()

    response = requests.get(url)

    reopen = open

    with open("sample_image", "wb") as f:
        f.write(response.content)

    reopen = open("sample_image", "rb")
    django_file = File(reopen)

    revsys = Company()
    entrys = Company.objects.all()
    entrys.delete
    blog = Company.objects.all()

    import shutil
    shutil.rmtree('media')
    revsys.name = "Revolution Systems"
    revsys.logo.save("meme.jpg", django_file, save=True)

    return render(request, 'home.html', {'data': url})


@csrf_exempt
def add(request):
    # TODO make the top nav make sense fuckface
    # TODO read up on CSS standalone classes for good practice
    crypto = request.GET['crypto']
    background = request.GET['back']
    type = request.GET['chart']
    crypto = crypto + '-USD'

    # Start datareader parse at 120 days ago
    startparse_ = datetime.today() - timedelta(days=int(120))

    # Use today
    endparse_ = datetime.today()

    plt.style.use(background)

    crypto_data_frame = data.DataReader(crypto, 'yahoo', startparse_, endparse_)

    if (type == 'Moving Average'):
        crypto_data_frame['Close'].loc[startparse_:endparse_].rolling(window=int(10)).mean().plot(
            label='Moving Average 10 rolling')

    crypto_data_frame['Close'].loc[startparse_:endparse_].plot(label=crypto + ' Price')

    plt.title("ff")
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
    reddit = Reddit
    urls = []
    url1 = str((Reddit.redditimage(reddit.getartUrls(), len(reddit.getartUrls()) - 1)))
    data_type = url1[-4:]

    while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
        url1 = str((Reddit.redditimage(reddit.getartUrls(), len(reddit.getartUrls()) - 1)))
    urls += "<ol> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </ol> "

    for i in range(len(urls)):
        self.arts += urls[i]

    return render(request, 'art.html', {'art': self.arts})


self.memes = ''


def meme(request):
    from matplot import Reddit
    reddit = Reddit
    urls = []
    url1 = str((Reddit.redditimage(reddit.getmemeUrls(), len(reddit.getmemeUrls()) - 1)))
    data_type = url1[-4:]

    while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
        print(url1)
        url1 = str((Reddit.redditimage(reddit.getmemeUrls(), len(reddit.getmemeUrls()) - 1)))

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
    story = "<li>" + str(reddit.copypasta()) + "</li> <br>"
    stories += story

    for i in range(len(stories)):
        self.ensemble += stories[i]

    return render(request, 'story.html', {'story': self.ensemble})
