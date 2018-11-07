# -*- mode: ruby -*-
# # vi: set ft=ruby :

unless File.exists?("id_rsa")
  system("ssh-keygen -t rsa -f id_rsa -N '' -q")
end

Vagrant.configure("2") do |config|
  config.vm.provider :virtualbox do |vb|
      vb.memory = 1024
      vb.name = "OracleLinuxML"
      vb.cpus = 1
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vb.customize ["modifyvm", :id, "--nictype2", "virtio"]  
  end
  config.ssh.forward_agent = true
  config.vm.box = "ol74"
  config.vm.box_url = "http://yum.oracle.com/boxes/oraclelinux/ol74/ol74.box"
  config.vm.hostname = "OracleLinuxML"
  config.vm.network "private_network", ip: "192.168.56.125", netmask: "255.255.255.0"
  #Uploading files I need for my ML demo
  config.vm.provision "file", source: "~/OracleLinuxML/files", destination: "/tmp/"
  config.vm.provision :shell, path: "bootstrap.sh" 
end
