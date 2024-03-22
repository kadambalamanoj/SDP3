from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from.views import *
urlpatterns = [
path('add_review/',add_review,name='add_review'),
path('review_list/',review_list,name='review_list'),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)