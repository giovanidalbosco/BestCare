# BestCare - Sistema de Controle de Residentes internados em Casas de Repouso

Desenvolvedores:
- Giovani Dalbosco
- Jackson Castellain
- Lucas Rezende
- Samir Buhatem

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

  - Cidades;
    > Lista dos municipios e estado.
  - Comorbidades;
    > Relacao das comorbidades listadas no site do Ministerio da Saude.
  - Estoque_Individual;
    > Estoque individual do residente, com finalidade de controlar o consumos de itens pessoais, sob a guarda da Casa de Repouso.
  - Event;
    > Eventos previsiveis gerarando log na agenda do Residente.
  - Ocorrencias;
    > Ocorrencias nao previsiveis, que devem ser armazenadas compondo o relatorio do Residente.
  - Pessoas;
    > Cadastro com dados de Residentes, Cuidadores e Responsaveis Externo.
  - SinalVital;
    > Levantamento periodico dos sinais Vitais do Residente;
  - Usos_Consumo;
    > Material de uso e consumo do Residente, devidamente controlado pelo modulo de estoque.

Beneficios:
  - Acompanhamento do residente em tempo real;
  - Lembretes instantaneos;
  - Gestao de estoque de medicamentos e itens de higiene;
  - Registro de ocorrencias anomalas;
  - Gestao de responsabilidade das prescricoes medicas;
  - Mensagens de intercorrencia instantaneas;
  - Melhor relacao entre Cuidador e Responsavel Externo.

## Instalação

Instale a versão 3.x do **Python** :

Clone este repositório no propmt do CMD: 
>git clone https://github.com/giovanidalbosco/BestCare.git

Vá para o repositório :
>cd BestCare

Criar um ambiente de desenvolvimento: 
> python -m venv venv

Ativar o ambiente virtual:
> venv/Scripts/activate

Instalar as dependências:
> pip install -r requirements.txt

Rodar o servidor: 
> python manage.py runserver

