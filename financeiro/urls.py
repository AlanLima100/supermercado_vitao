from django.urls import path
from .views import index, cadastro_cliente, promocao, produtos

urlpatterns = [
    path('', index, name='index'),
    path('cadastro_cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('promocao/', promocao, name='promocao'),
    path('produtos/', produtos, name='produtos'),

]
