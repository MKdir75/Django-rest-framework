from django.urls import path, include
from .views import PostsView, posts_detail, PostsAPIView, postDetailsAPIView, genericAPIView, postViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('posts', postViewSet, basename='posts')



urlpatterns = [
    #path('posts/', PostsView),
    #path('details/<int:pk>', posts_detail)

    #path('postsAPIView/', PostsAPIView.as_view()),
    #path('detailsAPIView/<int:pk>',postDetailsAPIView.as_view())

    path('genericAPIView/<int:id>/', genericAPIView.as_view()),
    path('', include(router.urls))
]