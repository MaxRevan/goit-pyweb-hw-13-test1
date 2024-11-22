from django.urls import path
from .views import add_author, add_quote, user_quotes_list, author_details_user

app_name = 'content'

urlpatterns = [
    path('add-author/', add_author, name='add_author'),
    path('add-quote/', add_quote, name='add_quote'),
    path('user-quotes/', user_quotes_list, name='user_quotes_list'),
    path('user-author/<str:id_>/', author_details_user, name='author_details_user'),
]
