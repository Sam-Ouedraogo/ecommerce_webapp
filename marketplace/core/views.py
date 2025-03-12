from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html',{
        'form': form
    })