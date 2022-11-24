from . import views
from django.urls import path


urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('slug:slug/', views.BuildDetail.as_view(), name='post_detail'),
]
