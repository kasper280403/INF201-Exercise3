import requests
import pandas as pd

client_id = "d43fc53b-9a43-49c3-a2b2-f27fca2a29d4"
endpoint = "https://frost.met.no/observations/v0.jsonld"


def set_parameters(sources, referencetime, elements):
    parameters = {
        "sources": sources,
        "referencetime": referencetime,
        "elements": elements
    }

    return parameters

def request_response(client_id, endpoint, parameters):
    response = requests.get(endpoint, params=parameters, auth=(client_id, ""))
    if response.status_code == 200:
        data = response.json()
        records = []
        for item in data.get("data", []):
            date = item["referenceTime"][:10]
            for obs in item["observations"]:
                records.append({
                    "date": date,
                    "value": obs["value"],
                    "unit": obs["unit"]
                })

        return pd.DataFrame(records)

    else:
        print("Error retrieving data:", response.status_code, response.text)

params_blindern = set_parameters("SN18700", "2024-09-14/2025-09-14", "mean(air_temperature P1D)")
blindern_df = request_response(client_id, endpoint, params_blindern)

print(blindern_df.head(20))