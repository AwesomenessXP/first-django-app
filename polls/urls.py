from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #ex: /polls/
    path('', views.index, name='index'), #index is a new view
    #ex: /polls/5/
    #what it looks like:
    #detail(request=<HttpRequest object>, question_id=34)
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # #ex: /polls/5/test/
    # path('<int:question_id>/test/', views.test, name='test'),
    # #ex: /polls/5/another/
    # path('<int:someNum>/another/', views.anotherTest, name='another')
]