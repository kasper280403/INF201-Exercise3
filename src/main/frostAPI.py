import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

params_aas = set_parameters("SN17850", "2024-09-14/2025-09-14", "mean(air_temperature P1D)")
aas_df = request_response(client_id, endpoint, params_aas)

blindern_df["date"] = pd.to_datetime(blindern_df["date"])
aas_df["date"] = pd.to_datetime(aas_df["date"])

plt.plot(blindern_df["date"], blindern_df["value"])
plt.plot(aas_df["date"],aas_df["value"])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # én tick per måned
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # format som ÅÅÅÅ-MM
plt.xticks(rotation=45)

plt.show()

merged_df = pd.merge(blindern_df, aas_df, on="date", suffixes=("_blindern", "_aas"))

# Lag scatterplot
plt.scatter(merged_df["value_blindern"], merged_df["value_aas"], color="green")
plt.xlabel("Blindern temperatur (°C)")
plt.ylabel("Aas temperatur (°C)")
plt.title("Sammenligning av daglig gjennomsnittstemperatur")
plt.grid(True)
plt.show()