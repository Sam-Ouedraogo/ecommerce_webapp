from django.shortcuts import render

from item.models import Category, Item

# Create your views here.

# show the newest 6 items
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all() # get all the categories
    
    
    return render(request, 'core/index.html', {
        'category': category, # These last 2 lines allow using the variable in the template. They point back to the predefined variables
        'items': items
    })


def contact (request):
    return render(request, 'core/contact.html')