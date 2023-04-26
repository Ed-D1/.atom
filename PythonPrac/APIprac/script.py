import requests
response = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json
")

print(response.text)
