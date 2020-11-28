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

    # Get random images from reddit related to art
    posts = Reddit.redditimager(Reddit.Reddit.artUrls, len(Reddit.Reddit.artUrls) - 1)
    for i in range(19):
        data_type = posts[i].url[-4:]
        # Check to make sure they are images
        if '.jpg' == data_type or '.png' == data_type or '.gif' == data_type:
            print(posts[i].url)
            urls += "<li> <img src =  '" + str(posts[i].url) + " ' alt='no image' height '600' width= '465'> </li> "

    # Add them to the arts list
    for i in range(len(urls)):
        arts += urls[i]
    # Save the arts objects in a session object so that when refreshing happens they remain in a session object
    request.session['arts'] = arts
    request.session.modified = True
    return render(request, 'art.html', {'art': arts})



