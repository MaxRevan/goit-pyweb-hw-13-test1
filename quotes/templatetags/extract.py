from bson.objectid import ObjectId
from django import template
from ..utils import get_mongodb

register = template.Library()

@register.filter(name='author')
def get_author(id_):
    db = get_mongodb()
    author = db.author.find_one({'_id': ObjectId(id_)})
    return author['author'] if author else "Невідомий автор"


register.filter('author', get_author)

