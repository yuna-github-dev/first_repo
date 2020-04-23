from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def var_view(request):
    nums = [1,2,3,4,5]
    return render(request, "var.html", {"nums":nums})
