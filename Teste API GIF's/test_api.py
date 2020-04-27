import json
import requests

# set the apikey and limit
apikey = "LIVDSRZULELA"  
# test value
lmt = 2

# our test search
search_term = "HACKER"

# get the top 8 GIFs for the search term
r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    #context 
    gifs = json.loads(r.content)
    #print(gifs)
    #print(gifs['next'])
    i = 0
    a = gifs['results']
    #print(a[0])
    #print(a[1])
    context = {}
    while (i < int(gifs['next'])):
        #print(a[i])
        #b = a[i]
        #print(b)
        #print(a[i]['id']) # print ok
        #print(a[i]['title']) # print ok
    
        b = a[i]['media']
        #d = c[i]
        #print(b[0]['gif']['url']) # print ok

        j = a[i]['id']
        context[j] = {'id': a[i]['id'], 'title' : a[i]['title'], 'url': b[0]['gif']['url']}
        

        i = i + 1
    
    response = context
    print(response.keys())
    """
    for res in response:
        print(response[res]['id'])
        print(response[res]['title'])
        print(response[res]['url'])

    i = 0
    while (i < len(response)):
        print(response[i]['id'])
        print(response[i]['title'])
        print(response[i]['url'])
        i = i + 1
    """
    
else:
    top_8gifs = None