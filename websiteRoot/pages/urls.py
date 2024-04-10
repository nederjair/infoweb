from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('/contacts', views.contacts, {'pagename': 'contacts'}, name='home'),
    path('<str:pagename>', views.index, name='index'),
    ]
