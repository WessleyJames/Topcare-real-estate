from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Property

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})
