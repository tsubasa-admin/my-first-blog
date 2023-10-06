from django.urls import path

from nodolist.views import PostCreateView, PostDeleteView, PostTotalTimeView, PostUpdateView

from .views import PostListView, PostDetailView, TagListView, toppage

app_name = "nodolist"
urlpatterns = [
    path("", toppage, name="toppage"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("post_list/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("tag_list/", TagListView.as_view(), name="tag_list"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("post_delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("post_update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("post_total/", PostTotalTimeView.as_view(), name="post_total"),
]
