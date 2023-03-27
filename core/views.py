from django.shortcuts import redirect, render
from item.models import Category, Item
from .forms import SignUpForm


def index(request):
    Items = Item.objects.filter(is_sold = False)[0:6]
    Categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'Categories' : Categories,
        'items' : Items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })