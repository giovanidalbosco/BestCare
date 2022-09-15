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
    path('agenda',views.Agenda),
    path('uso_consumo_list', views.Uso_Consumo_list, name='uso_consumo_list'),
    path('uso_consumo_add', views.Uso_Consumo_add, name='uso_consumo_add'),
    path('uso_consumo_edit/<int:id>', views.Uso_Consumo_edit, name="uso_consumo_edit"),
    path('uso_consumo_delete/<int:id>', views.Uso_Consumo_delete, name="uso_consumo_delete"),
    path('estoque_individual_list', views.Estoque_Individual_list, name='estoque_individual_list'),
    path('estoque_individual_add', views.Estoque_Individual_add, name='estoque_individual_add'),
    #path('email', views.Envia_email, name='envia_email'),
    # path('estoque_edit/<int:id>', views.Estoque_edit, name="estoque_edit"),
    # path('estoque_delete/<int:id>', views.Estoque_delete, name="estoque_delete"),
]
