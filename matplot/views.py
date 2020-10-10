
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render





@csrf_exempt
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def add(request):

    return render(request)


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

