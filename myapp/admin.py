from django.contrib import admin
from myapp.models import Topic, Article, Comment, Profile

admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Profile)
