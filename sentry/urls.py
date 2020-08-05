from django.contrib import admin
from django.urls import path
from core.views import posts

handler404 = 'core.views.custom_404_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', posts),
]
