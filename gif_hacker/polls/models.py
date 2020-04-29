from django.db import models
import requests
import json


# Create your models here.

class Vote (models.Model):
    id_gif = models.CharField(max_length=200)
    # vote_type: UP/DOWN 
    vote_type = models.CharField(max_length=200)

    def total_votos (self, id_gif):
        v = Vote.objects.filter(id_gif__exact=id_gif).count()
        return v

    def total_votos_up (self, id_gif):
        v = Vote.objects.filter(id_gif__exact=id_gif, vote_type__exact="UP").count()
        return v
    
    def total_votos_down (self, id_gif):
        v = Vote.objects.filter(id_gif__exact=id_gif, vote_type__exact="DOWN").count()
        return v
    
    def ordenar (self, describe):
        votes = Vote.objects.all()
    
        # Carregamento/vinculação dos votos registrados na database aos gifs extraídos da API

        for vote in votes:
            for d in describe:
                if (vote.id_gif == d['id']):
                    d['votos_total'] = Vote.total_votos(self=0, id_gif=vote.id_gif)
                    d['votos_up'] = Vote.total_votos_up(self=0, id_gif=vote.id_gif)
                    d['votos_down'] = Vote.total_votos_down(self=0, id_gif=vote.id_gif)
        
        sorted_describe = sorted(describe, key = lambda y : (-y.get('votos_up', 0), y.get('votos_down', 0)))
        
        return sorted_describe
    
    def request (self, apikey, lmt, search_term):
        # Requisição GET para carregar os gifs 
        response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=minimal&ar_range=wide" % (search_term, apikey, lmt))

        if response.status_code == 200:
            # Carrega os gifs, reparte o json em partes úteis e gera um novo json somente com as informações necessárias. 
            result = json.loads(response.text)
            describe = result['results']
        else:
            return 404
        
        return describe