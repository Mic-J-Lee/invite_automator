# add this on top
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parseandrequest/', include('parseandrequest.urls')),
]