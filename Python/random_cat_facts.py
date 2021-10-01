import requests
import pprint as p

# a scraper that gets random cat facts from an api

url = "https://catfact.ninja/fact"

response = requests.get(url)



data = {
    "status_code": response.status_code,
    "content_type": response.headers["Content-Type"],
    "cat_fact": response.json()["fact"],
    "length_of_fact": response.json()["length"],
    "date": response.headers["Date"],
}

p.pprint(data)
