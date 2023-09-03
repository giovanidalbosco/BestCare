# BestCare
## Sistema de Controle de Residentes internados em Casas de Repouso

### ✒️ Desenvolvedores / Responsabilidade
- Giovani Dalbosco - BackEnd Python
- Jackson Castellain - FrontEnd HTML/CCS/JS
- Lucas Rezende - BackEnd Python
- Samir Buhatem - Banco de Dados MySQL/SQlite3

#### ⚙️ Links de acesso
https://www.entra21-bestcare.heroku.app.com
https://github.com/giovanidalbosco/BestCare.git

#### 🛠️ Ferramentas utilizadas:
  - asgiref==3.5.2 : ASGI é um padrão para aplicativos e servidores da Web assíncronos do Python se comunicarem entre si e posicionado como um sucessor assíncrono do WSGI. Você pode ler mais em https://asgi.readthedocs.io/en/latest/ ;
  
  - backports.entry-points-selectable==1.1.0 : Fornece compatibilidade futura de pontos de entrada “selecionáveis” mesmo em versões mais antigas de importlib_metadata e importlib.metadata e evita o uso que aciona avisos de descontinuação ;
  
  - certifi==2022.6.15 : A Certifi fornece a coleção cuidadosamente selecionada de certificados raiz da Mozilla para validar a confiabilidade dos certificados SSL enquanto verifica a identidade dos hosts TLS ;
  
  - charset-normalizer==2.1.0 : Uma biblioteca que ajuda você a ler texto de uma codificação de conjunto de caracteres desconhecida ;
  
  - distlib==0.3.2 : Distlib é uma biblioteca que implementa funções de baixo nível relacionadas ao empacotamento e distribuição de software Python. Destina-se a ser usado como base para ferramentas de empacotamento de terceiros. A documentação está disponível em https://distlib.readthedocs.io/ ;
  
  - dj-database-url==1.0.0 : Este utilitário simples do Django permite que você utilize a variável de ambiente DATABASE_URL inspirada em 12 fatores para configurar seu aplicativo Django ;
  
  - Django==4.1 : Django é um framework web Python de alto nível que encoraja o desenvolvimento rápido e design limpo e pragmático ;
  
  - django-crispy-forms==1.14.0 : A melhor maneira de ter formulários Django DRY. Crie layouts programáticos reutilizáveis ​​a partir de componentes, tendo controle total do HTML renderizado sem escrever HTML em modelos. Tudo isso sem quebrar a forma padrão de fazer as coisas no Django, então funciona bem com qualquer outro aplicativo de formulário ;
  
  - django-heroku==0.3.1 : Esta é uma biblioteca Django para aplicativos Heroku que garante uma experiência de implantação e desenvolvimento perfeita ;

  - docopt==0.6.2 : cria interfaces de linha de comando ;

  - filelock==3.0.12 : Este pacote contém um único módulo, que implementa um bloqueio de arquivo independente de plataforma em Python, que fornece uma maneira simples de comunicação entre processos ;
 
  - gunicorn==20.1.0 : Gunicorn 'Green Unicorn' é um servidor HTTP WSGI Python para UNIX. É um modelo de trabalhador pré-fork portado do projeto Unicorn de Ruby ;
  
  - idna==3.3 : Suporte para o protocolo Internationalized Domain Names in Applications (IDNA) conforme especificado na RFC 5891 . Esta é a versão mais recente do protocolo e às vezes é chamada de “IDNA 2008” ;
  
  - mysql==0.0.3 : MySQL cria um banco de dados para armazenamento e manipulação de dados, definindo a relação de cada tabela. Clientes podem fazer solicitações digitando comandos SQL específicos no MySQL. A aplicação do servidor responde com a informação solicitada fazendo aparecer no cliente ; 
  
  - mysqlclient==2.1.1 : Este é um aplicativo cliente de banco de dados que serve como meio/interface entre o usuário executando códigos Python e o banco de dados mysql . mysqlclient foi desenvolvido para substituir o MySql-python e fornece suporte para Python3, embora também seja compatível com versões anteriores ;
  
  - num2words==0.5.10 : Normalização de texto inverso para números. Atualmente suporta apenas a localidade en-US ;
  
  - numpy==1.22.4 : NumPy é o pacote fundamental para computação de array com Python ;
  
  - pandas==1.4.2 : é uma biblioteca de código aberto licenciada pelo BSD que fornece estruturas de dados de alto desempenho e fáceis de usar e ferramentas de análise de dados para a linguagem de programação Python ;
  
  - platformdirs==2.2.0 : É um módulo único para que outros pacotes Python possam fornecer sua própria cópia privada ;

  - psycopg2==2.9.3 : O Psycopg 3 é uma implementação moderna de um adaptador PostgreSQL para Python ;

  - python-dateutil==2.8.2 : O módulo dateutil fornece extensões poderosas para o módulo datetime padrão ;
  
  - python-decouple==3.6 : O Decouple ajuda você a organizar suas configurações para que você possa alterar os parâmetros sem precisar reimplantar seu aplicativo ;

  - pytz==2022.1 : . Essa biblioteca permite cálculos de fuso horário precisos e entre plataformas usando Python 2.4 ou superior. Ele também resolve o problema de horários ambíguos no final do horário de verão, sobre o qual você pode ler mais na Referência da Biblioteca Python ( datetime.tzinfo ) ;

  - requests==2.28.1 : Requests permite enviar solicitações HTTP/1.1 com extrema facilidade. Não há necessidade de adicionar manualmente as strings de consulta aos seus URLs ou codificar seus dados PUT& POST- mas hoje em dia, basta usar o método json ;

  - six==1.16.0 : Um wrapper de API python para e621.net ;

  - sqlparse==0.4.2 : sqlparse é um analisador SQL sem validação para Python. Ele fornece suporte para análise, divisão e formatação de instruções SQL ;

  - tzdata==2022.2 : Este é um pacote Python contendo binários compilados em zic para o banco de dados de fuso horário da IANA. Destina-se a ser um substituto para sistemas que não possuem dados de fuso horário do sistema instalados (ou não os têm instalados em um local padrão), como parte do PEP 615 ;

  - urllib3==1.26.11 : Um pacote inofensivo para evitar ataques de typosquatting ;
  
  - virtualenv==20.7.2 : Uma ferramenta para criar ambientes python isolados ;
  
  - virtualenvwrapper-win==1.2.6 : uma ferramenta para criar ambientes virtuais Python isolados, cada um com suas próprias bibliotecas e pacotes de sites especialmente para Windows ;
  
  - whitenoise==6.2.0 : WhiteNoise permite que seu aplicativo web sirva seus próprios arquivos estáticos, tornando-o uma unidade independente que pode ser implantada em qualquer lugar sem depender de nginx, Amazon S3 ou qualquer outro serviço externo. (Especialmente útil no Heroku, OpenShift e outros provedores de PaaS).

