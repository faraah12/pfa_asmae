from django.shortcuts import render
from .models import Vol

def home(request):
    list_vols = Vol.objects.all()
    context={"liste_vols":list_vols}
    return render(request,"index.html",context)