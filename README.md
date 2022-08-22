# BestCare - Sistema de gestao de pacientes internados em Casas de Repouso

Projeto de conclusão do Curso Entra21/2022 - Python

Desenvolvedores:
- Giovani Dalbosco
- Jackson Castellain
- Lucas Rezende
- Samir Buhatem

## 29/07/2022
- Criado versão BestCare v1.0 no Draw.io para inicialização do diagrama de classes;
- Definido foco na administração do paciente;

##  01/08/2022
- Aprovado o Projeto pelo Prof. Adriano
- Mensagens via WhattsApp, Telegram e E-mail devem ser colocados em Entidade Propria, e nao enviar.
- Programa devera ser iniciado pela criacao das paginas de Front End

### Paginas a serem criadas
- Log-in
- Cadastro Usuario
- Cadastro Residente
- Cadastro Contato/Responsavel
- Cadastro Informacoes
- Cadastro Comorbidades
- Cadastro Medicamentos
- Inclusao Documentos

### Sprint_01 - 12/08 a 19/08
- Definicao Template
- Responsavel: Todos
- Ferramentas: HTML/CSS/JS

##  18/08/2022

### História do usuário
- Sistema de gerenciamento para casas de repouso focado no residente. 
- Principais funcionalidades:
  - Agenda diária de atividades, remédios, consultas e exames;
  - Lembretes automáticos;
  - Armazenamento de histórico de rotinas (eventos) com retorno de previsibilidade de consumo de itens pessoais e remedios;
  - Controle de estoque individualizado por residente de itens de higiene e medicamentos;
  - Comunicação com responsável externo (log de saída) a confirmação de todos os eventos do residente com o log do responsável pela solução;
  - Dashboard.


- Entidades do projeto:
  - Log-in;
  - Cadastro Usuario;
  - Cadastro Residente;
  - Cadastro Contato/Responsavel;
  - Cadastro Informacoes;
  - Cadastro Comorbidades;
  - Cadastro Medicamentos;
  - Inclusao Documentos;
  - Log de eventos.

Beneficios:
  - Acompanhamento do residente em tempo real;
  - Lembretes instantaneos;
  - Gestao de estoque de medicamentos e itens de higiene;
  - Estatistica de consumo de itens (fraldas por exemplo);
  - Registro de ocorrencias anomalas;
  - Gestao de responsabilidade das prescricoes medicas;
  - Relatorio mensal dos eventos;
  - Mensagens de intercorrencia instantaneas;
  - Melhor relacao entre Cuidador e Responsavel Externo.

# 22/08/2022


> Diagrama de relacionamentos

```md
Pessoas
-
pessoa_id int PK
pessoa_nome string
pessoa_endereco string
pessoa_CPF String
pessoa_classe_id String FK >- Classe.classe_id
pessoa_telefone String
pessoa_estoque_id String FK >- Estoque_Individual.estoque_id
pessoa_comorbidade_id String FK >-< Pessoas_Comorbidades.pessoa_comorbidade_id


Estoque_Individual
-
estoque_id int PK
estoque_consumo_id string FK - Usos_E_Consumo.consumo_id 
estoque_quantidade int


Eventos
-
evento_id int PK
evento_nome String
evento_pessoa_paciente string FK >- Pessoas.pessoa_id
evento_pessoa_funcionario String FK >- Pessoas.pessoa_id 

user
-
usuario_id int PK
usuario_nome String

Comorbidades
-
comorbidade_id int PK
comorbidade_nome String

Classe
-
classe_id int PK
classe_nome String

Usos_E_Consumo
-
consumo_id int PK
consumo_nome String

Pessoas_Comorbidades
-
pessoa_comorbidade_id int PK
pessoa_comorbidade_nome String  FK - Comorbidades.comorbidade_id
```

