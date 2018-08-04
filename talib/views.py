from django.shortcuts import render
from talib.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def index(request):
    return render(request,"talib/index.html")

def register(request):
    registered = False
    print(100000000000000000001)
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit =False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'talib/registration.html',{'user_form':user_form,
                                                'profile_form':profile_form,
                                                'registered':registered
                                                })

def user_login(requeset):
    if requeset.method == 'POST':
        username = requeset.POST['username']
        password = requeset.POST['password']
        print(username)
        print(password)

        user = authenticate(requeset,username=username,password=password)
        if user:
            if user.is_active:
                login(requeset,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse('INVALIDE')
    else:
        return render(requeset,'talib/login.html')