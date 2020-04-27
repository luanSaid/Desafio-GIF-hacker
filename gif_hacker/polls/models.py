from django.db import models

# Create your models here.

class Vote (models.Model):
    id_gif = models.CharField(max_length=200)
    # vote_type: UP/DOWN 
    vote_type = models.CharField(max_length=200)

    def query_vote_types(self):
        return self.vote_type
    
    def query_id_gif(self):
        return self.id_gif