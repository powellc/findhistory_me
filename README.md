[InteractiveHistory.me](http://mainecivichackday.github.io/interactivehistory_me/)
=====================

Bangor History Museum wants a website. They also have 40,000 unique historical artifacts.
Can we do anything cool with this? Probably ;-)

Goal
-----

Allow users to connect to a website, and view historical artifacts relevant to their current
location. Perhaps especially historical photos.

Proposal
--------
 
Archiving information is a done deal. We can store data very easily in all kinds of ways. 
But what about providing ways for people to FIND history? This should actually be a 
solvable problem. Location-based data, HTML5 location-aware browsers, and cell connections.

  1. Backend data store - currently going with Flask talking to [Riak](http://docs.basho.com/riak/latest/)
  2. Admin interface to input data - using [AngularJS](http://docs.angularjs.org)
  3. Lookup missing GIS coordinates if we only have addresses
  4. Solr-backend for proximity queries - using [Yokozuna project](https://github.com/basho/yokozuna) for Solr+Riak integration
  5. Very basic front end to display artifacts relevant to the current location

Installation (on EC2)
---------------------
  1. Install dependencies:
     ```sudo apt-get install build-essential libncurses5-dev openssl libssl-dev fop xsltproc unixodbc-dev git```
  2. [Install Erlang from source](http://docs.basho.com/riak/latest/tutorials/installation/Installing-Erlang/#Installing-on-GNU-Linux):
    - ```mkdir erlang; cd erlang```
    - ```curl -O https://raw.github.com/spawngrid/kerl/master/kerl; chmod a+x kerl```
    - ```./kerl build R15B02 r15b02```
    - ```./kerl install r15b02 ~/erlang/r15b02```
    - ```. ~/erlang/r15b02/activate```
    - (Feel free to add ```. ~/erlang/r15b02/activate``` to your user's .bashrc)
  5. Install JRE 1.6 or later: ```sudo apt-get install default-jre```
  4. [Install Yokozuna](https://github.com/basho/yokozuna/blob/master/docs/INSTALL.md):
    - ```wget http://data.riakcs.net:8080/yokozuna/riak-yokozuna-0.6.0-src.tar.gz```
    - ```tar xvzf riak-yokozuna-0.6.0-src.tar.gz``` and ```cd riak-yokozuna-0.6.0-src```
    - ```make```
    - ```make stage```
  5. Increase the [Open File limit](http://docs.basho.com/riak/latest/cookbooks/Open-Files-Limit/#Linux):
     Edit ```/etc/security/limits.conf``` and append the following lines to the file:
      ```
       *               soft     nofile          65536
       *               hard     nofile          65536
      ```
  6. Update the ```rel/riak/etc/app.config``` file, set n=1, enable yokozuna, 
     increase ```solr_startup_wait``` time (it was timing out on an EC2 micro).
     