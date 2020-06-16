from django.shortcuts import render,redirect
from app import forms

from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login
from django.contrib import auth
from django.contrib import messages
from app.models import *
import json
# Create your views here.
from django.contrib.messages import get_messages
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request,'index.html')


def signup(request):
    form= forms.UserCreationForm()
    if request.method=='POST':
        form= forms.UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            name=form.cleaned_data.get('name')
            messages.success(request,f"{name}", extra_tags='alert')
            login(request,user)
            #return redirect('/dashboard/')
            return HttpResponse('USer created successfully')
        else:
            #for msg in form.error_messages:
            #    messages.error(request,f"{msg}: {form.error_messages[msg]}")
            messages.error(request, 'Invalid details', extra_tags='alert')

    return render(request,'signup.html',{'form':form})
def customauthenticate(email,password):
    userr = Registration.objects.all().get(email=email)
    if userr.password==password:
        return userr
    return None

def authlogin(request):
    form= forms.LoginForm()
    if request.method=='POST':
        form= forms.LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]

            user = customauthenticate(email=email,password=password)
            if user is not None:
                messages.success(request, f"{user.name}", extra_tags='alert')
                login(request, user)
                #messages.info(request, user.name)
                #messages.success(request,"login successful")
                return redirect('/dashboard/')
                #return render(request, 'home.html',{'user':user})
                #return HttpResponse(user.name)
            else:
                messages.error(request,"Invalid Credentails", extra_tags='alert')

                return render(request, 'login.html',{'form':form})




    return render(request,'login.html',{'form':form})



def dashboard(request):

    if messages:

        storage = get_messages(request)
        if len(storage)==1:
            for ele in storage:
                name=ele
            user=Registration.objects.get(name=name)
            #return HttpResponse(user)
            return render(request,'dashboard.html',{'user':user})


def categoryform(request,name):
    user=Registration.objects.get(name=name)
    requestType=user.personcategory_id
    if requestType==2:
        form= forms.MoneyFinderForm(instance=user)
        if request.method=='POST':
            form = forms.MoneyFinderForm(request.POST)

    elif requestType==1:
        form=forms.InvestorForm(instance=user)
        if request.method=='POST':
            form = forms.InvestorForm(request.POST)

    #elif requestType=='Others':
    else:
        form=forms.OthersForm(instance=user)
        if request.method=='POST':
            form = forms.OthersForm(request.POST)



    if form.is_valid():
        form.save()
        return HttpResponse('<h2>Data saved successfully</h2>')

    return render(request,'categoryform.html',{'form':form,'name':name})


def logout(request):
    auth.logout(request)
    return render(request,'index.html')


def myforms(request,id):
    user=Registration.objects.all().get(id=id)
    if user.personcategory_id==1:
        inv=Investor.objects.all().order_by('-date')
        return render(request,'myforms.html',{'Category':inv,'cat':'Investor'})
    elif user.personcategory_id==2:
        mf=MoneyFinder.objects.order_by('-date')

        return render(request,'myforms.html',{'Category':mf,'cat':'MoneyFinder'})
    else:

        return render(request,'myforms.html',{'Category':Others.objects.order_by('-date'),'cat':'Others'})


def form(request,id,cat):
    if cat=='Investor':
        requestedform=Investor.objects.all().get(id=id)
        formm=forms.InvestorForm(instance=requestedform)

    elif cat=='Money Finder':
        requestedform=MoneyFinder.objects.all().get(id=id)
        formm=forms.MoneyFinderForm(instance=requestedform)
    else:
        requestedform=Others.objects.all().get(id=id)
        formm=forms.OthersForm(instance=requestedform)


    if request.method == 'POST':
        formm = forms.InvestorForm(request.POST)
        if formm.is_valid():
            formm.save()
            return HttpResponse('<h2>Changes Succesful </h2>')
            #return redirect('/myforms/',{'id':id})

    return render(request,'form.html',{'form':formm,'id':id,'cat':cat})

@api_view(['DELETE'])
def removeform(request,id,cat):
    if cat=='Investor':
        obf=Investor.objects.get(id=id)
        obf.delete()
    elif cat=='Money Finder':
        obf=MoneyFinder.objects.get(id=id)
        obf.delete()
    else:
        obf=Others.objects.get(id=id)
        obf.delete()

    return Response('Item deleted successfully')














