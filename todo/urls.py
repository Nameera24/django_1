
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myapp1/', include('myapp1.urls')),
    
    path('admin/', admin.site.urls),
]
