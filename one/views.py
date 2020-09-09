from django.shortcuts import render
from one.models import UpcommingEvent,AboutUs,Events,Home,Gallery
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    home_data=Home.objects.all()
    return render(request,'home/index.html',{'home':home_data})


def resources(request):
    event_data=UpcommingEvent.objects.all().order_by('-id')
    resource_data=Events.objects.all().order_by('-resourcetDate')
    paginator = Paginator(resource_data,9)
    page = request.GET.get('page')
    resource_data = paginator.get_page(page)
    return render(request,'home/resource.html',{'resource':resource_data,'event':event_data})

def about(request):
    about_data = AboutUs.objects.all()
    return render(request,'home/about.html',{'about':about_data})

def gallery(request):
    gallery_data = Gallery.objects.all().order_by('-id')
    paginator = Paginator(gallery_data,9)
    page = request.GET.get('page')
    gallery_data = paginator.get_page(page)
    return render(request,'home/gallery.html',{'gallery':gallery_data})