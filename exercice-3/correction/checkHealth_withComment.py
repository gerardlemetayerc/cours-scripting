import requests, sys

# Récupération des paramètres de lignes de commande
tenantID = sys.argv[1]
secret = sys.argv[3]
appID = sys.argv[2]

# Initialisation de la requête à distination de Microsoft 365 pour obtenir le token
URL = "https://login.microsoftonline.com/{}/oauth2/v2.0/token".format(tenantID)
headers = { "Content-Type" : "application/x-www-form-urlencoded"}
body = {
    "scope"  : "https://graph.microsoft.com/.default",
    "grant_type" : "client_credentials", 
    "client_id" : appID,
    "client_secret" : secret
}


# Le bloc try permet de "capturer" les incidents de scripts et d'envoyer un retour géré.
try:
    # Récupération du token d'authentification pour les service Microsoft365
    token_request = (requests.post(URL, headers = headers, data = body))

    # Si le code de retour de la requête Web est 200, dans ce cas, on traite les étapes suivantes
    if(token_request.status_code == 200):
        # Extraction du token dans la réponse
        token = (token_request.json())["access_token"]

        # Préparation de la requête afin d'obtenir l'état des services M365
        url = 'https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews'
        headers = {'Authorization': 'Bearer ' + token}
        response = requests.get(url, headers=headers)

        # Si la requête est en succès, on continue.
        if(response.status_code == 200):
            # On retourne le contenu
            print(response.text)
        else:
            # On affiche le retour de la ligne de commande avec le code HTTP en cas d'erreur
            print("Erreur {} - {}".format(response.status_code,(response.json())["error"]["message"]))
    else:
        # Idem que précédemment
        print("Echec de récupération du token : {} - {}".format(token_request.status_code,(token_request.json())["error_description"]))
except:
    print("Oups, un évènement imprévu s'est produit")