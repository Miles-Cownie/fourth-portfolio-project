from . import views
from django.urls import path


urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('<slug:slug>/', views.BuildDetail.as_view(), name='build_detail'),
    path('like/<slug:slug>', views.BuildLike.as_view(), name='build_like'),
]
