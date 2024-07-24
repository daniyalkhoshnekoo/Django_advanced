from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    #path('f/', views.indexview, name='fbv-index'),
    #path("c/", TemplateView.as_view(template_name="index.html")),
    path('cbv-index/', views.IndexView.as_view(),name='cbv-index'),
    path('post/', views.PostList.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]