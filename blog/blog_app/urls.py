from blog_app import views
from django.urls import path
from django.conf import settings        #for attach media files
from django.conf.urls.static import static  #for attach media files

urlpatterns = [
        path("",views.index,name='home'),
        path("about/",views.about,name='about'),
        path("contact/",views.contact,name='contact'),
        path("event/",views.event,name='event'),
        path("news/",views.news,name='news'),
        path("post_d/<slug>",views.post_d,name='post_d'),
        path("event_d/<slug>",views.event_d,name='event_d'),
        path("news_d/<slug>",views.news_d,name='news_d'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)