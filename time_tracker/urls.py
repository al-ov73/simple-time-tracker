from django.contrib import admin
from django.urls import path

from time_tracker import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/task/', views.TaskStatus.as_view(), name='task_status'),
    path('', views.TaskView.as_view(), name='index'),
]
