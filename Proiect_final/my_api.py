import requests

url = "https://holidays.abstractapi.com/v1/?api_key=ce278d49b20d447989c988dcea7f3177&country=US&year=2020&month=12&day=25"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
gi