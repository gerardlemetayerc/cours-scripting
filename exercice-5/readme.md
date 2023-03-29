# Installation de l'ordonnanceur Rundeck

Pour installer Rundeck, plusieurs choix possibles :
* Vous êtes dans un environnement "docker" : utilisez l'image : https://docs.rundeck.com/docs/administration/install/docker.html
* Sinon, utilisez le package de déploiement relatif à votre environnement

## Exemple d'installation sur une machine Debian 11

* Installation des prérequis 
```
sudo apt install curl openjdk-11-jre-headless
```

* Configuration de APT et déploiement du package
```
curl -L https://packages.rundeck.com/pagerduty/rundeckpro/gpgkey | sudo apt-key add -
echo "deb https://packages.rundeck.com/pagerduty/rundeck/any/ any main
deb-src https://packages.rundeck.com/pagerduty/rundeck/any/ any main" | sudo tee -a /etc/apt/sources.list.d/rundeck.list
sudo apt update
sudo apt install rundeck
```

* Initialisation de la base de données
```
mysql -u root -p
create database rundeckdb;
create user rundeck@localhost identified by 'password';
grant all on rundeckdb.* to rundeck@localhost;
flush privileges;
quit;
```

* Configuration des fichiers

**/etc/rundeck/framework.properties**
```
framework.server.name = <votreip>
framework.server.hostname = <votreip>
framework.server.port = 4440
framework.server.url = http://<votreip>:4440
```

**/etc/rundeck/rundeck-config.properties**
```
[...]
# change hostname here
grails.serverURL=http://<votreip>:4440
dataSource.driverClassName = org.mariadb.jdbc.Driver
dataSource.url = jdbc:mysql://localhost/rundeckdb?autoReconnect=true&useSSL=false
dataSource.username = rundeck
dataSource.password = password


#dataSource.dbCreate = none
#dataSource.url = jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;DB_CLOSE_ON_EXIT=FALSE;NON_KEYWORDS=MONTH,HOUR,MINUTE,YEAR,SECONDS
#grails.plugin.databasemigration.updateOnStart=true

# Encryption for key storage
```

* Initialisation de rundeck
```
systemctl enable rundeckd
systemctl start rundeckd
```

* Vérification de la base SQL
```
mysql -uroot -p
CONNECT rundeckdb;
SHOW TABLES;
+----------------------------+
| Tables_in_rundeckdb        |
+----------------------------+
| DATABASECHANGELOG          |
| DATABASECHANGELOGLOCK      |
| auth_token                 |
| base_report                |
| execution                  |
| job_file_record            |
| log_file_storage_request   |
| node_filter                |
| notification               |
| orchestrator               |
| plugin_meta                |
| project                    |
| rdoption                   |
| rduser                     |
| referenced_execution       |
| report_filter              |
| scheduled_execution        |
| scheduled_execution_filter |
| scheduled_execution_stats  |
| storage                    |
| stored_event               |
| webhook                    |
| workflow                   |
| workflow_step              |
| workflow_workflow_step     |
+----------------------------+
25 rows in set (0,001 sec)
```

* Debug en cas de démarrage en échec :

Le fichier de log de rundeck se trouve dans **/var/log/rundeck/service.log** pour la partie démarrage du service.