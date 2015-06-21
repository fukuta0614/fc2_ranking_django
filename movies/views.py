# -*- encoding:utf-8 -*-


from django.shortcuts import render, RequestContext,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pymongo import MongoClient
from django import template
from collections import Counter
import re
register = template.Library()

@register.filter(name='private')
def private(obj, attribute):
    return getattr(obj, attribute)

# Create your views here.

def init_mongo(database,collection):
    connect = MongoClient('localhost', 27017)#, max_pool_size=None)
    db = connect[database]
    global collect
    # collect = db.movie_list
    collect = db[collection]

def home(request):
    # news = News.objects.all()
    page = request.GET.get('page')
    tag = request.GET.get('tag')
    query = request.GET.get('query')
    init_mongo('fc2_movie','movies_non_adult')

    tags = []
    for movie in collect.find():
        tags.extend(movie['tag'])
    tags = Counter(tags).most_common(100)
    five = [-2,-1,0,1,2]
    if tag:
        movies = list(collect.find({'kind':'すべてのユーザー','tag':tag}).sort([('fav',-1)]))
    elif query:
        movies = list(collect.find({'kind':'すべてのユーザー','title':re.compile(query)}).sort([('fav',-1)]))
    else:
        movies = list(collect.find({'kind':'すべてのユーザー'}).sort([('fav',-1)]))
    paginator = Paginator(movies, 100) # Show 25 contacts per page

    print(request.META['HTTP_USER_AGENT'])

    if page:
        num = (int(page) - 1 ) * 100
    else:
        num = 0
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)

    return render_to_response('home.html',
                              locals(),
                              context_instance=RequestContext(request))

def download(request):
    if request.GET.get('20150225qFpqAs3t'):
        print('asdf')

    return render_to_response('home.html',
                              locals(),
                              context_instance=RequestContext(request))

