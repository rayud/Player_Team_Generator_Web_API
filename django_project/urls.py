from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    re_path(r'^', include('my_app.urls')),
    re_path(r'^admin/', admin.site.urls)
]
