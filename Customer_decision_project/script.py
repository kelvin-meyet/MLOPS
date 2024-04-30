import requests

r = requests.get("https://www.linkedin.com")
print(r.status_code)

print(r.ok)
