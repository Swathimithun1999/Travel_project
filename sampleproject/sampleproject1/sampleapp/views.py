from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})



def demo(request):
    obj=team.objects.all()
    return render(request,"index.html",{'result':obj  })































































































































































































#def addition(request)x=int(request.GET['num1'])
   #y=int(request.GET['num2'])
  # res={}
   #res["addition"]=x+y
   #res["substraction"] = x - y
  #res["multiplication"]=x*y
  #res["division"]=x/y
 # return render(request, "about.html", {'result': res})

   # def detail(request):
   # return HttpResponse("hello i am details")

   # def thanks(request):
   # return HttpResponse("Thank you all")





































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































