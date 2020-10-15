from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render


@csrf_exempt
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def add(request):
    return render(request)


def art(request):
    from matplot import Reddit
    # Check to see if previous arts object exists from last session
    if request.GET.get('Bored? Click to clear cache') == 'Bored? Click to clear cache':
        request.session['arts'] = ''
        request.session.modified = True

    arts = request.session.get('arts', '')
    urls = []
    if arts == '':
        for i in range(3):
            url1 = str((Reddit.redditimage(Reddit.getartUrls(), len(Reddit.getartUrls()) - 1)))
            data_type = url1[-4:]
            # Check to make sure they are images
            if '.jpg' == data_type or '.png' == data_type or '.gif' == data_type:
                urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "
            # load all of the images to an HTML list
        # Add them to the arts list
        for i in range(len(urls)):
            arts += urls[i]

    # Get random images from reddit related to art
    for i in range(12):
        url1 = str((Reddit.redditimage(Reddit.getartUrls(), len(Reddit.getartUrls()) - 1)))
        data_type = url1[-4:]
        # Check to make sure they are images
        if '.jpg' == data_type or '.png' == data_type or '.gif' == data_type:
            urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "

    # Add them to the arts list
    for i in range(len(urls)):
        arts += urls[i]
    # Save the arts objects in a session object so that when refreshing happens they remain
    request.session['arts'] = arts
    request.session.modified = True
    return render(request, 'art.html', {'art': arts})


def meme(request):
    from matplot import Reddit
    # Check to see if previous memes object exists from last session
    memes = request.session.get('memes', '')

    urls = []
    if memes == '':
        for i in range(8):
            url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
            data_type = url1[-4:]
            # Check to make sure they are images
            while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
                url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
                data_type = url1[-4:]
            # load all of the images to an HTML list
            urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "
        # Add them to the arts list
        for i in range(len(urls)):
            memes += urls[i]

    # Get random images from reddit related to art
    for i in range(3):
        url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
        data_type = url1[-4:]
        # Check to make sure they are images
        while '.jpg' != data_type and '.png' != data_type and '.gif' != data_type:
            url1 = str((Reddit.redditimage(Reddit.getmemeUrls(), len(Reddit.getmemeUrls()) - 1)))
            data_type = url1[-4:]
        # load all of the images to an HTML list
        urls += "<li> <img src =  '" + str(url1) + " ' alt='no image' height '600' width= '465'> </li> "
    # Add them to the arts list
    for i in range(len(urls)):
        memes += urls[i]
    request.session['memes'] = memes
    return render(request, 'meme.html', {'memes': memes})


# Create your views here.


def story(request):
    from matplot import Reddit
    reddit = Reddit
    if request.GET.get('Bored? Click to clear cache') == 'Bored? Click to clear cache':
        request.session['arts'] = ''
        request.session.modified = True
    ensemble = request.session.get('ensemble', '')


    stories = []
    _story = "<li>" + str(Reddit.copypasta()) + "</li> <br>"
    stories += _story

    for i in range(len(stories)):
        ensemble += stories[i]
    request.session['ensemble'] = ensemble

    return render(request, 'story.html', {'story': ensemble})
