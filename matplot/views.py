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

    # Get random images from reddit related to art
    posts = Reddit.reddit_imager(Reddit.Reddit.art_urls, len(Reddit.Reddit.art_urls) - 1)
    for post in posts:
        data_type = post.url[-4:]
        # Check to make sure they are images
        if '.jpg' == data_type or '.png' == data_type or '.gif' == data_type:
            arts += "<li> <img src =  '" + str(post.url) + " ' alt='no image' height '600' width= '465'> </li> "

    # Save the arts objects in a session object so that when refreshing happens they remain in a session object
    request.session['arts'] = arts
    request.session.modified = True
    return render(request, 'art.html', {'art': arts})



