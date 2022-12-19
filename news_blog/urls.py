from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('posts', views.CommentsViewSet)

urlpatterns = [
    path('posts/', views.PostsListCreateView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostsRetrieveUpdateDestroyAPIView.as_view(), name='posts_detail'),
    path('comments/', include(router.urls)),
]