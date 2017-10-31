from django.conf.urls import url
from . import views

app_name = 'tree_view'
urlpatterns = [
    url(r'embedding/', views.embedding, name='embedding'),
    url(r'research/', views.research, name='research'),
    url(r'new/', views.new, name='new'),
    url(r'member/', views.member, name='member'),
]