from django.shortcuts import render ,HttpResponse,redirect
from .models import  Students ,Foorm
from .form import Addstud ,Formss,Userauth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as logoutsite
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .jasons import Studentser
from django.http import HttpResponse
def file(request):
    data = Students.objects.all()

    return render(request, 'demo/index1.html', {'data':data})
def iD(request,st_id):
    dat = Students.objects.filter(id=st_id)

    return render(request, 'demo/index2.html', {'d':dat})

def delate(request,st_i):

     Students.objects.filter(id=st_i).delete()
     da = Students.objects.all()
     return render(request, 'demo/index3.html',{'e':da})

    # return render(request, 'demo/index3.html', {'di':da})

def form(request):

    # dat = Students.objects.filter(id=st_id)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        track = request.POST['track']
        # Students.objects.create(name =name ,age=age , track= track)
        Students.objects.create(name=name, age=age,track=track)
        return redirect('bac')
    # return redirect('ad/')

    return render(request, 'demo/form.html')


def login(request):

    # dat = Students.objects.filter(id=st_id)
    if request.method == 'POST':
        name = request.POST['email']
        age = request.POST['password']
        # track = request.POST['track']
        # Students.objects.create(name =name ,age=age , track= track)
        Foorm.objects.create(name=name, passw=age)


    return render(request, 'login/login.html')


def addnew(request):
    form = Addstud()
    if (request.method=='GET'):
        return render(request,'demo/testform.html',{'form':form})
    else:
        form = Addstud(request.POST)
        if(form.is_valid()):
         Students.objects.create(name=request.POST['name'], age=request.POST['age'], track=request.POST['track'])
        return redirect('bac')


def Login(request):
    form = Formss()
    if (request.method=='POST'):
    #     return render(request,'login/login.html',{'form':form})
    # else:
        form = Formss(request.POST)
        if form.is_valid():
         # Foorm.objects.create(name=request.POST['name'], passw=request.POST['passw'])
            use = form.save()
            auth_login(request,use)
            return redirect('bac')
        return render(request, 'login/login.html',{'form':form})
def createuser(request):
    form = Formss()

    mysuer=User.objects.create_user('mohamedhamed','mohamedhame2ed@gmail.com','0129879597')
    return render(request,'login/login.html',{'form':form})
def loginbase(request):
    user = {}
    data = Students.objects.all()
    form = Userauth
    if (request.method=='GET'):
        return render(request,'login/login.html',{'form':form})

    else:
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       print(user)
       if (user):
           auth_login(request,user)
           return redirect('bac')
           # return render(request, 'demo/index1.html', {'form': data , 'us':user})
           # return redirect('bac')


def logOut(request):
    logoutsite(request)

    return render(request,'login/logotsite.html')
       # return render(request, 'demo/index1.html', {'form': form})
class Apostudent(APIView):
    def get(self,request):
        dataApi = Students.objects.all()
        da = Studentser(dataApi,many=True)
        return Response(da.data)
    def post(self,request):
        Students.objects.create(name=request.POST['name'], age=request.POST['age'], track=request.POST['track'])
        return HttpResponse(status=200)

@login_required
def vi(request):

    return render(request,'demo/hi.html')