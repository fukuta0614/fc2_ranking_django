# -*- encoding:utf-8 -*-

from django.shortcuts import render, RequestContext,render_to_response,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import Counter
from bs4 import BeautifulSoup
from movies.models import Movie,Tag
import re,urllib2
import cPickle
from django.http import HttpResponse

def home(request):
    page = request.GET.get('page')
    tag = request.GET.get('tag')
    query = request.GET.get('query')
    sort_type = request.GET.get('sort_type')


    tags = Tag.objects.all()[:100]

    if sort_type == None:
        sort_type = 0
    else:
        sort_type = int(sort_type)
    if tag:
        movies = Movie.objects.filter(tag__contains=tag)
    elif query:
        movies = Movie.objects.filter(title__contains=query)
    else:
        movies = Movie.objects.all()
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
    target = request.GET.get('target')
    ginfo_url=Movie.objects.get(id=target).ginfo_url
    # soup = BeautifulSoup(urllib2.urlopen(ginfo_url,timeout=3).read())
    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url=ginfo_url,data=b'None',headers={'User-Agent':request.META['HTTP_USER_AGENT']})).read())
    # print(soup.string)
    filepath = str(soup).replace(";","").split("&amp")
    flv_url =  filepath[0].split('=')[1] + '?' + filepath[1]
    # flv_url =  filepath.split('&')[0].split('=')[1] + '?' + filepath.split('&')[1]


    if flv_url.startswith('http'):
        return redirect(flv_url)
    else:
        return redirect('/')