import requests

class LocationFinder:
"""A client for retrieving geolocation data for IP addresses using ip-api.com."""

    BASE_URL = "http://ip-api.com/json/"

    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        
    def get_location(self, ip_address: str) -> dict | None:
        """Fetch location details including Region, Zip, Lat/Lon, and ISP for a given IP."""
        url = f"{self.BASE_URL}{ip_address}"

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == "success":
                self._display_info(data)
                return data
            else:
                print(f"API Error  : {data.get('message', 'Unknown error')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Network/HTTP Error: {e}")
            return None

    def _display_info(self, data: dict) -> None:
        """Helper method to print formatted location details."""
        print(f"\nIP Address : {data.get('query')}")
        print(f"City       : {data.get('city')}")
        print(f"Region     : {data.get('regionName')} ({data.get('region')})")
        print(f"Zip Code   : {data.get('zip')}")
        print(f"Country    : {data.get('country')}")
        print(f"Latitude   : {data.get('lat')}")
        print(f"Longitude  : {data.get('lon')}")
        print(f"ISP        : {data.get('isp')}")

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self.session.close()