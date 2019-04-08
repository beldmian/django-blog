from django.urls import path
from . import views
from django.conf import settings
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.ShowArticlesView.as_view(), name='homepage'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail')
]
