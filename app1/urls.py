from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('quemSomos', views.Somos),
    path('base_telainicial', views.Base_telainicial),
    path('solucoes', views.Solucoes),
    path('login', views.Login, name='login'),
    path('cadastro', views.Cadastro, name='cadastro'),
    path('comorbidades_list', views.Comorbidades_list, name='comorbidades_list'),
    path('comorbidades_add', views.Comorbidades_add, name='comorbidades_form'),
    path('comorbidades_edit/<int:id>', views.Comorbidades_edit, name="comorbidades_form"),
    path('comorbidades_delete/<int:id>', views.Comorbidades_delete, name="comorbidades_delete"),
    path('telainicial', views.Inicial, name='telainicial'),
    path('medicamentos_list', views.Medicamentos_list, name='medicamentos_list'),
    path('medicamentos_add', views.Medicamentos_add, name='medicamentos_form'),
    path('medicamentos_edit/<int:id>', views.Medicamentos_edit, name="medicamentos_form"),
    path('medicamentos_delete/<int:id>', views.Medicamentos_delete, name="medicamentos_delete"),
    path('estoque_individual_list/', views.Estoque_Individual_list, name='estoque_individual_list'),
    path('estoque_individual_add/<int:id>', views.Estoque_Individual_add, name='estoque_individual_form'),
    path('ocorrencias_list', views.Ocorrencias_list, name='ocorrencias_list'),
    path('ocorrencias_add', views.Ocorrencias_add, name='ocorrencias_form'),
    path('ocorrencias_edit/<int:id>', views.Ocorrencias_edit, name='ocorrencias_form'),
    path('ocorrencias_delete/<int:id>', views.Ocorrencias_delete, name='ocorrencias_delete'),
    path('residentes_list', views.Residentes_list, name='residentes_list'),
    path('residentes_add', views.Residentes_add, name='residentes_form'),
    path('residentes_edit/<int:id>', views.Residentes_edit, name='residentes_form'),
    path('residentes_delete/<int:id>', views.Residentes_delete, name='residentes_delete'),
    path('cuidadores_list', views.Cuidadores_list, name='cuidadores_list'),
    path('cuidadores_add', views.Cuidadores_add, name='cuidadores_form'),
    path('cuidadores_edit/<int:id>', views.Cuidadores_edit, name='cuidadores_form'),
    path('cuidadores_delete/<int:id>', views.Cuidadores_delete, name='cuidadores_delete'),
    path('responsavel_list', views.Responsavel_list, name='responsavel_list'),
    path('responsavel_add', views.Responsavel_add, name='responsavel_form'),
    path('responsavel_edit/<int:id>', views.Responsavel_edit, name='responsavel_form'),
    path('responsavel_delete/<int:id>', views.Responsavel_delete, name='responsavel_delete'),
    path('sinalvital_list', views.SinalVital_list, name='sinalvital_list'),
    path('sinalvital_add', views.SinalVital_add, name='sinalvital_form'),
    path('sinalvital_edit/<int:id>', views.SinalVital_edit, name='sinalvital_form'),
    path('sinalvital_delete/<int:id>', views.SinalVital_delete, name='sinalvital_delete'),
    path('agenda/', views.Agenda.as_view(), name='agenda'),
    path('event/new/<int:residente_id>', views.event, name='event_new'),
    path('event/edit/<int:event_id>', views.event, name='event_edit'),
    #path('email', views.Envia_email, name='envia_email'),
    # path('estoque_edit/<int:id>', views.Estoque_edit, name="estoque_edit"),
    # path('estoque_delete/<int:id>', views.Estoque_delete, name="estoque_delete"),
]
