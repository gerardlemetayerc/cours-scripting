# Supervision des applications Microsoft 365

A l'aide de l'API graph de santé de Microsoft 365, réalisez un script python permettant de retourner le json contenant l'état de santé des services 365 associé à votre tenant. Ce script doit prendre en charge 3 paramètres :
* L'ID du tenant
* L'ID de l'application dans le tenant autorisant la supervision
* Le secret associé à l'application afin s'authentifier à Microsoft 365

- Lien vers la documentation de l'API : https://learn.microsoft.com/en-us/graph/api/servicehealth-get?view=graph-rest-1.0&tabs=http
- Méthode d'authentification : Oauth2 à l'aide d'un token

```
POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token HTTP/1.1
Host: login.microsoftonline.com
Content-Type: application/x-www-form-urlencoded

client_id={clientID}
&scope=https://graph.microsoft.com/.default
&client_secret={secret}
&grant_type=client_credentials
```
