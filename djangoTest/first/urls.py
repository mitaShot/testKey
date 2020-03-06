from django.urls import path, re_path

from . import views
from djangoTest import urls
from django.urls.conf import include


urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('result/', views.result, name="result"),
    #re_path(r'^select/(?P<year>[0-9]{4}/$')
    path('second/', include('second.urls'), name='secondIndex'),
]