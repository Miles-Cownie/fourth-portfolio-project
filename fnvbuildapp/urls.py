from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('<slug:slug>/', views.BuildDetail.as_view(), name='build_detail'),
    path('accounts/', include('allauth.urls')),
]
