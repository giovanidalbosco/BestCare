# Título do projeto
## BestCare - Sistema de Controle de Residentes internados em Casas de Repouso

✒️ Desenvolvedores / Responsabilidade
- Giovani Dalbosco - BackEnd Python
- Jackson Castellain - FrontEnd HTML/CCS/JS
- Lucas Rezende - BackEnd Python
- Samir Buhatem - Banco de Dados MySQL/SQlite3

🛠️ Construído com:
> Django
> Python
> MySQL
> HTML5
> CSS3
> JS

⌨️ História do usuário
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
  
Futuro do Best Care:
  - Alarme de Agenda
  - Log de Atendimento Ocorrencias/Agenda
  - Disparo WhattsApp por Ocorrencia
  - Emissao Relatorio Mensal de Agenda e Ocorrencias, incluindo historico de Sinal Vital
  - Controle de Estoque Individual
  - Planejamento de usos_consumo
  - Arquivo de Documentos individualizado
  - Dashboard
  - Cadastro e controle de quartos
  - Cadastro e controle de prestadores de servicos

Expansao Best Care:
> Versao Mobile para uso de Idosos e Cuidadores em residencia propria

🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

📋 Pré-requisitos
Instale a versão 3.x do **Python** :

Clone este repositório no propmt do CMD: 
>git clone https://github.com/giovanidalbosco/BestCare.git

🔧 Instalação
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






⚙️ Executando os testes
Explicar como executar os testes automatizados para este sistema.

🔩 Analise os testes de ponta a ponta
Explique que eles verificam esses testes e porquê.

Dar exemplos
⌨️ E testes de estilo de codificação
Explique que eles verificam esses testes e porquê.

Dar exemplos
📦 Implantação
Adicione notas adicionais sobre como implantar isso em um sistema ativo


Mencione as ferramentas que você usou para criar seu projeto

Dropwizard - O framework web usado
Maven - Gerente de Dependência
ROME - Usada para gerar RSS
🖇️ Colaborando
Por favor, leia o COLABORACAO.md para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

📌 Versão
Nós usamos SemVer para controle de versão. Para as versões disponíveis, observe as tags neste repositório.


Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

Um desenvolvedor - Trabalho Inicial - umdesenvolvedor
Fulano De Tal - Documentação - fulanodetal
Você também pode ver a lista de todos os colaboradores que participaram deste projeto.

📄 Licença
Este projeto está sob a licença (sua licença) - veja o arquivo LICENSE.md para detalhes.

🎁 Expressões de gratidão
Conte a outras pessoas sobre este projeto 📢;
Convide alguém da equipe para uma cerveja 🍺;
Um agradecimento publicamente 🫂;
etc.