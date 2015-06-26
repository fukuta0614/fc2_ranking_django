# -*- encoding:utf-8 -*-

from django.shortcuts import render, RequestContext,render_to_response,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pymongo import MongoClient
from collections import Counter
from bs4 import BeautifulSoup
import re,urllib2
import cPickle
from django.http import HttpResponse

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
    sort_type = request.GET.get('sort_type')
    init_mongo('fc2_movie','adult_movies')

    tags = []
    for movie in collect.find():
        tags.extend(movie['tag'])
    tags = Counter(tags).most_common(100)
    # with open('static/tags.pickle') as f:
    #     tags = cPickle.load(f)

    # five = [-2,-1,0,1,2]
    if sort_type == None:
        sort_type = 0
    else:
        sort_type = int(sort_type)
    # print(sort_type)
    # print(['fav','playing'][sort_type])
    if tag:
        movies = list(collect.find({'kind':'すべてのユーザー','tag':tag,'thumbnail':{'$exists':True}}).sort([(['fav','playing'][sort_type],-1)]))
    elif query:
        movies = list(collect.find({'kind':'すべてのユーザー','title':re.compile(query),'thumbnail':{'$exists':True}}).sort([(['fav','playing'][sort_type],-1)]))
    else:
        movies = list(collect.find({'kind':'すべてのユーザー','thumbnail':{'$exists':True}}).sort([(['fav','playing'][sort_type],-1)]))
    # with open('static/fc2_movies.pickle') as f:
    #     movies = cPickle.load(f)
    paginator = Paginator(movies, 100) # Show 25 contacts per page
    url = request.get_full_path()

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
    init_mongo('fc2_movie','adult_movies')
    target = request.GET.get('target')
    ginfo_url=collect.find({'_id':target})[0]['ginfo_url']
    soup = BeautifulSoup(urllib2.urlopen(ginfo_url,timeout=3).read())
    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url=ginfo_url,data=b'None',headers={'User-Agent':request.META['HTTP_USER_AGENT']})).read())
    # print(soup.string)
    filepath = str(soup).replace(";","").split("&amp")
    flv_url =  filepath[0].split('=')[1] + '?' + filepath[1]
    # flv_url =  filepath.split('&')[0].split('=')[1] + '?' + filepath.split('&')[1]


    if flv_url.startswith('http'):
        return redirect(flv_url)
    else:
        return redirect('/')