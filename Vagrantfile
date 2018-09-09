# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
   config.vm.provision "shell", inline: <<-SHELL
     yum -y install epel-release
     yum -y update
     yum -y groupinstall Development Tools
     yum -y install \
      libcurl-devel \
      openssl-devel \
      python34 \
      python34-devel \
      python34-pip \
      python34-pycurl \
      python34-numpy \
     && echo all done!
     cd /vagrant/
     pip3 install --upgrade pip
     pip3 install -r requirements.txt
     
   SHELL

end
