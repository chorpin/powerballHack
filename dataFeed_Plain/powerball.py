import requests

url = "https://powerball.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": "9302947c6amsh47bc60d44fa1619p1c393cjsn28439cdc9a65",
    "X-RapidAPI-Host": "powerball.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
