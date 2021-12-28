from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
""" 
def login (request):
    
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if  email == "" or senha == "":
            print('Os campos estão vazios.')
            return redirect ('login')
        
        #print(email, senha)
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print ("Login realizado")
                
                return redirect ('dashboard')
    
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    
    return redirect ('login.html')

def  dashboard (request):
    if request.user.is_authenticated:
        
        return render(request, 'usuarios/dashboard.html')
    
    else:
        return redirect ('login') """
