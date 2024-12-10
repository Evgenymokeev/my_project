from django.http import HttpResponse, HttpRequest,HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
import calendar


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls page.")
# Create your views here.
def feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls page.")
def article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} ")
def main_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} comment")
def update_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} update")
def del_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Hello. It's id: {article_id} delete")
def get_create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Create")
def get_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Topics")
def main_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"This is topics #{topic_id}.")
def sub_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"This is topics #{topic_id}: subscribe")

def un_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"This is topics #{topic_id}: unsubscribe")
def get_profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Profile")
def set_register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Register")
def st_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. st_password")
def get_login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Login")
def art_logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. Logout")
def month_archive(request: HttpRequest, year: int, month: int) -> HttpResponse:
    current_year = datetime.now().year
    if year < 1900 or year > current_year + 10:
        return HttpResponseNotFound("Invalid year")
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(f"Articles for {calendar.month_name[month]} {year}")

