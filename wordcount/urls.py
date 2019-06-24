from django.contrib import admin
from django.urls import path

import count.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',count.views.home,name="home"),
    path('result/<int:text_id>/',count.views.result,name="result"),
    
    path('about/',count.views.about,name="about"),
    path('history/',count.views.history,name="history"),
    path('create/',count.views.create,name='create'),
]
