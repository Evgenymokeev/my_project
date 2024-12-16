from django.http import HttpResponse, HttpRequest,HttpResponseNotFound
from django.shortcuts import render, redirect,get_object_or_404
from datetime import datetime
import calendar
from myapp.models import Topic, Article



def main(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'main.html', {'articles': articles})
def feed(request):
    topics_name = Topic.objects.filter(name__in=['cinema','sport'])
    articles = Article.objects.filter(topic__in=topics_name).order_by('-created_at')
    if not articles.exists():
        return ("topics")

    return render(request, 'my_feed.html', {'articles': articles})

def set_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return render(request, 'article.html')

def main_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} comment")
def upd_article(request):
    updated_article = Article.objects.all()
    return render(request, 'update_article.html', {'updated_article': updated_article})
def del_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} delete")
def get_create(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'create_article.html', {'articles': articles})
def get_topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topic': topics})


def main_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    topic = get_object_or_404(Topic, pk=topic_id)
    articles = topic.articles.all()
    return render(request, 'topic.html', {'topic': topic, 'articles': articles})

def sub_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"This is topics #{topic_id}: subscribe")

def un_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"This is topics #{topic_id}: unsubscribe")
def get_profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')
def set_register(request: HttpRequest) -> HttpResponse:
    return render(request, 'register.html')
def st_password(request: HttpRequest) -> HttpResponse:
    return render(request, 'set_password.html')
def get_login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')
def art_logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Logout")


def month_archive(request: HttpRequest, year: int, month: int) -> HttpResponse:
    # Проверка на допустимый год
    current_year = datetime.now().year
    if year < 1900 or year > current_year + 10:
        return HttpResponseNotFound("Invalid year")
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month")
    articles = Article.objects.filter(created_at__year=year, created_at__month=month).order_by('-created_at')
    if articles.exists():
        return render(request, 'by_date.html', {'articles': articles, 'year': year, 'month': month})
    else:
        return render(request, 'by_date.html', {'articles': None, 'year': year, 'month': month})