# ubuntu server 18.04 기준
apt-get update;
apt-get install -y nginx;
apt-get install -y supervisor;
apt-get install -y virtualenv;
virtualenv -p python3 $HOME/cau_chatbot/env;
.$HOME/cau_chatbot/env/bin/activate;
pip install -r $HOME/cau_chatbot/requirements.txt;
rm -rf /etc/nginx/sites-available/default;
ln -sf $HOME/cau_chatbot/deploy/nginx.conf /etc/nginx/sites-available/default;
ln -sf $HOME/cau_chatbot/deploy/supervisor.conf /etc/supervisor/conf.d/cau_chatbot.conf;
supervisorctl reread;
supervisorctl update;
service nginx restart;
