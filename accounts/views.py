from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        fm = UserCreationForm()
    return render (request, 'accounts/register.html',{'form':fm})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST )
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/accounts/profile') 
        else:
            fm = AuthenticationForm()      
        return render (request, 'accounts/login.html',{'form':fm})
    else: 
        return HttpResponseRedirect('/accounts/profile')      
    

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'accounts/profile.html')
    else:
        return HttpResponseRedirect('/accounts/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')