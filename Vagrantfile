Vagrant::Config.run do |config|
  config.vm.box     = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network :hostonly, '11.0.0.10'  
  config.vm.forward_port 80, 8085
  config.vm.customize ["modifyvm", :id, "--memory", "256"]
  config.vm.customize ["modifyvm", :id, "--cpus", "1"]

  #config.vm.share_folder("vagrant-root", "/vagrant", ".", :nfs => true)

  config.vm.provision :ansible do |ansible|
    ansible.inventory_file = "deploy/hosts"
    ansible.extra_vars = { vm:1 }
    ansible.playbook = "deploy/provision.yml"
  end
end