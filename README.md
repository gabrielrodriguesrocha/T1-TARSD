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
1. POST: o cliente envia as informações sobre o container para o servidor
2. GET: o cliente recebe as informações armazenadas no servidor

As Requisições são feitas com seus respectivos nomes

