[findhistory.me](http://http://23.21.88.45/)
=====================

Bangor History Museum wants a website. They also have 40,000 unique historical artifacts.
Can we do anything cool with this? Probably ;-)

Check out the alpha: http://23.21.88.45/

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
    - ```make stagedevrel```
    - ```cd dev```
  5. At this point, you have the potential to run 4 Riak nodes locally -- dev1, dev2, dev3, dev4.
    The 'devrel' Riak release is used for developers to run a mini-cluster on their local machines.
    We obviously don't want to do this in production -- for our demo purposes, we're just going to 
    use the ```dev1`` node.
    So:
    ```cd dev1```
  6. Increase the [Open File limit](http://docs.basho.com/riak/latest/cookbooks/Open-Files-Limit/#Linux):
     Edit ```/etc/security/limits.conf``` and append the following lines to the file:

      ```
      *               soft     nofile          65536
      *               hard     nofile          65536
      ```

  7. Update the ```etc/app.config``` file, set n=1, enable yokozuna, 
     increase ```solr_startup_wait``` time (it was timing out on an EC2 micro).
     See the sample [app.config](https://github.com/mainecivichackday/interactivehistory_me/blob/master/riak_config/app.config)
     file in this repo.
  8. Start Riak: ```bin/riak start```
     
Testing Riak+Solr installation
------------------------------
  1. ```cd ~/riak-yokozuna-0.6.0-src/dev/dev1```
  2. Send a "riak ping": ```bin/riak ping```
    Should respond with: ```pong```
  3. Test out the HTTP interface:
    ```curl http://127.0.0.1:10018/ping```
    Should return: ```OK```
    Note: 10018 is the HTTP api port for this particular Riak installation (you can check to see 
    what port yours listens on by doing ```cat etc/app.config | grep http```.
  4. Try a read/write test: ```bin/riak-admin test```
    Should get back:
    ```Successfully completed 1 read/write cycle to 'riak@127.0.0.1'```

Enabling Solr search/indexing on a Riak bucket
----------------------------------------------
Now that Yokozuna has been installed and enabled in the ```app.config```, 
a Solr index must be created for each individual bucket (that you want to be able to search).
For example, if we're storing our museum exhibits in an ```exhibits``` bucket:

```curl -XPUT -i -H 'content-type: application/json' http://127.0.0.1:10018/yz/index/exhibits```

The above line enables Solr indexing on that bucket. (With a default schema).

