from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly, )

from api.permissions import IsOwnerOrAuthorizedOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer, )
from posts.models import Follow, Group, Post


class GetPostViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    """
    (GET, POST): получаем список всех постов или создаём новый пост.
    (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAuthorizedOrReadOnly, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    (GET): получаем список всех групп.
    (GET): получаем информацию о группе по id
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CommentViewSet(viewsets.ModelViewSet):
    """
    (GET, POST): получаем список всех комментариев поста с id=post_id или
    создаём новый, указав id поста, который хотим прокомментировать.
    (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий
    по id у поста с id=post_id.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrAuthorizedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(
                Post,
                id=self.kwargs.get(
                    "post_id")
            )
        )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()


class FollowViewSet(GetPostViewSet):
    """
    (GET, POST): получаем список всех подписок автора или
    делем новую подписку на автора
    """
    serializer_class = FollowSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['=user__username', '=following__username', ]

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
