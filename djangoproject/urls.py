"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import ArticleListView,FeedView, ArticleDetailView, main_article, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, TopicListView,TopicDetailView,SubscribeTopicView,UnsubscribeTopicView,ProfileView,UserRegisterView,PasswordChangeView,get_login,art_logout,MonthArchiveView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
path('', ArticleListView.as_view(), name='main'),
path('feed/', FeedView.as_view(), name='my_feed'),

path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:article_id>/comment/', main_article, name='main_article'),
    #
path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='update_article'),


path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),

path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic'),
    path('article/create/', ArticleCreateView.as_view(), name='create_article'),
    path('topics/', TopicListView.as_view(), name='topics'),
path('topic/<int:topic_id>/subscribe/', SubscribeTopicView.as_view(), name='subscribe_topic'),
    path('topic/<int:topic_id>/unsubscribe/', UnsubscribeTopicView.as_view(), name='unsubscribe_topic'),
path('profile/', ProfileView.as_view(), name='profile'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('set-password/', PasswordChangeView.as_view(), name='set_password'),
    path('login/', get_login, name='login'),
    path('logout/', art_logout, name='logout'),
path('archive/<int:year>/<int:month>/', MonthArchiveView.as_view(), name='by_date'),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)