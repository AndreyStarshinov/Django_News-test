from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news_page/', index, name='news_page')
]
