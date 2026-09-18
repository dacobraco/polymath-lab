import requests

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

for event in events:
    title = event["title"]
    geometry = event["geometry"]
    latest_point = geometry[-1]
    date = latest_point["date"]
    coordinates = latest_point["coordinates"]
    magnitude = latest_point["magnitudeValue"]
    unit = latest_point["magnitudeUnit"]
    longitude, latitude = coordinates
    print("Event:", title)
    print("Date:", date)
    print("Longitude:", longitude)
    print("Latitude:", latitude)
    print("Magnitude:", magnitude, unit)
    print()
