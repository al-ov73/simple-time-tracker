from django.contrib import admin
from django.urls import path

from time_tracker import views
from django.urls import path

from rest_framework.routers import DefaultRouter


# router = DefaultRouter(trailing_slash=True)

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskView.as_view(), name='index'),
]
# urlpatterns.extend([
#     path('', views.TaskSerializerView.as_view(), name='index'),
# ])