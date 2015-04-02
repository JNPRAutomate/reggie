# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.define "testvm-reggie" do |testvm|
    testvm.vm.hostname = "Reggie-testvm"
    testvm.vm.box = "ubuntu/trusty64"

    testvm.vm.network "private_network",
      ip: "10.255.254.10",
      virtualbox__intnet: "reggie"
  
    testvm.vm.synced_folder ".", "/reggie", disabled: false
    
    testvm.ssh.username = "root"
    testvm.vm.provision "shell", inline: <<-SHELL
      sudo apt-get install software-properties-common
      sudo apt-get update -y
      sudo apt-get upgrade -y
      sudo apt-get install -y python-dev
      sudo apt-get install -y python-pip
      sudo pip install virtualenv
      sudo pip install virtualenvwrapper
    SHELL

    testvm.ssh.username = "vagrant"
    testvm.vm.provision "shell", privileged: false, inline: <<-SHELL
      mkdir ~/.virtualenvs
      export WORKON_HOME=~/.virtualenvs
      echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
      . /usr/local/bin/virtualenvwrapper.sh
      echo ". /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

      mkvirtualenv reggie
      cd /reggie
      pip install -r /reggie/requirements.txt
    SHELL

    testvm.vm.network "forwarded_port", guest: 5000, host: 18500
    testvm.vm.network "forwarded_port", guest: 8000, host: 18000
    testvm.vm.network "forwarded_port", guest: 80, host: 18080

  end
end
