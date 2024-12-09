from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls page.")
# Create your views here.
