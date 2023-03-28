# Excercice 1 : Installation de Zabbix et premier usage des API

## Installation de Zabbix serveur

Installez Zabbix sur votre environnement à l'aide du mode opératoire d'installation : https://www.zabbix.com/fr/download

### Exemple d'installation sur Debian 11

* Installation des prérequis

```
wget https://repo.zabbix.com/zabbix/6.4/debian/pool/main/z/zabbix-release/zabbix-release_6.4-1+debian11_all.deb
sudo dpkg -i zabbix-release_6.4-1+debian11_all.deb
sudo apt update
sudo apt install mariadb-server zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

````

* Initalisation de la base de données
```
sudo mysql -uroot -p
mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin;
mysql> create user zabbix@localhost identified by 'password';
mysql> grant all privileges on zabbix.* to zabbix@localhost;
mysql> set global log_bin_trust_function_creators = 1;
mysql> quit;
zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix
sudo mysql -uroot -p
mysql> set global log_bin_trust_function_creators = 0;
mysql> quit;
```

* Configuration du mot de passe de la base de données dans Zabbix
```
sudo nano /etc/zabbix/zabbix_server.conf
DBPassword=password
```

* Initialisation des services et démarrage de zabbix
```
sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2
```

* Accédez à l'URL http://votreip/zabbix, les identifiants sont Admin / zabbix

## Générez le token API pour l'utilisateur administrateur

A l'aide du menu d'administration du token du compte administrateur, générez un token pour les appels APIs : http://votreip/zabbix/zabbix.php?action=user.token.list

## Générez un utilisateur a l'aide de l'API zabbix

Générez un compte utilisateur à l'aide d'un appel API. La documentation est disponible [ici]( https://www.zabbix.com/documentation/current/en/manual/api/reference/user/create).

La correction de cet exercice [ici](correction)
