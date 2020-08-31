from django.contrib import admin
from django.urls import path,include
from check_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('check_app.urls')),
]
