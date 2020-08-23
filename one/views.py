from django.shortcuts import render
from one.models import Event,Resource,AboutUs,EventsOver,Gal

# Create your views here.
def index(request):
    Gal_data=Gal.objects.all()
    return render(request,'home/index.html',{'gal':Gal_data})

def events(request):
    event_data=Event.objects.all()
    over_data=EventsOver.objects.all()
    return render(request,'home/events.html',{'event':event_data,'over':over_data})

def resources(request):
    resource_data=Resource.objects.all()
    return render(request,'home/resource.html',{'resource':resource_data})

def about(request):
    about_data = AboutUs.objects.all()
    return render(request,'home/about.html',{'about':about_data})
