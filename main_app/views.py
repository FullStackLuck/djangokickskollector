from django.shortcuts import render
from django.http import HttpResponse 
from .models import Kick
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Collection
# class Kick:
#     def __init__(self, name, brand, color, release):
#         self.name = name
#         self.brand = brand
#         self.color = color
#         self.release = release

# kicks = [
#     Kick("Bred 11'", "Air Jordans", "Red, Black, White", 2012),
# ]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render (request, "about.html")

def kicks_index(request):
    kicks = Kick.objects.all()
    return render (request,"kicks/index.html", {'kicks':kicks})

def kicks_detail(request, kick_id):
    kick = Kick.objects.get(id=kick_id)
    return render(request, 'kicks/detail.html', {'kick':kick})

class KickCreate(CreateView):
    model = Kick
    fields = "__all__"
    success_url = '/kicks/'

class KickUpdate(UpdateView):
    model = Kick
    fields = "__all__"

class KickDelete(DeleteView):
    model=Kick
    success_url= "/kicks/"