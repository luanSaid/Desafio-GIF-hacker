# Desafio GIF hacker 
Os hackers do mundo inteiro discutem diariamente pela deep web, porém na última semana chegaram a um impasse: qual é o GIF que melhor representa a cultura hacker? Para resolver isso, um anônimo corajoso se ofereceu a criar um software pra resolver isso de uma vez, para que todos possam voltar a tentar hackear os servidores da NASA e fazer regadores de planta com Arduino.  Surpresa: FOI O LUAN SAID. O trabalho dele foi criar um projeto em Django, que capta os melhores GIFs hacker da internet, e os mostra em uma página para votação, contendo a imagem GIF, o número de votos que ele recebeu até agora, e dois botões: vote up (+1) e vote down (-1).

# Sobre o sistema
Também conhecido como Central de GIF Hacker (CGH), o CGH como abordado anteriormente teve o back-end programado com o simples e prático framework Django, o banco de dados nativo: SQLite, o front-end em HTML5 e CSS3 e o consumo da API de gifs Tenor. Visando uma boa experiencia para o usuário (UX) o sistema conta com uma interface responsiva, isto é, um fácil acesso para diferentes dispositivos e navegadores da web. Ademais, para um carregamento mais rápido e eficiente dos gifs, apenas os votos são efetivamente carregados da base de dados, os gifs após a requisição são temporariamente armazenados, apenas para fins de visualização. Mas fique traquil@, os votos estarão sempre seguros e salvos, a aplicação foi modelada pensando justamente nisso! Agora cabe a você hacker, votar nos seus gifs favoritos!

# Preparação do ambiente para a execução do projeto:
Antes de darmos início ao passo ao passo, se liga nos pré requisitos para executar o sistema:
>> Ter a versão do Python 3 instalada na sua máquina.

Abra um terminal de sua preferência e execute os passos abaixo:

**Passo 1: Instalar o django**
>> $ python3 -m pip install Django

Obs: Problemas? Para resolução de dúvidas, acesse a documentação oficial de instalação do Django em: https://docs.djangoproject.com/en/3.0/topics/install/

**Passo 2: Clonar repositório**
>> $ git clone https://github.com/luanSaid/Desafio-GIF-hacker.git

**Passo 3: Entrar na pasta clonada**
>> $ cd Desafio-GIF-hacker/gif_hacker

**Passo 4: Executar o projeto**
>> $ python3 manage.py runserver

**Passo 5: Acessar o endereço da aplicação**
Se tudo ocorreu bem, essa é a etapa final, e ao executar o comando acima o servidor irá emitir uma mensagem similar a:

>> $ System check identified no issues (0 silenced).
>> $ April 29, 2020 - 18:22:14
>> $ Django version 3.0.5, using settings 'gif_hacker.settings'
>> $ Starting development server at http://127.0.0.1:8080/
>> $ Quit the server with CONTROL-C

**Altere** o endereço de http://127.0.0.1:8080/  **para** http://127.0.0.1:8080/polls copie e cole na barra de URL do seu navegador.

**Observações**:  
Ao iniciar o projeto, o banco de dados estará vazio, pronto para começar a receber as votações dos GIF's hacker.







