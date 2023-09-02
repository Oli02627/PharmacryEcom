from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUPForm, LoginForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#==Account-Home============#
def account_home(request):
    return render(request,"account/account.html")

#==Login===================#
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.user.is_anonymous:    
        if request.method =='POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user and not user.is_active:
                    msg= '*Account is Deactivated'

                elif user and user.is_active:
                    login(request, user)
                    try:
                        if request.GET['next']:
                            return redirect(request.GET['next'])
                    except Exception as e:
                        return redirect('index')
                else:
                    msg= '* Invalid Credentials'
            else:
                msg = 'Error Valitation form'
        return render(request, 'account/login.html',{'form':form, 'msg':msg})
    
    elif request.user.is_authenticated:
        return redirect('index')


#====Sign-up=======================#
def register_view(request):
    msg = None
    
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUPForm(request.POST)

            if form.is_valid():
                form.save()
                msg = 'user created'
                return redirect('login_view')
            else:
                msg = '*Form Is Not Valid'
        else:
            form = SignUPForm()
        return render(request, 'account/signup.html', {'form': form, 'msg': msg})
    
    elif request.user.is_authenticated:
        return redirect('index')


#==logout===============================#
def logoutUser(request):
    logout(request)
    return redirect('index')

#==Profile========================#
@login_required
def profile_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = EditUserProfileForm(request.POST,request.FILES, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, '*Profile Update Successfully')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'account/profile_temp/profile.html',{'form':fm})
    else:
        return redirect('login_view')



#==Change-User-Password============================#
@login_required
def userchangepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ps = PasswordChangeForm(user=request.user, data=request.POST)
            if ps.is_valid():
                ps.save()
                update_session_auth_hash(request, ps.user)
                messages.success(request, '*Password Change Successfully')
                return redirect('profile_view')
        else:
            ps = PasswordChangeForm(user=request.user)
        return render(request,'account/profile_temp/changepass.html',{'form2':ps})
    else:
        return redirect('login_view')


