from django.contrib import admin
from .models import Posts, Comment, Faq

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Faq)