from django.http import HttpResponse
from django.shortcuts import render
from .models import Vote
import requests
import json

def index(request):
    # set the apikey and limit
    apikey = "LIVDSRZULELA"  
    # test value
    lmt = 3
    # our test search
    search_term = "HACKER"

    # get the top 20 GIFs for the search term
    response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
    if response.status_code == 200:
        # Carrega os gifs, reparte o dict em partes úteis e gera um novo dict somente com as informações necessárias. 
        gifs = json.loads(response.content)
        i = 0
        a = gifs['results']
        context = {}
        while (i < int(gifs['next'])):
            if (a[i]['title'] == ''):
                a[i]['title'] = 'teste'

            b = a[i]['media']
            #j = a[i]['title']
            j = a[i]['title']
            context[i] = {'id': a[i]['id'], 'titulo' : a[i]['title'], 'url': b[0]['gif']['url']}
            i = i + 1
    else:
        return 404
    context = {'gifs': context}
    return render(request, 'polls/index.html', context)
    

def detail(request, id_gif):
    return HttpResponse("You're looking at question %s." % id_gif)

def results(request, id_gif):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id_gif)

def vote(request, id_gif):
    return HttpResponse("Você está votando  no GIF %s." % id_gif)