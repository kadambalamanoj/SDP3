from django.contrib import admin
from django.urls import path
from.views import *
from . import views
urlpatterns = [
    # path("Manoj/", hello1),
    path('',newhomepage,name='newhomepage'),
    path('travel/',travelpackage,name='travelpackage'),
    path('p/',print1,name='print1'),
    path('console/',printtoconsole,name='printtoconsole'),
    path('r/', random1, name='random1'),
    path('rand1/',random123,name='random123'),
    path('dt/',getdate1,name='getdate1'),
    path('d/',get_date,name='get_date'),
    path('tm/',tzcall,name='tzcall'),
    path('dm/',registerloginfunction,name='registerloginfunction'),
    path('da/',database,name='database'),
    path('pi/',pie_chart,name='pi'),
    path('pic/',piecal,name='piecal'),
    path('mt/',my,name='my'),
    path('w/',weatherlogic,name='weatherlogic'),
    path('wh/',weathe,name='wh'),
    # path('signup',views.sign,name='signup'),
    # path('login',views.log,name='login'),
    path('login/',login,name="login"),
    path('signup/',sinup,name="signup"),
    path('login1/',login1,name="login1"),
    path('signup1/', sinup1, name='signup1'),
    path('logout/',logout,name='logout'),
    path('ca/',ca,name='ca'),
    path('contactmail/',contactmail,name='contactmail'),
    path('ma',views.sentmail,name='ma'),
    path('short_url',views.url_shortener,name='short_url'),
    path('ssa/<str:short_url>/', views.redirect_to_original, name='ssa'),

    # path('login1/',login1,name='login1'),
#    path('signup1/',signup1,name='signup1'),
#    path('logout/',logout,name='logout'),


]