# Supervision des applications Microsoft 365

## Création du script de supervision

A l'aide de l'API graph de santé de Microsoft 365, réalisez un script python permettant de retourner le json contenant l'état de santé des services 365 associé à votre tenant. Ce script doit prendre en charge 3 paramètres :
* L'ID du tenant
* L'ID de l'application dans le tenant autorisant la supervision
* Le secret associé à l'application afin s'authentifier à Microsoft 365

- Lien vers la documentation de l'API : https://learn.microsoft.com/en-us/graph/api/servicehealth-get?view=graph-rest-1.0&tabs=http
- Méthode d'authentification : Oauth2 à l'aide d'un token

### Information complémentaires

```
POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token HTTP/1.1
Host: login.microsoftonline.com
Content-Type: application/x-www-form-urlencoded

client_id={clientID}
&scope=https://graph.microsoft.com/.default
&client_secret={secret}
&grant_type=client_credentials
```


## Intégration dans Zabbix

* Rendez-vous dans le fichier /etc/zabbix/zabbix_server.conf, et décommentez la ligne suivante :
```
ExternalScripts=/chemin/defaut/zabbix/external_script
```
* Assurez-vous que le chemin indiqué par le paramètre existe bien

* Redémarrez le service Zabbix
```
sudo systemctl restart zabbix-server
```

* Installez Python sur votre serveur ainsi que les prérequis liés à votre script
```
sudo apt install python3-pip
pip3 install requests
```

* Déployez votre script dans le répertoire précédemment décommenté.
 * **NB : si votre script a été développé depuis une machine Windows, n'oubliez pas d'ajouter en en-tête de votre script la ligne suivante :**
```
#!/usr/bin/env python3
```
 * **!! NB 2 : N'oubliez pas de rendre votre script exécutable !!**
