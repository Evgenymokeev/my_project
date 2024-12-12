from django.http import HttpResponse, HttpRequest,HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
import calendar


def main(request: HttpRequest) -> HttpResponse:
    return render(request,"main.html")
# Create your views here.
def feed(request):
    return render(request, 'my_feed.html')
def set_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return render(request, 'article.html')
def main_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} comment")
def upd_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return render(request, 'update_article.html')
def del_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} delete")
def get_create(request: HttpRequest) -> HttpResponse:
    return render(request, 'create_article.html')
def get_topics(request: HttpRequest) -> HttpResponse:
    return render(request, 'topics.html')
def main_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return render(request, 'topic.html')
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
    current_year = datetime.now().year
    if year < 1900 or year > current_year + 10:
        return HttpResponseNotFound("Invalid year")
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(f"Articles for {calendar.month_name[month]} {year}")

