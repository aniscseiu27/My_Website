from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from newsletter.models import Post

from . import views

urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                              template_name="home.html")),
                 url(r'(?P<pk>\d+)$',  DetailView.as_view(model=Post,
                 	                      template_name='home.html')),
               
               url(r'^list/$', "newsletter.views.post_list", name="list"),
               url(r'^create/$', "newsletter.views.post_create"),
               url(r'^(?P<id>\d+)/$', "newsletter.views.post_detail", name="detail"),
               url(r'^(?P<id>\d+)/edit/$', "newsletter.views.post_update", name="update"),
               url(r'^(?P<id>\d+)/delete/$', "newsletter.views.post_delete"),

               url(r'^success/$', "newsletter.views.contact_success", name="success")
               ]
