import requests
import json
import time


def group_info():
    res = requests.get("https://production.collegeschedule.ru:2096/specialties/groups?offset=0&limit=500&specialtyId=0")
    with open("group_info.json", mode="w") as f:
        f.write(res.text)


url = "https://production.collegeschedule.ru:2096/schedule"
params = {
    'from': '1662940800',
    'to': '1663372800',
    'titles': 'true',
    'groupId': '24',
    'published': 'false'
}
response = requests.get(url, params=params).json()
