# CHATTER

This is a cloud based chatforum app written by Brady Ibanez for SOFE 4630U - Cloud Computing - Assignment 1. It as an app 
based on the premise of guess chatting with other active users for the fact that recently active users and the chatrooms
used can be seen, but during chatting within a known room, there is no means of seeing who is in the room, or who may have
sent a recently received message, for that matter. While the later is possible, and attainable through simple Django development, the main focus is to exemplify cloud based server config on a Linux VM including synchronous, and asychronous Websocket call interation. This was done without issue with the feature of guess chatting alone. 

## Getting Started

In order to run in a cloud VM, as is done currently @ http://assignmentunochat.tk, it is necessary to install nginx,
redis, uwsgi, and daphne servers and run them concurrently through server configuration provided in the /ServerConfig folder kept within this /src directory. All of the files included in /ServerConfig should be in your Ubuntu VM before starting of the servers. It is also necessary that the cloud VM run is an Ubuntu VM running version 16.04. To install these servers, run in your Ubuntu terminal:

1) $ sudo apt-get update
  - required to update all included packaging within the Ubuntu machine prior to installation os server

2) $ sudo apt-get install nginx
  - implementing nginx within the Ubuntu VM

3) $ sudo apt-get install redis-server
  - implementing redis within the Ubuntu VM
  
4) $ sudo apt-get install build-essential python

5) $ apt-get install python-dev
  - 4/5 required for Django implementation of uWSGI/Daphne
  
6) $ sudo ln -s /etc/nginx/sites-available/ /etc/nginx/sites-enabled
  - creates necessary connection between config files outlined in /ServerConfig for uwsgi/daphne/redis connection, etc.

These commands are all that is required. You may be wondering how Daphne and uWSGI come into play. 

Daphne inclussion is provided through Django once the C and Python compiler interfacing becomes possible through the python-dev packaging of steps 4 and 5. In order to install, you would simply run $ pip3 install daphne and the same with uwsgi, however, this is included in python virtualenv provided here.  

uWSGI is inate to Django via their wsgi.py This is also taken care of in the Django configuration provided within the virtualenv of this repository.  

## Configure Django with your cloud IP/domain

In order to be referenced from within the cloud Ubuntu VM, all that is needed to be done is reassigning of the ALLOWED_HOSTS within the /chatter/settings.py file from this current /src directory. As stands, the current 

ALLOWED_HOSTS = ['178.128.239.207', 'assignmentunochat.tk']

makes it possible for users to access the app at the existing configured DigitalOcean Ubuntu VM through either above mentioned URL request. 

## Deployment

In order to deploy Chatter, the above given server and Django configuration should be entirely sufficient. If everything is installed and the directory hierarchy remains the same as that outline here, simply check the IP or domain pertaining to your cloud VM and you should be good to go.  

All servers are governed by a supervisor script outlined also in the /ServerConfig folder. If it is seen that either Daphne or uWSGI have failed, the supervisor will run their start commands automatically again to bring them back. 

Should any errors arrise, from either the synchronous Http side or the asynchronous Websocket side, the following commands can be run depending on the issue to bring the app back:

- systemctl restart nginx
- systemctl restart uwsgi
- systemctl daemon-reload (for daphne restart)

For those not interested in working to deploy, as previously mentioned, the app is available at http://assignmentunochat.tk

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Nginx](https://www.nginx.com/) - The overarching URL request server
* [Redis](https://redis.io/) - Used to queue requests provided by Nginx for Daphne and uWSGI
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) - Synchoronous Http request responding server
* [Daphne](http://manpages.ubuntu.com/manpages/bionic/man1/daphne.1.html) - Asynchronous Websocket responding server
* [Django Channels](https://channels.readthedocs.io/en/latest/) - Mechanism for asychronous chat room user.py object development and implementation

## Authors

* **Brady Ibanez** - *Cloud based implementation and app functionality* 
