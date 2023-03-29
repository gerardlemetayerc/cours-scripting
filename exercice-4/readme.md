# Supervision des licences et de la synchronisation Azure AD

L'objectif de cet exercice : superviser à l'aide des API Graph les licences Microsoft 365 ainsi que la synchronisation Azure AD.

Les APIs à utiliser : 
* https://graph.microsoft.com/v1.0/subscribedskus
* https://graph.microsoft.com/v1.0/organisation

Faites en sorte qu'en définitve la supersivion ne soit gérée que par un seul script python, en prenant en compte un paramètre supplémentaire (le type d'API à appeler)