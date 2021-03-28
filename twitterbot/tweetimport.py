from authcheck import api, user_id
import requests

url = f"https://api.twitter.com/2/users/{user_id}/mentions"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)
#print(response.text)
