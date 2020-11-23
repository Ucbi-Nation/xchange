from django.urls import path

from .views import index, aaa, rates,about,blog

urlpatterns = [
    path('', index, name='index'),
    path('aaa', aaa, name='aaa'),
    path('rates/', rates, name='rates'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
]