#### ⌨️ História do usuário
- Sistema de gerenciamento para casas de repouso focado no residente. 
- Principais funcionalidades:
  - Agenda diária de atividades, medicamentos, consultas e exames;
  - Lembretes automáticos;
  - Armazenamento de histórico de rotinas (eventos) com retorno de previsibilidade de consumo de itens pessoais e remedios;
  - Controle de estoque individualizado por residente de itens de higiene e medicamentos;
  - Comunicação com responsável externo (log de saída) a confirmação de todos os eventos do residente com o log do responsável pela solução;
  - Dashboard.

#### Banco de Dados do projeto:

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

#### 💰 Beneficios:
  - Acompanhamento do residente em tempo real;
  - Lembretes instantaneos;
  - Gestao de estoque de medicamentos e itens de higiene;
  - Registro de ocorrencias anomalas;
  - Gestao de responsabilidade das prescricoes medicas;
  - Mensagens de intercorrencia instantaneas;
  - Melhor relacao entre Cuidador e Responsavel Externo.
  
#### 🚀 Futuro do Best Care:
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
  - Versao Mobile para uso de Idosos e Cuidadores em residencia propria

#### 📌 Versão
Nós usamos SemVer para controle de versão. Para as versões disponíveis, observe as tags neste repositório.

#### 📄 Licença
Este projeto está sob a licença
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007) - veja o arquivo LICENSE.md para detalhes.

#### 🎁 Gratidão
📢 Projeto desenvolvido em grupo, com os desenvolvedores acima mencionado, como trabalho de conclusao de curso do ENTRA21 edicao 2022; fica nosso agradecimentos aos mentores, coordenadores e ancoras do Entra21 pela oportunidade disponibizada.

🫂 Agradecimento especial ao professor e orientador Adriano Machado pelo empenho e dedicacao no processo de aprendizagem das melhores praticas e conceitos de programacao.