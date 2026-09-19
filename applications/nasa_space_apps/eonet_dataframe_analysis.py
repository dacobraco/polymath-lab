import requests
import pandas as pd

url = "https://eonet.gsfc.nasa.gov/api/v3/events"

params = {
    "category": "wildfires",
    "status": "open",
    "days": 10,
    "limit": 3
}

response = requests.get(url, params=params)
data = response.json()
events = data["events"]

print("There are", len(events), "events.")

rows = []

for event in events:
    title = event["title"]
    geometry = event["geometry"]
    latest_point = geometry[-1]
    date = latest_point["date"]
    coordinates = latest_point["coordinates"]
    magnitude = latest_point["magnitudeValue"]
    unit = latest_point["magnitudeUnit"]
    longitude, latitude = coordinates
    event_row = {
        "title": title,
        "date": date,
        "longitude": longitude,
        "latitude": latitude,
        "magnitude": magnitude,
        "unit": unit
    }

    rows.append(event_row)

df = pd.DataFrame(rows)
print(df)
print(df["magnitude"])
largest_magnitude = df["magnitude"].max()
largest_index = df["magnitude"].idxmax()
print(largest_magnitude)
print(largest_index)
largest_event = df.loc[largest_index]
print(largest_event)
print("Largest event:", largest_event["title"])
print("Magnitude:", largest_event["magnitude"], largest_event["unit"])

sorted_df = df.sort_values("magnitude", ascending=False)
print(sorted_df)

summary_df = sorted_df[["title", "magnitude", "unit"]]
print(summary_df)

summary_df.to_csv("applications/nasa_space_apps/eonet_wildfire_summary.csv", index=False)
