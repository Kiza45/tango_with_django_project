from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    #Note they key boldmessage matches to {{ boldmessage }} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function  ot make out lives easier.
    #Note that the first parameter is the template we wish to use

    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html')
    #context=context_dict)
