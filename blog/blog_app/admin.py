from django.contrib import admin
from blog_app.models import blogpost
from blog_app.models import Contact
from blog_app.models import Event
from blog_app.models import News

# Register your models here.
admin.site.register(blogpost)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(News)
