from django.shortcuts import render
from django.http import HttpResponse
#import category model
from rango.models import Category
from rango.models import Page

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    #Note they key boldmessage matches to {{ boldmessage }} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    
    #Return a rendered response to send to the client.
    #We make use of the shortcut function  ot make out lives easier.
    #Note that the first parameter is the template we wish to use

    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html')
    #context=context_dict)

def show_category(request, category_name_slug):
    #Create a dictionary which we can pass
    #to the template rendering engine
    context_dict = {}

    try:
        #Can we find a category name slug wiht thengiven name?
        #if we can't, the .get() method rasies a DoesNorExist exception
        #The .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)

        #Retrieve all of the associated pages
        #The filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
        
        #adds our results list to the template context under name pages
        context_dict['pages'] = pages

        # We also add the category object from
        # the database to the context dictionary
        # We'll use this in the template to verify that the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us
        context_dict['category'] = None
        context_dict['pages'] = None
        


    #Go render the response and return it to the client
    return render(request, 'rango/category.html', context=context_dict)
    
        
