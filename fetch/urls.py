from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short-url/', views.short_url, name='short_url'),
    path('long-url/', views.long_url, name='long_url'),
    path('long-urls/', views.long_urls, name='long_urls'),
    path('short-urls/', views.short_urls, name='short_urls'),
    path('count/', views.count, name='count'),

]
