from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')), 

    path('api/auth/', include('djoser.urls')),  
    path('api/auth/', include('djoser.urls.authtoken')), 
    path('api/auth/', include('djoser.urls.jwt')), 
]

