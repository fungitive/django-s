from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def showtime(request):
    t=time.ctime()
    return render(request, "index.html",{"time":t})

def article_year(request,year):
    return HttpResponse("year:%s" % year)
def article_years(request,years,months):
    return HttpResponse("years:%s months:%s" % (years,months))
def registry(request):
    if request.method=="POST":
        print(request.POST.get("user"))
        print(request.POST.get("age"))
        return HttpResponse("success!")
    return render(request,"registry.html")