
change ip in src back.conf front.conf __
change allowed host in back-end setting __
sftp -i privatekey.pem ubuntu@ip  __
put -r Back-end Front-end backup.sql .htaccess front.conf back.conf apache2.conf ports.conf  __
ssh -i private-key.pem ubuntu@ip __
sudo apt update __
sudo apt install mysql-server __
sudo mysql  __
CREATE DATABASE testdb; __
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456789'; __
exit __
sudo apt install nodejs npm pip apache2 python3 python3-pip  -y __
sudo ufw app list __
sudo ufw allow 'Apache' __
sudo ufw allow 'OpenSSH' __
sudo ufw allow 8000 __
sudo ufw enable  __
sudo ufw status  __
sudo systemctl status apache2  __
exit __
cd /var/www/ __
sudo mkdir main __
cd ~  __
mysql -u root -p testdb < backup_testdb.sql __
sudo mv apache2.conf /etc/apache2/ __
sudo mv ports.conf /etc/apache2/ __
sudo mv back.conf /etc/apache2/sites-available/ __
sudo mv front.conf /etc/apache2/sites-available/ __
sudo mv Back-end/ /var/www/main/ __
sudo mv Front-end/ /var/www/main/ __
sudo mv htaccess_deltename.htaccess /var/www/main/Front-end/.htaccess __
cd /etc/apache2/sites-available/ __
check site by ip  __
sudo  apt-get install libapache2-mod-wsgi-py3 -y __
sudo a2dissite 000-default.conf __
sudo a2ensite back.conf __
sudo a2ensite front.conf __
sudo systemctl restart apache2 __
cd /var/www/main/Back-end __
source venv/bin/activate __
sudo apt install libsystemd-dev pkg-config libmysqlclient-dev libyaml-dev libcairo2-dev gcc python3-dev -y __
sudo pip install pkgconfig __
sudo pip install --upgrade pyyaml __
sudo pip install wheel __
sudo pip install -r requirements.txt __
cd /var/www/main/Back-end/ __
python3 manage.py runserver 9000 __
python3 manage.py makemigrations  __
python3 manage.py migrate  __
cd /var/www/main/ __
sudo chmod -R 777 Back-end/ __
deactivate __
cd /var/www/main/Front-end/ __
npm install --force  __
npm run build __
sudo a2enmod wsgi __
sudo a2enmod rewrite __
sudo systemctl restart apache2  __



























