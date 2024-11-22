from bson.objectid import ObjectId
from django.contrib.auth.models import User
from django.shortcuts import render
from .utils import get_mongodb
from django.core.paginator import Paginator

def main(request, page=1):
    db = get_mongodb()
    quotes_cursor = db['quote'].find()  
    quotes = list(quotes_cursor) 
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    #print(quotes)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def author_details(request, id_):
    db = get_mongodb()
    author = db['author'].find_one({'_id': ObjectId(id_)})
    if not author:
        return render(request, '404.html', status=404)
    return render(request, 'quotes/author_details.html', {'author': author})
