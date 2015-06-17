from django.shortcuts import render, RequestContext
from pymongo import MongoClient

# Create your views here.

def init_mongo(database,collection):
    connect = MongoClient('localhost', 27017)#, max_pool_size=None)
    db = connect[database]
    global collect
    # collect = db.movie_list
    collect = db[collection]

def home(request):
    # news = News.objects.all()
    init_mongo('fc2_movie','movies')
    movies = collect.find()[1200:1300]
    return render_to_response('home.html',
                              locals(),
                              context_instance=RequestContext(request))
