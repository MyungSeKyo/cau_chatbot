apt-get update;
apt-get install -y nginx;
apt-get install -y supervisor;
apt-get install -y python3;
apt-get install -y python3-pip;
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
pip3 install virtualenv;
virtualenv -p python3 $HOME/cau_chatbot/env;
./$HOME/cau_chatbot/env/bin/activate;
pip install -r $HOME/cau_chatbot/requirements.txt;
rm -rf /etc/nginx/sites-available/default;
ln -s $HOME/cau_chatbot/deploy/nginx.conf /etc/nginx/sites-available/default;
ln -s $HOME/cau_chatbot/deploy/supervisor.conf /etc/supervisor/conf.d/cau_chatbot.conf;
supervisorctl reread;
supervisorctl update;
supervisorctl start cau_chatbot;
service nginx restart;