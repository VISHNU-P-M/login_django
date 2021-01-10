from django.contrib import messages
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.session.has_key('password'):
        return redirect(home)
    else:
        return render(request,'login.html')
def home(request):
    if request.session.has_key('password'):
        return render(request,'home.html')
    else:
        return redirect(login)
def send(request):  
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        if uname == 'vishnumanoharan' and pswd == 'qwerty123':
            request.session['password']=pswd
            return JsonResponse('true',safe=False)
        else :
            return JsonResponse('false',safe=False)
            
def logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(login)
        
        
    