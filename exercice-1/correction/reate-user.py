import requests

token = ""
host = ""
username = ""
surname = ""
name = ""
password = ""
proxies = {
    "http": "",
    "https": "",
}

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

print(x)
