from django.conf.urls import url
from . import views

app_name = 'tree_view'
urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'embedding/', views.embedding, name='embedding'),
]