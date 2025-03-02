
from django.contrib import admin
from django.urls import path,include

from configapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include("configapp.urls")),
    path('',index,name='home')
]
