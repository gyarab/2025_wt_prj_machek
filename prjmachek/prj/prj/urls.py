from django.contrib import admin
from django.urls import path
from prj.api import api  # přidej tento import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # přidej tento řádek
]
