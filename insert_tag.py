
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from movies.models import Movie,Tag
from collections import Counter
from pymongo import MongoClient

def init_mongo(database,collection):
        connect = MongoClient('localhost', 27017)#, max_pool_size=None)
        db = connect[database]
        global collect
        # collect = db.movie_list
        collect = db[collection]


init_mongo('fc2_movie','movies_non_adult')
for i,movie in enumerate(collect.find({},{'rate':0,'flv_url':0,'kind':0})):
    print(i)
    movie['id']=movie.pop('_od')
    movie['tag'] = ','.join(movie['tag'])
    Movie(**movie).save()

movies = Movie.objects.values()

tags = []
for movie in movies:
    tags.extend(movie['tag'].split(','))
tags = Counter(tags).most_common(1000)
for tag in tags:
    tag = {'tag':tag[0],'num':tag[1]}
    Tag(**tag).save()