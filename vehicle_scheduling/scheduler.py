import requests

# API URLs
DEPOT_API = "http://20.207.122.201/evaluation-service/depots"
VEHICLE_API = "http://20.207.122.201/evaluation-service/vehicles"


def fetch_data():
    depots = requests.get(DEPOT_API).json()
    vehicles = requests.get(VEHICLE_API).json()
    return depots, vehicles


def main():
    depots, vehicles = fetch_data()
    
    print("Depots:", depots)
    print("Vehicles:", vehicles)


if __name__ == "__main__":
    main()
