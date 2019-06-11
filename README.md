# T1-TARSD
O atual projeto é uma prova de conceito para a disciplina de Tópicos Avançados em Redes e Sistemas Distribuídos.

Pré Requisitos:
1. [Vagrant 2.2.4](https://www.vagrantup.com/) ou recente

# Execução

```
vagrant up
```
Acessar os host dos containers criados pelo vagrant

```
vagrant ssh [client | server]
```

No host do container client executar:
```
docker run -it app_client
```
O cliente deste projeto pode chamar duas requisições REST
1. POST: o cliente envia as informações sobre o *container* para o servidor
2. GET: o cliente recebe as informações armazenadas no servidor

As Requisições são feitas com seus respectivos nomes

# Desenvolvimento

Inicialmente foram feitas as imagens das aplicações de *client* e *server*.

As pastas ```docker_client``` e ```docker_server``` contém os arquivos construídos para construção das imagens que são executadas no *client* e *server*, respectivamente. Ambas imagens são estendidas da imagem  ```python``` do repositório oficial do Docker:

- ```docker_client```:
  - o arquivo ```info_server.py``` descreve um servidor simples que permite que o container descrito pela Dockerfile possa solicitar informações sobre si mesmo através da Docker SDK for Python. Esse arquivo não é incluso na imagem descrita pela Dockerfile.
  - a Dockerfile presente instala os requisitos da aplicação e cria um container que age como um "prompt" interativo que permite envio de requisições GET e POST para um servidor - no caso, para a máquina virtual *server* e para o servidor de informações.
  
- ```docker_server```:
  - a Dockerfile presente, novamente, instala os requisitos da aplicação e cria um container e cria um servidor REST simplificado para armazenamento de informações através do pacote ```bottle```.

Foi feito, então, um Vagrantfile com as configurações de duas máquinas virtuais, *client* e *server* conforme as especificações requisitadas.

Então três scripts de provisionamento foram construídos, um comum para as duas máquinas virtuais e um específico para cada uma.
- ```provision.sh```: 
  - instala o Docker;
  - clona este repositório dentro das máquinas;
- ```server_setup.sh```: 
  - inicializa o *swarm* no servidor, colocando o comando para *join* no repositório compartilhado do Vagrant; 
  - cria a imagem do Docker para o serviço do servidor, bem como um volume para que o banco de dados seja compartilhado entre os containers do serviço;
  - e finalmente inicializa o serviço publicando-o na porta 5001 com três réplicas;
- ```client_setup.sh```: 
  - executa o comando para se juntar ao *swarm* do servidor;
  - cria a imagem do Docker da aplicação;
  - executa o servidor de informações sobre os *containers* executando na máquina.
