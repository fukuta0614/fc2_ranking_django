
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from movies.models import Movie,Tag
from collections import Counter

movies = Movie.objects.values()

tags = []
for movie in movies:
    tags.extend(movie['tag'].split(','))
tags = Counter(tags).most_common(1000)
for tag in tags:
    tag = {'tag':tag[0],'num':tag[1]}
    Tag(**tag).save()