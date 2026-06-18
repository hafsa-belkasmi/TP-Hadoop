import requests

url = "https://factcheck.afp.com/"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text[:500])