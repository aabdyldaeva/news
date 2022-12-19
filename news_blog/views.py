from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets

from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer


class PostsListCreateView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
