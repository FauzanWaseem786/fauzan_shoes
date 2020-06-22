from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from website_model.forms import Membr_form,ord_form
from website_model.models import Member,ordr
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'website_model/home.html')
def Premium(request):
    return render(request,'website_model/premium.html')
def Variety(request):
    return render(request,'website_model/Variety.html')
def location(request):
    return render(request,'website_model/location.html')
def brands(request):
    return render(request,'website_model/brands.html')
def shoes (request):
    return render(request,'website_model/shoes.html')
def boots(request):
    return render(request,'website_model/boots.html')
def sandals(request):
    return render(request,'website_model/sandals.html')
def slippers(request):
    return render(request,'website_model/slippers.html')
def Membership(request):
    registered = False
    if(request.method == 'POST'):
        Member = Membr_form(request.POST,request.FILES)
        #profile = pro_form(request.POST,request.FILES)
        if Member.is_valid() :
            user = Member.save()
            username = request.POST.get('Name', '')
            password = request.POST.get('password', '')
            Email = request.POST.get('email', '')
            Hometown=request.POST.get('Hometown','')
            user.save()
            #profil = profile.save()
            #profil.save()
            user = authenticate(request, username=username, password=password,email=Email)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=username, password=password, email=Email)
                registered = True
                user.save()

        else:
            print("user_form.errors")
    else:
        Member=Membr_form()
        #profile=pro_form()
    return render(request,'website_model/premium.html',{ 'mem':Member,'registered':registered})
def login(request):
    logo=False
    if request.method == 'POST':
         username = request.POST.get('Name','')
         password = request.POST.get('password', '')

         user=authenticate(username=username,password=password)
         if user:
            if user.is_active:
                logi=True
                dj_login(request,user)
                #return HttpResponseRedirect(reverse('index'))
                return render(request,'website_model/home.html',{'logi':logi})
            else:
                return HttpResponse("Your account was inactive.")
         else:
            print("Someone tried to login and failed.")
            print("their credentials were username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'website_model/login.html', {})
@login_required
def ilogout(request):
    logout(request)
    return redirect('/login/')
def change(request):
    if(request.method == 'POST'):
        u=request.POST.get('Name','')
        Usr=User.objects.get(username=u)
        n=request.POST.get('newpassword','')
        Usr.set_password(n)
        Usr.save()
        return redirect('/login/')
    else:
        return render(request, 'website_model/chg_pswrd.html', {})

def OrDer(request):
    if(request.method == 'POST'):
        O=True
        order =ord_form(request.POST)
        Email=request.POST.get('email_id','')
        if order.is_valid() :
            ord = order.save()
            ord.save()
            print('mail',Email)
            send_mail('Your order has been succesfully placed.','Thanks a lot for buying from us .','vasufauzan1010@gmail.com',[Email],fail_silently=False)
        else:
            print("user_form.errors")
    else:
        O=False
        order = ord_form()

    return render(request,'website_model/order.html',{ 'order':order,'O':O})
