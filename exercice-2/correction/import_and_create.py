import requests, csv, datetime, string, random

host = ''
token = ''

def get_random_string(length):
    characters = string.ascii_letters + string.digits + "!#?@"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Fonction réalisant l'appel API de création des comptes utilisateurs
def make_api_query(host,token,username,surname,name,password):

    # Définition des proxy
    proxies = {
        "http": "",
        "https": "",
    }

    # Définition du coeur de la requête
    body = {
        "jsonrpc": "2.0",
        "method": "user.create",
        "params": {
            "username": username,
            "surname": surname,
            "name": name,
            "passwd": password,
            "usrgrps": [
                {
                    "usrgrpid": "13"
                }
            ],
            "roleid": 1
        },
        "auth": token,
        "id": 1
    }


    api = "http://{}/zabbix/api_jsonrpc.php".format(host)
    x = requests.post(api, json = body, proxies = proxies)
    
    # Récupération du code retour de Zabbix
    response = x.json()
    if("error" in response.keys()):
        return response["error"]["data"]
    else:
        return "success"
    

# Chargement du fichier CSV
with open(__file__ + "\\..\\..\\listeUtilisateur.csv", newline="") as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        currDate = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        prenom = row['prenom']
        nom = row["nom"]
        username = prenom[0:2].upper() + nom[0:2].upper() + currDate
        password = get_random_string(10)
        status = make_api_query(host,token,username,nom,prenom,password)
        print('{} {} - Username: {} - password: {} - creation : {}'.format(prenom, nom, username, password,status))
