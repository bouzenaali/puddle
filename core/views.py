from django.shortcuts import render

from item.models import Category, Item

def index(request):
    Items = Item.objects.filter(is_sold = False)[0:6]
    Categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'Categpries' : Categories,
        'items' : Items,
    })

def contact(request):
    return render(request, 'core/contact.html')
