from django.http import HttpResponse, HttpResponseRedirect
from django.http import QueryDict
from django.shortcuts import render
from .models import Vote

def index (request):
    # Insira os paramêtros de busca (chave de acesso, limite e o termo de busca) para realizar a requisição na API TENOR
    describe = Vote.request(self=0, apikey="LIVDSRZULELA", lmt=20, search_term = "HACKER")
    
    if (describe == 404):
        message_error = 'Ocorreu um erro inesperado na busca pelos seus gifs, cheque as suas credencias de acesso a API em polls/views.py'
        return render(request, 'polls/index.html', message_error)
    else:
        # Vinculação das curtidas e Ordenação por número de curtidas
        describe = Vote.ordenar(self=0, describe=describe)

        context = {'describes': describe}
        return render(request, 'polls/index.html', context)

def like(request, id_gif):
    v = Vote(id_gif=id_gif, vote_type='UP')
    v.save()
    return index(request)

def deslike(request, id_gif):
    v = Vote(id_gif=id_gif, vote_type='DOWN')
    v.save()
    return index(request)