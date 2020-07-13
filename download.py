import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
print(res.text[:100])