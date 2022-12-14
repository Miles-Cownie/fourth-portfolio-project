from . import views
from django.urls import path


urlpatterns = [
    path('', views.BuildList.as_view(), name='home'),
    path('<slug:slug>/', views.BuildDetail.as_view(), name='build_detail'),
    path('like/<slug:slug>', views.BuildLike.as_view(), name='build_like'),
    path('characterbuild_form/add/',
         views.CharacterBuildCreate.as_view(), name='author-add'),
    path('characterbuild_form/edit/<slug:slug>',
         views.CharacterBuildUpdate.as_view(), name='author-edit'),
    path('characterbuild_confirm_delete/<slug:slug>',
         views.CharacterBuildDelete.as_view(), name='author-delete'),
]
