from django.shortcuts import render,HttpResponse
from blog_app.models import blogpost
from blog_app.models import Contact
from blog_app.models import Event
from blog_app.models import News
from datetime import datetime

# Create your views here.
def index(request):
    post= blogpost.objects.all()
    data={
        'data':post,
    }
    return render(request,'index.html',data)

def contact(request):
    data1={
        'tem':0,
    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        date=datetime.today()
        
        con = Contact(uname=name,email=email,phone=phone,desc=desc,date=date)
        con.save()
        data1['tem']=1
    return render(request,'contact.html',data1)

def about(request):
    return render(request, 'about.html')

def post_d(request,slug):
    raw_data=blogpost.objects.get(slug=slug)
    data0={
        'data':raw_data,
    }
    return render(request,'post_da.html',data0)

def event(request):
    i_data= Event.objects.all()
    data_ev={
        'data_ev':i_data,
    }
    return render(request, 'event.html',data_ev)

def news(request):
    i_data= News.objects.all()
    data_ne={
        'data_ne':i_data,
    }
    return render(request, 'news.html',data_ne)

def event_d(request,slug):
    ev_data=Event.objects.get(ev_slug=slug)
    data_ev={
        'data_ev':ev_data,
    }
    return render(request, 'event_d.html',data_ev)

def news_d(request,slug):
    ne_data=News.objects.get(n_slug=slug)
    data_ne={
        'data_ne':ne_data,
    }
    return render(request, 'news_d.html',data_ne)