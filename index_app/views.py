from django.shortcuts import render,HttpResponse
import requests
from .models import *

# Create your views here.

# indext page
def index(request):
    return render(request,"index_app/index.html")


# get method page
def get_page(request):
    name=request.GET.get("name")
    text=request.GET.get("comment")
    if name!=None and text!=None :
        Comment.objects.create(name=name,comment=text)
    return render(request,"index_app/get.html")


# post method page
def post_page(request):
    name=request.POST.get("name_post")
    text=request.POST.get("comment_post")
    if name!=None and text!=None:
        Comment.objects.create(name=name,comment=text)
    return render(request,"index_app/post.html")

#ddos page
def ddos_apge(request):
    url = "http://127.0.0.1:8000/get/?name=%D8%A7%D8%B4%DA%A9%D8%A7%D9%86+%D9%BE%D9%88%D8%B1%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D9%84%D9%87&comment=a&done=send"
    for i in range(100000):
        requests.get(url=url)
    return HttpResponse("DDOS attack complited!")