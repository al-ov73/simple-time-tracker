from django.contrib import admin
from django.urls import path

from time_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskView.as_view(), name='index'),
]
