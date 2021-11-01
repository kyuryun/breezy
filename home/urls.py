from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home_index'),
    path('about/', AboutView.as_view(), name='home_about'),
    path('service/', ServiceView.as_view(), name='home_service'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/detail/<pk>/', review_detail, name='review_detail'),
    path('review/upload/', post_new, name='review_upload'),
    path('review/delete/<int:pk>/', remove_post, name='review_delete'),
    path('review/edit/<int:pk>/', edit_post, name='review_edit'),

    path('post/', PostList.as_view(), name='post_list'),
    path('post/upload/', post_new2, name='post_upload'),
    path('post/detail/<pk>/', post_detail, name='post_detail'),
    path('post/delete/<int:pk>/', remove_post2, name='post_delete'),
    path('post/edit/<int:pk>/', edit_post2, name='post_edit'),

    path('review/comment/<int:pk>', comment_new, name="comment_new"),
    path('post/comment/<int:pk>', comment_new2, name="comment_new2"),

    # FAQ 화면
    path('faq/', FAQView.as_view(), name='post_faq'),
]