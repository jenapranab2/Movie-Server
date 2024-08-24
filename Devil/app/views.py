from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .form import *
from django.urls import reverse

# Create your views here.

def home(request):
    MO = Movies.objects.all()
    d={'MO':MO}
    if request.method == "POST":
        mov_no1 = request.POST.get("sl")
        request.session['no']=mov_no1
        return HttpResponseRedirect(reverse('movie'))
    return render(request,'home.html',d)

def show(request):
    no= request.session.get('no')
    movie=Movies.objects.filter(movie_no=no)
    d={'movie':movie}
    return render(request,'movie.html',d)

def player(request):
    no=request.session.get('no')
    movie = Movies.objects.filter(movie_no = no)
    print(movie[0].movie)
    d={'movie1':movie[0].movie,'movie':movie}
    return render(request,'t.html',d)


def english(request):
    MO= Movies.objects.filter(lang="Engish")
    d={'MO':MO}
    if request.method == "POST":
        mov_no1 = request.POST.get("sl")
        request.session['no']=mov_no1
        return HttpResponseRedirect(reverse('movie'))
    return render(request,'home.html',d)


def hindi(request):
    MO= Movies.objects.filter(lang="Hindi")
    d={'MO':MO}
    if request.method == "POST":
        mov_no1 = request.POST.get("sl")
        request.session['no']=mov_no1
        return HttpResponseRedirect(reverse('movie'))
    return render(request,'home.html',d)

def admin_reg(request):
    ARF = Admin_Reg()
    d={'ARF':ARF}

    if request.method == 'POST':
        ARDF = Admin_Reg(request.POST)

        if ARDF.is_valid() :
            pw = ARDF.cleaned_data['password']
            MARDF = ARDF.save(commit=False)
            MARDF.set_password(pw)
            MARDF.save()
        return HttpResponseRedirect(reverse('admin_log'))
    return render(request,'admin_reg.html',d)



def admin_log(request):
    if request.method =='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')

        AUO = authenticate(username=un,password=pw)
        if AUO and AUO.is_active :
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('upload'))
        return HttpResponse("invalid credentials")
    return render(request,'login.html')

def upload(request):
    UDF= Upload()
    d = {'UDF':UDF}
    if request.method =='POST' and request.FILES: 
        
        UDFO = Upload(request.POST,request.FILES)
        print(UDFO)
        if UDFO.is_valid():
            UDFO.save()
        else:
            return HttpResponse('invalid data')
    return render(request,'upload.html',d)
    

def play(request):
    pass