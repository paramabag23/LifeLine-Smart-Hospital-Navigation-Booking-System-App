import math
import random

class GPSModule:
    def __init__(self):
        # Simulated hospital coordinates (latitude, longitude)
        self.hospital_location = (28.6139, 77.2090)  # Delhi coordinates
        self.parking_locations = [
            (28.6145, 77.2085),  # Main parking
            (28.6135, 77.2095),  # East parking
            (28.6140, 77.2080)   # West parking
        ]
        
    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """Calculate distance between two points using Haversine formula"""
        R = 6371  # Earth's radius in kilometers
        
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        
        a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    def get_user_location(self):
        """Simulate getting user's current location"""
        print("\n📍 Detecting your location...")
        import time
        time.sleep(1)
        
        # Simulate GPS coordinates
        lat = self.hospital_location[0] + random.uniform(-0.01, 0.01)
        lon = self.hospital_location[1] + random.uniform(-0.01, 0.01)
        
        return (lat, lon)
    
    def calculate_distance_to_hospital(self, user_location=None):
        """Calculate distance from user to hospital"""
        if user_location is None:
            user_location = self.get_user_location()
        
        distance = self.haversine_distance(
            user_location[0], user_location[1],
            self.hospital_location[0], self.hospital_location[1]
        )
        
        return distance
    
    def find_nearest_parking(self, user_location=None):
        """Find nearest parking location"""
        if user_location is None:
            user_location = self.get_user_location()
        
        nearest = None
        min_distance = float('inf')
        
        for i, parking in enumerate(self.parking_locations):
            distance = self.haversine_distance(
                user_location[0], user_location[1],
                parking[0], parking[1]
            )
            if distance < min_distance:
                min_distance = distance
                nearest = i
        
        return nearest, min_distance
    
    def get_travel_info(self):
        """Get complete travel information to hospital"""
        print("\n" + "="*50)
        print("🗺️ GPS NAVIGATION SYSTEM")
        print("="*50)
        
        user_location = self.get_user_location()
        
        print(f"\n📍 Your location: ({user_location[0]:.4f}, {user_location[1]:.4f})")
        print(f"🏥 Hospital location: ({self.hospital_location[0]:.4f}, {self.hospital_location[1]:.4f})")
        
        # Calculate distance
        distance = self.calculate_distance_to_hospital(user_location)
        
        print(f"\n📏 Distance to hospital: {distance:.2f} km")
        
        # Calculate travel time
        walking_time = distance / 5 * 60  # 5 km/h walking speed
        driving_time = distance / 40 * 60  # 40 km/h driving speed
        
        print(f"🚶 Walking time: {walking_time:.0f} minutes")
        print(f"🚗 Driving time: {driving_time:.0f} minutes")
        
        # Find nearest parking
        parking_idx, parking_dist = self.find_nearest_parking(user_location)
        if parking_idx is not None:
            print(f"\n🅿️ Nearest parking: {parking_dist:.2f} km away")
        
        # Directions
        print("\n🗺️ DIRECTIONS:")
        if distance < 1:
            print("   • You're very close to the hospital")
            print("   • Follow hospital signboards")
        elif distance < 5:
            print("   • Take the main road towards hospital")
            print("   • Hospital will be on your right/left")
        else:
            print("   • Use GPS navigation for turn-by-turn directions")
            print("   • Consider using public transport")
        
        # Traffic simulation
        traffic_level = random.choice(['Light', 'Moderate', 'Heavy'])
        print(f"\n🚦 Estimated traffic: {traffic_level}")
        
        if traffic_level == 'Heavy':
            print("   • Add 15-20 minutes extra travel time")
        
        return distance

def distance_calculator():
    """Main distance calculation interface"""
    gps = GPSModule()
    
    print("\n" + "="*50)
    print("📏 DISTANCE CALCULATOR")
    print("="*50)
    
    print("\nOptions:")
    print("1. Calculate distance to hospital")
    print("2. Find nearest parking")
    print("3. Get complete travel information")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        distance = gps.calculate_distance_to_hospital()
        print(f"\n📏 Distance to hospital: {distance:.2f} km")
        
    elif choice == '2':
        parking_idx, distance = gps.find_nearest_parking()
        parking_names = ['Main Parking', 'East Parking', 'West Parking']
        print(f"\n🅿️ Nearest parking: {parking_names[parking_idx]}")
        print(f"📏 Distance: {distance:.2f} km")
        
    elif choice == '3':
        gps.get_travel_info()
        
    else:
        print("❌ Invalid option!")