from django.db.models.expressions import F
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import request
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.contrib import auth

from ordemfila.models import ordem_fila
from fila.models import vaga_fila
from .models import Fila
from rest_framework import viewsets
from .serializer import OrdemFilaSerializer

import json
import requests

# Create your views here.

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
    
    return redirect ('login')

def  dashboard (request):
    if request.user.is_authenticated:
        
        filas = Fila.objects.all()
        
        dados = {
            'filas' : filas
        }
        
        return render(request, 'usuarios/dashboard.html', dados)
    
    else:
        return redirect ('login')
    
def index (request):
    if request.user.is_authenticated:
    
        
        return redirect ('dashboard')
    
    else:
        return redirect ('login')
    
def fila (request, fila_id):
    
    dados_fila = get_object_or_404(Fila, pk=fila_id)
    vagas = vaga_fila.objects.all()
    
    fila_aguardando = ordem_fila.objects.all().filter(fila=fila_id, posicao3=1)
    totalPessoasFila = ordem_fila.objects.filter(fila=fila_id, posicao3=1).count()
    
    print(totalPessoasFila)
    
    exibir_fila ={
        'fila' : dados_fila,
        'vagas' : vagas,
        'fila_aguardando' : fila_aguardando,
        'totalPessoas': totalPessoasFila
    }
    return render (request, 'Fila.html', exibir_fila)

def adicionar_pessoas(request):
    
    vagas = vaga_fila.objects.all()
    
    dados = {
        'vagas' : vagas
    }
    
    
    if request.method == 'POST':
        
        fila = request.POST ['fila']
        nome = request.POST ['nome']
        celular = request.POST ['celular']
        vaga = request.POST ['vaga']
        placa = request.POST ['placa']
        posicao2 = 1
        posicao3 = 1
        
        #values('posicao',)
        #posicao = ordem_fila.objects.filter(fila=fila).latest('posicao')
        verUltimaPosicao = ordem_fila.objects.values('posicao',).filter(fila=fila).last()
        UltimaPosicao = ordem_fila.objects.values('id').last()
        
        #if UltimaPosicao['id'].exist():
        
            
        
        if ordem_fila.objects.filter(fila=fila).exists():
            
            ultima = verUltimaPosicao['posicao']
            novaPosicao = ultima + 1
            
            ultima = UltimaPosicao['id']
            posicao_fila = ultima + 1
            
            salvarFila = ordem_fila.objects.create(fila=fila, nome_usuario=nome, celular_usuario=celular, posicao=novaPosicao, vaga=vaga, posicao2 = posicao2, posicao3 = posicao3, placa=placa )
            salvarFila.save()
            
            print("Salvo..")
            
            #https://api.whatsapp.com/send?phone=552199999&text=dsds
            return redirect ("http://api.whatsapp.com/send?phone=55" + celular +"&text= Você foi cadastrado na fila, visualize sua posição aqui: http://localhost:8000/minhaposicao/" + fila + "/" + str(posicao_fila))
            
        else:
        
            posicao = 0
            posicao_fila = 1
            
            salvarFila = ordem_fila.objects.create(fila=fila, nome_usuario=nome, celular_usuario=celular, posicao=posicao, vaga=vaga, posicao2 = posicao2, posicao3 = posicao3, placa = placa)
            salvarFila.save()
            
            print("Salvo..")    
        
            #https://api.whatsapp.com/send?phone=552199999&text=dsds
            return redirect ("http://api.whatsapp.com/send?phone=55" + celular +"&text= Você foi cadastrado na fila, visualize sua posição aqui: http://localhost:8000/minhaposicao/" + fila + "/" + str(posicao_fila))
    
    else:
        #api.whatsapp.com/send?phone=15551234567
        return render (request, 'adicionar_pessoas.html', dados)

def criar_fila(request):
    
    if request.method == 'POST':
        
        salvar_nome_fila = request.POST ['nome_fila']
        salvar_empresa = request.POST ['empresa']
        salvar_site = request.POST ['site']
        salvar_vaga = request.POST ['vaga']
        
        fila = Fila.objects.create(nome_fila=salvar_nome_fila, empresa=salvar_empresa, site=salvar_site, vaga=salvar_vaga)
        fila.save()
        
        print('Fila Salva')
        return redirect ('index')
    
    else:
        return render (request, 'criar_fila.html')

def visualizar_fila(request, fila_id, fila_usuario):
        
    r = requests.get('http://localhost:8000/apiordemfilas/' + str(fila_usuario))
    totalPessoasFila = ordem_fila.objects.filter(fila=fila_id, posicao3=1).count()

    books = r.json()
    
    books2 = books['posicao']

    books_list = {
            'books':books,
            'posicaofila':books2,   
            }
    

    
    
    
    
    return render(request,'visualizar_fila.html', books_list)
    
   
def deleta_usuario(request, usuario_id):
    
    
    
    ver = ordem_fila.objects.filter(pk=usuario_id).values('fila').last()
    id_fila = ver['fila']
    id = str(id_fila)
    
    ordem_fila.objects.filter(fila=id).update(posicao=F('posicao') - 1)
    
    print(id)
    
    usuario = get_object_or_404(ordem_fila, pk=usuario_id)
    usuario.delete()
    
    return redirect('index')

    
#METODO USADO PARA ATUALIZAR A POSIÇÃO DOS USUARIOS NA FILA
def atualiza(request, usuario_id):
    
   
    if request.method == 'POST':
            
        id_fila = request.POST ['id_fila']
        
        #AQUI ENCONTRO A ULTIMA POSIÇÃO DA FILA DE ACORDO COM O CLIENTE EM ESPERA
        ver = ordem_fila.objects.filter(pk=usuario_id).values('fila').last()
        
        #SEPARO E PEGO O VALOR DO DISCIONARIO
        id_fila = ver['fila']
        id = str(id_fila)
        
        #AQUI PEGO A POSIÇÃO PARA COMPARAR E FAZER AS ATUALIZAÇÕES, CASO CONTRARIO ELE ATUALIZA TUDO
        posicao = ordem_fila.objects.filter(pk=usuario_id).values_list('posicao', flat=True).get()
        
        #CONTO O TOTAL DE PESSOAS NA FILA PARA COMPARAR NO PROXIMO IF
        totalPessoasFila = ordem_fila.objects.filter(fila=id_fila, posicao3=1).count()
        
        soma_posicao = posicao + 1
        
        if soma_posicao == totalPessoasFila: 
            
            ordem_fila.objects.filter(fila=id, posicao__gt = 0, posicao = soma_posicao).update(posicao=F('posicao') - soma_posicao)
            
            usuario = get_object_or_404(ordem_fila, pk=usuario_id)
            usuario.posicao3 = 0
            usuario.save()
            
            print("deletado")
                    
        else:
            
            ordem_fila.objects.filter(fila=id, posicao__gt = 0).update(posicao=F('posicao') - 1)
            
            usuario = get_object_or_404(ordem_fila, pk=usuario_id)
            usuario.posicao3 = 0
            usuario.save()

            print("Atualizado") 

        

        return redirect('index')

def mudar_status(request, usuario_id):
    
    ver = Fila.objects.filter(pk=usuario_id).values('id').last()
    idx = ver['id']
    id = str(idx)
    
    
    
    if request.method == 'POST':
        status2 = request.POST ['status']

        Fila.objects.filter(pk=id).update(status=status2)
        
        
    
    return redirect('dashboard')

class ordemViewset (viewsets.ModelViewSet):
        
    queryset = ordem_fila.objects.all()
    serializer_class = OrdemFilaSerializer