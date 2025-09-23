import requests
import pandas as pd


client_id = "d43fc53b-9a43-49c3-a2b2-f27fca2a29d4"

endpoint = "https://frost.met.no/observations/v0.jsonld"

parameters = {
    "sources": "SN18700",
    "referencetime": "2024-09-14/2025-09-14",
    "elements": "mean(air_temperature P1D)"
}

response = requests.get(endpoint, params=parameters, auth=(client_id, ""))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Feil ved henting:", response.status_code, response.text)