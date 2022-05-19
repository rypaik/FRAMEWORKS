import requests

BASE = "http://127.0.0.1:5000/"
# for 02_main.py
# response = requests.get(BASE + "helloworld/Chris")


# for main.py
response = requests.get(BASE + "video/1", {"name": "Test video 1", "likes":10, "views":100})
print(response.json())
