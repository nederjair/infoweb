from django.shortcuts import render
from .models import Page
from .models import Contact

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'image': pg.image,
        'height': pg.height,
        'width': pg.width,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        }
    return render(request, 'pages/home.html', context)

def contacts(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    cont = Contact.objects.all()
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'contact_list': Contact.objects.all()
        }
    return render(request, 'pages/contact.html', context)
