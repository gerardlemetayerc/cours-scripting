# Projet de fin de séance : mise en oeuvre d'une infrastructure de supervision et de d'exécution de job

## Contexte

Vous montez actuellement une startup d'infogérance ayant pour objectif de gérer les infrastructures cloud de clients finaux.

Votre objectif premier est de mettre en oeuvre une solution de supervision clef en main afin de récupérer les informations suivantes sur le Cloud de Microsoft 365, afin de faciliter votre capacity planning sur les licences utilisateurs :
* Supervision de l'état de santé des services de Microsoft 365

Afin de sécuriser votre environnement, il a été décidé de mettre en place un ordonnanceur sous Rundeck, qui aura pour objectifs pour le moment :
* Exécuter un script python de sauvegarde de base de donnes MySQL (celle de Zabbix et de Rundeck)
* Le script de sauvegarde devra conserver : un fichier par semaine sur 7 jours

La supervision devra egalement s'assurer que les jobs réalisées depuis votre serveur Rundeck soient fonctionnels.

## Rendu 

Vous devrez rendre :
* Un schéma d'architecture de votre infrastructure finale
* Une présentation de 15 minutes présentant votre solution et votre maquette.
