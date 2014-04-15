# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.ssh.forward_agent = true

    config.vm.define "devbox" do |dev|
      dev.vm.box = "precise64"
      dev.vm.box_url = 'http://files.vagrantup.com/precise64.box'
      dev.vm.network "private_network", ip: "192.168.100.11"
      dev.vm.network "forwarded_port", guest: 80, host: 8011

      dev.vm.provision "ansible" do |ansible|
          ansible.playbook = "ansible/vagrant.yml"
          ansible.sudo = true
          ansible.ask_sudo_pass = true
          ansible.inventory_path = "ansible/local_hosts"
          ansible.host_key_checking = false
          ansible.verbose = 'vv'
          ansible.limit = 'all'
      end
    end

end
