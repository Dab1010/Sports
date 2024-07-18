from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sports/', include('sports.urls')),  # Include the sports app URLs
]
#url pattern 
from django.contrib import admin
from django.urls import path, include
from sports.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Add this line for the root URL
    path('sports/', include('sports.urls')),
]
