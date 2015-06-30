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
    is_adult = request.GET.get('is_adult')

    if sort_type == None or sort_type == 0:
        sort_type = 'fav'
    else:
        sort_type = 'playing'

    if is_adult is None:
        is_adult = 0
    else:
        is_adult = int(is_adult)

    tags = Tag.objects.filter(is_adult=is_adult).order_by('-num')[:100]

    if tag:
        movies = Movie.objects.filter(is_adult=is_adult).filter(tag__contains=tag).order_by('-{}'.format(sort_type))
    elif query:
        movies = Movie.objects.filter(is_adult=is_adult).filter(title__contains=query).order_by('-{}'.format(sort_type))
    else:
        movies = Movie.objects.filter(is_adult=is_adult).order_by('-{}'.format(sort_type))
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