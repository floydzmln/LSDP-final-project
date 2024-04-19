import csv
import utm
import matplotlib.pyplot as plt

# Function to convert latitude and longitude to UTM
def convert_to_utm(lat, lon):
    utm_coord = utm.from_latlon(lat, lon)
    return utm_coord[0], utm_coord[1]


# Read the CSV file and extract GPS coordinates during the first video recording
def extract_gps_coordinates(csv_file):
    gps_coordinates = []
    video_started=False
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['CUSTOM.isVideo'] == 'Recording':  # Check if it's a video recording
                video_started=True
                lat = float(row['OSD.latitude'])
                lon = float(row['OSD.longitude'])
                gps_coordinates.append((lat, lon))
                # Assuming only need the coordinates during the first video recording
            elif video_started and row['CUSTOM.isVideo'] != 'Recording':
                break

    return gps_coordinates

if __name__=="__main__":
    # Extract GPS coordinates
    gps_coordinates = extract_gps_coordinates('DJIFlightRecord_2021-03-18_.csv')

    # Convert GPS coordinates to UTM
    utm_coordinates = [convert_to_utm(lat, lon) for lat, lon in gps_coordinates]

    # Unzip UTM coordinates
    utm_easting, utm_northing = zip(*utm_coordinates)

    # Plot the flight path
    plt.figure(figsize=(10, 6))
    plt.plot(utm_easting, utm_northing, marker='o')
    plt.title('Flight Path')
    plt.xlabel('UTM Easting')
    plt.ylabel('UTM Northing')
    plt.grid(True)
    plt.show()
