from django.conf.urls import url 
from . import views

urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
    url(r'^pictures/$',views.index,name = 'index')
]