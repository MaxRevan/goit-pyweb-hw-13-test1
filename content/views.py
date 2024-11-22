from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from .models import Quote
from django.http import HttpResponseNotFound
from .models import Author

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content:add_quote')
    else:
        form = AuthorForm()
    return render(request, 'content/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user 
            quote.save()
            return redirect('content:user_quotes_list') 
    else:
        form = QuoteForm()
    return render(request, 'content/add_quote.html', {'form': form})

def user_quotes_list(request):
    user_quotes = Quote.objects.filter(user__isnull=False)
    return render(request, 'content/user_quotes_list.html', {'user_quotes': user_quotes})

def author_details_user(request, id_):
    try:
        author = Author.objects.get(pk=id_) 
        return render(request, 'content/author_details_user.html', {'author': author})
    except Author.DoesNotExist:
        return HttpResponseNotFound("Author not found")
    except ValueError:
        return HttpResponseNotFound("Invalid ID format")



