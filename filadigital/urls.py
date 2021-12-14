from django.db import router
from django.urls import path
from django.urls.conf import include, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ordemfilas', views.ordemViewset, basename='OrdemFilas')


urlpatterns = [
    path('', views.index, name='index'),
    path('criar_fila', views.criar_fila, name='criar_fila'),
    path('<int:fila_id>', views.fila, name='fila'),
    path('adicionar_pessoas', views.adicionar_pessoas, name='adicionar_pessoas'),
    path('minhaposicao/<int:fila_id>/<int:fila_usuario>', views.visualizar_fila, name='minhaposicao'),
    path('api', include(router.urls)),
    path('deleta/<int:usuario_id>',  views.deleta_usuario, name='deleta_usuario'),
    path('atualiza/<int:usuario_id>',  views.atualiza, name='atualiza'),
]