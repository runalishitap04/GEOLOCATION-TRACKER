import requests
import folium
import webbrowser

def get_geolocation():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()

        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')  # This is in "lat,lon" format

        print(f"IP Address: {ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"Coordinates: {loc}")

        return loc, city, region, country
    except Exception as e:
        print("Error fetching geolocation:", e)
        return None, None, None, None

def create_map(loc, city, region, country):
    lat, lon = map(float, loc.split(','))
    my_map = folium.Map(location=[lat, lon], zoom_start=10)

    folium.Marker(
        [lat, lon],
        popup=f"{city}, {region}, {country}",
        tooltip="Your Location"
    ).add_to(my_map)

    map_file = "geolocation_map.html"
    my_map.save(map_file)
    webbrowser.open(map_file)

def main():
    loc, city, region, country = get_geolocation()
    if loc:
        create_map(loc, city, region, country)

if __name__ == "__main__":
    main()
