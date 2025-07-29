from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.get_articles, name='get_articles'),
    path('articles/create', views.create_article, name='create_article'),
    path('article/<int:pk>', views.get_article, name='get_article'),
    path('article/<int:pk>/update', views.update_article, name='update_article'),
    path('article/<int:pk>/delete', views.delete_article, name='delete_article'),
]