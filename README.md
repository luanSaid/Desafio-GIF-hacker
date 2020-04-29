# Desafio-GIF-hacker 

Os hackers do mundo inteiro discutem diariamente pela deep web, porém na última semana chegaram a um impasse: qual é o GIF que melhor representa a cultura hacker? Para resolver isso, um anônimo corajoso se ofereceu a criar um software pra resolver isso de uma vez, para que todos possam voltar a tentar hackear os servidores da NASA e fazer regadores de planta com Arduino.  Surpresa: FOI O LUAN SAID. O trabalho dele é criar um projeto em Django, que vai captar os melhores GIFs hacker da internet, e vai mostrá-los em uma página para votação, contendo a imagem GIF, o número de votos que ele recebeu até agora, e dois botões: vote up (+1) e vote down (-1).

Requisitos:
- Hackers precisam ser organizados, então use o git (sugestão de server: gitlab) para versionamento;
- Tenha um arquivo README na raiz do projeto, explicando em detalhes como rodá-lo. Aproveite para explicar suas decisões de projeto aqui;
- Use a API REST de https://tenor.com/gifapi/documentation#quickstart-search para pegar os 20 primeiros GIFs com a palavra "hacker";
- Os hackers do mundo esperam ter acesso à apenas uma tela: a tela principal (index), com os GIFs "hacker" ordenados decrescente pelo número de votos, os botões de votação e o número de votos de cada GIF;
- Você não precisa implementar paginação: mostre todos os GIFs na mesma página. Também não precisa de autenticação: qualquer um pode votar quantas vezes quiser.

Você vai ser avaliado pelos seguintes itens:
- Capacidade e qualidade de uso do git;
- Pensamento analítico;
- Integração com a API;
- Modelagem do sistema;
- Qualidade da interface.

# Preparação do ambiente para a execução do projeto:

Antes de darmos início ao passo ao passo, se liga nos pré requisitos para executar o sistema:
>> Ter a versão do Python 3 instalada na sua máquina.

**Passo 1: Instalar o django**
>> $ python3 -m pip install Django

Obs: Problemas? Para resolução de dúvidas, acesse a documentação oficial de instalação do Django em: https://docs.djangoproject.com/en/3.0/topics/install/


**Passo 2: Executar o projeto**
>> $ cd local_onde_o_repositorio_foi_instalado/gif_hacker
>> $ python3 manage.py runserver








