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
  - Log-in;
    > Destinado a armazenar os logs de ingresso ao sistema.
  - Cidades;
    > Lista dos municipios brasileiros e seu estado.
  - Comorbidades;
    > Relacao das comorbidades listadas no site do Ministerio da Saude.
  - Documentos;
    > Armazenamento de arquivos documentais do Residente.
  - Estoque_Individual;
    > Estoque individual do residente, com finalidade de controlar o consumos de itens pessoais, sob a guarda da Casa de Repouso.
  - Eventos;
    > Eventos previsiveis e capaz de gerar log na agenda do Residente.
  - Ocorrencias;
    > Ocorrencias nao previsiveis, que devem ser armazenadas compondo o relatorio do Residente.
  - Pessoas;
    > Cadastro com dados de Residentes, Cuidadores e Responsaveis Externo.
  - Prescricao;
    > medicamentos prescritos, registrados no arquivo de documento, populado em agenda. 
  - SinalVital;
    > Levantamento periodico dos sinais Vitais do Residente, com geracao de graficos evolutivos.
  - Usos_Consumo;
    > Material de uso e consumo do Residente, devidamente controlado pelo modulo de estoque.

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

## Instalação

Instale a versão 3.x do **Python** :

Clone este repositório no propmt do CMD: 
>git clone https://github.com/giovanidalbosco/BestCare.git

Vá para o repositório :
>cd BestCare

Crie um ambiente de desenvolvimento: 
> python -m venv venv

Vá para o ambiente:
> venv/Scripts/activate

Instale as dependências:
> pip install -r requirements.txt

Play o servidor: 
> python manage.py runserver


## Informações que devem ser adicionadas no arquivo .env

>SECRET_KEY = 'django-insecure-^nl5(2384i&aauk2flacfeq=mu9&xrn7a6t^p+g7@*bl9by55v'

>EMAIL_HOST_USER=bestcaureauth

>EMAIL_HOST_PASSWORD=bestcare@123

>EMAIL_USE_TLS=True

>EMAIL_PORT=587

>EMAIL_HOST=smtp-mail.outlook.com