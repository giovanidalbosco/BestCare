from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('quemSomos', views.Somos),
    path('solucoes',views.Solucoes),
    path('cadastro',views.Cad, name='cadastro'),
    path('comorbidades_list', views.Comorbidades_list, name='comorbidades_list'),
    path('comorbidades_add', views.Comorbidades_add, name='comorbidades_add'),
    path('comorbidade_edit/<int:id>', views.Comorbidade_edit, name="comorbidade_edit"),
    path('comorbidade_delete/<int:id>', views.Comorbidade_delete, name="delete-comorbidade"),
    path('telainicial',views.Inicial,name='telainicial'),
    path('agenda',views.Agenda)
]
