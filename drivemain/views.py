from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MyModelForm
from .models import MyModel
# Create your views here.

def my_view(request):
    return render (request,"index.html")

def homepage(request):
    if request.method == "POST":
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("my-view")
    else:
        form = MyModelForm()
    return render(request, 'home.html', {'form': form})
    
def my_view(request):
    images = MyModel.objects.all()
    return render(request, "index.html", {"images": images})
