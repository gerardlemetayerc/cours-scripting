$token = ""
$name = ""
$username
$surname = ""
$password = ""
$token = ""
$host = ""

$body = @"
{
    "jsonrpc": "2.0",
    "method": "user.create",
    "params": {
        "username": $username,
        "name": $name,
        "surname": $surname,
        "passwd": $password,
        "usrgrps": [
            {
                "usrgrpid": "13"
            }
        ],
        "roleid": 1
    },
    "auth": $token,
    "id": 1
}
"@

(Invoke-RestMethod -ContentType "application/json" -Method POST -Body $body -Uri "http://$host/zabbix/api_jsonrpc.php")
