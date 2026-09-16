import requests

url = "https://eonet.gsfc.nasa.gov/api/v3/events"

response = requests.get(url)
data = response.json()

print(type(data))
print(data.keys())

events = data["events"]

print(type(events))
print(len(events))

first_event = events[0]

print(type(first_event))
print(first_event.keys())
print("ID:", first_event["id"])
print("Title:", first_event["title"])
print("Categories:", first_event["categories"])

category = first_event["categories"][0]["title"]

print("Category:", category)
print("Geometry:", first_event["geometry"])

geometry = first_event["geometry"]
first_point = geometry[0]

print(type(first_point))
print(first_point.keys())

date = first_point["date"]
coordinates = first_point["coordinates"]
magnitude = first_point["magnitudeValue"]
unit = first_point["magnitudeUnit"]

print("Date:", date)
print("Coordinates:", coordinates)
print("Magnitude:", magnitude, unit)

longitude = coordinates[0]
latitude = coordinates[1]

print("Longitude:", longitude)
print("Latitude:", latitude)

latest_point = geometry[-1]

latest_date = latest_point["date"]
latest_coordinates = latest_point["coordinates"]
latest_magnitude = latest_point["magnitudeValue"]
latest_unit = latest_point["magnitudeUnit"]

latest_longitude = latest_coordinates[0]
latest_latitude = latest_coordinates[1]

print("Latest date:", latest_date)
print("Latest longitude:", latest_longitude)
print("Latest latitude:", latest_latitude)
print("Latest magnitude:", latest_magnitude, latest_unit)

print()
print("NASA EONET EVENT")
print("----------------")
print("ID:", first_event["id"])
print("Title:", first_event["title"])
print("Category:", category)
print("Latest date:", latest_date)
print("Latest longitude:", latest_longitude)
print("Latest latitude:", latest_latitude)
print("Latest magnitude:", latest_magnitude, latest_unit)

print()
print("First 5 events with categories:")

for event in events[:5]:
    title = event["title"]
    category = event["categories"][0]["title"]

    print(title, "|", category)


category_counts = {}

for event in events:
    category = event["categories"][0]["title"]

    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1


print()
print("EVENTS BY CATEGORY")
print("------------------")

for category, count in category_counts.items():
    print(category, ":", count)

most_common_category = max(category_counts, key=category_counts.get)
most_common_count = category_counts[most_common_category]

print()
print("DATASET SUMMARY")
print("---------------")
print("Total events:", len(events))
print("Number of categories:", len(category_counts))
print("Most common category:", most_common_category)
print("Number of events:", most_common_count)
