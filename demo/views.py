from django.shortcuts import render ,HttpResponse
from .models import  Students ,Foorm

# Create your views here.
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