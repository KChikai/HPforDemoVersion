from django.conf.urls import url
from . import views

app_name = 'homepage'
urlpatterns = [
    # ja
    url(r'ja/home/', views.home, name='home'),
    url(r'ja/research/', views.research, name='research'),
    url(r'ja/new/', views.new, name='new'),
    url(r'ja/member/', views.member, name='member'),
    url(r'ja/paper/', views.paper, name='paper'),

    # en
    url(r'en/home/', views.home_en, name='home_en'),
    url(r'en/research/', views.research_en, name='research_en'),
    url(r'en/new/', views.new_en, name='new_en'),
    url(r'en/member/', views.member_en, name='member_en'),
    url(r'en/paper/', views.paper_en, name='paper_en'),

    # common
    url(r'paper_d/(?P<question_id>[0-9]+)/$', views.detail_paper, name='paper_detail'),
    url(r'author_d/(?P<question_id>[0-9]+)/$', views.detail_author, name='author_detail'),
    url(r'result_bib/$', views.download_bibtex, name='result_bibtex')
]