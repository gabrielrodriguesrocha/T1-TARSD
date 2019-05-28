# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "server" do |server|

 	server.vm.box = "ubuntu/bionic64"
 	server.vm.network "forwarded_port", guest: 9000, host: 9001
  	#server.vm.network "public_network"
    server.vm.network "private_network", ip: "192.168.50.2"
  	server.vm.hostname = "server"
  	server.vm.provider "virtualbox" do |vb|
      		vb.memory = "4096"
    	  	vb.name = "server"
    server.vm.provision :shell, path: "./server_setup.sh"
  	end
end
config.vm.define "client" do |client|

 	client.vm.box = "ubuntu/bionic64"
  	#client.vm.network "public_network"
    client.vm.network "private_network", ip: "192.168.50.3"
  	client.vm.hostname = "client"
  	client.vm.provider "virtualbox" do |vb|
      		vb.memory = "2048"
    	  	vb.name = "client"
    client.vm.provision :shell, path: "./server_setup.sh"
  	end
end
  config.vm.provision :shell, path: "./provision.sh"
end
