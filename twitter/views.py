from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import feedparser
import BeautifulSoup
import urllib2

# Create your views here.

def parser(request,user):

    dicc = feedparser.parse('http://twitrss.me/twitter_user_to_rss/?user='+user)    
    salida = ""
    enlaces = []

    for index in range(5):
        salida += "<p><b>"+dicc.entries[index].title+"</b></p>"
        linea = dicc.entries[index].title
        lista = linea.split('https://')

        if len(lista)>1:
            enlaces.append(lista[1].split(' ')[0])
            enlaceHttp = "http://"+ enlaces[len(enlaces)-1].split('&')[0]
            salida += "<ol>"+enlaceHttp+"</ol>"
    
    return HttpResponse(salida)
