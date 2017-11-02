from django.conf.urls import url
from . import views

app_name = 'homepage'
urlpatterns = [
    url(r'home/', views.home, name='home'),
    url(r'research/', views.research, name='research'),
    url(r'new/', views.new, name='new'),
    url(r'member/', views.member, name='member'),
    url(r'paper/', views.paper, name='paper'),
    url(r'paper_d/(?P<question_id>[0-9]+)/$', views.detail_paper, name='paper_detail'),
    url(r'author_d/(?P<question_id>[0-9]+)/$', views.detail_author, name='author_detail'),
    url(r'result_bib/$', views.download_bibtex, name='result_bibtex')
]