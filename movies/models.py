from django.db import models

class Movies(models.Model):
    id = models.CharField(max_length=120,primary_key=True)
    url = models.CharField(max_length=120,default='unknown')
    title = models.CharField(max_length=120,default='notitle')
    link = models.CharField(max_length=120,default='nolink')
    ginfo_url = models.CharField(max_length=120,default='unknown')
    playtime = models.CharField(max_length=120,default='unknown')
    thumbnail = models.CharField(max_length=120,default='unknown')
    fav = models.IntegerField()
    playing = models.IntegerField()


    def __str__(self):
        return self.title
