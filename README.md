
change ip in src back.conf front.conf\
change allowed host in back-end setting \
sftp -i privatekey.pem ubuntu@ip \
put -r Back-end Front-end backup.sql .htaccess front.conf back.conf apache2.conf ports.conf \
ssh -i private-key.pem ubuntu@ip \
sudo apt update \
sudo apt install mysql-server \
sudo mysql  \
CREATE DATABASE testdb; \
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456789'; \
exit \
sudo apt install nodejs npm pip apache2 python3 python3-pip  -y \
sudo ufw app list \
sudo ufw allow 'Apache' \
sudo ufw allow 'OpenSSH' \
sudo ufw allow 8000 \
sudo ufw enable  \
sudo ufw status  \
sudo systemctl status apache2  \
exit \
cd /var/www/ \
sudo mkdir main \
cd ~  \
mysql -u root -p testdb < backup_testdb.sql \
sudo mv apache2.conf /etc/apache2/ \
sudo mv ports.conf /etc/apache2/ \
sudo mv back.conf /etc/apache2/sites-available/ \
sudo mv front.conf /etc/apache2/sites-available/ \
sudo mv Back-end/ /var/www/main/ \
sudo mv Front-end/ /var/www/main/ \
sudo mv htaccess_deltename.htaccess /var/www/main/Front-end/.htaccess \
cd /etc/apache2/sites-available/ \
check site by ip  \
sudo  apt-get install libapache2-mod-wsgi-py3 -y \
sudo a2dissite 000-default.conf \
sudo a2ensite back.conf \
sudo a2ensite front.conf \
sudo systemctl restart apache2 \
cd /var/www/main/Back-end \
source venv/bin/activate \
sudo apt install libsystemd-dev pkg-config libmysqlclient-dev libyaml-dev libcairo2-dev gcc python3-dev -y \
sudo pip install pkgconfig \
sudo pip install --upgrade pyyaml \
sudo pip install wheel \
sudo pip install -r requirements.txt \
cd /var/www/main/Back-end/ \
python3 manage.py runserver 9000 \
python3 manage.py makemigrations  \
python3 manage.py migrate \
cd /var/www/main/ \
sudo chmod -R 777 Back-end/ \
deactivate \
cd /var/www/main/Front-end/ \
npm install --force \
npm run build \
sudo a2enmod wsgi \
sudo a2enmod rewrite \
sudo systemctl restart apache2 \



























