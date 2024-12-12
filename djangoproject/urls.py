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
from myapp.views import (main, feed, set_article, main_article, upd_article, del_article, get_create, get_topics,main_topic, \
    sub_topic,un_topic,get_profile,set_register,st_password,get_login,art_logout,month_archive)



urlpatterns = [
    path('', main, name='main'),
    path('my-feed/', feed, name='my_feed'),
    path('<int:article_id>/', set_article, name='article'),
    path('<int:article_id>/comment/', main_article, name='main_article'),
    path('<int:article_id>/update/', upd_article, name='update_article'),
    path('<int:article_id>/delete/', del_article, name='delete_article'),
    path('create/', get_create, name='create_article'),
    path('topics/', get_topics, name='topics'),
    path('topics/<int:topic_id>/', main_topic, name='topic'),
    path('topics/<int:topic_id>/subscribe/', sub_topic, name='subscribe_topic'),
    path('topics/<int:topic_id>/unsubscribe/', un_topic, name='unsubscribe_topic'),
    path('profile/', get_profile, name='profile'),
    path('register/', set_register, name='register'),
    path('set-password/', st_password, name='set_password'),
    path('login/', get_login, name='login'),
    path('logout/', art_logout, name='logout'),
    path("<int:year>/<int:month>/", month_archive, name='by_date'),
    path('admin/', admin.site.urls),
]
