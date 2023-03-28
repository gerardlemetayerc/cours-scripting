import requests, sys

tenantID = sys.argv[1]
secret = sys.argv[3]
appID = sys.argv[2]

URL = "https://login.microsoftonline.com/{}/oauth2/v2.0/token".format(tenantID)
headers = { "Content-Type" : "application/x-www-form-urlencoded"}

body = {
    "scope"  : "https://graph.microsoft.com/.default",
    "grant_type" : "client_credentials", 
    "client_id" : appID,
    "client_secret" : secret
}

token_request = (requests.post(URL, headers = headers, data = body))

if(token_request.status_code == 200):
    token = (token_request.json())["access_token"]
    url = 'https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    if(response.status_code == 200):
        print(response.json())
    else:
        print("Erreur {} - {}".format(response.status_code,(response.json())["error"]["message"]))
else:
    print("Echec de récupération du token : {} - {}".format(token_request.status_code,(token_request.json())["error_description"]))