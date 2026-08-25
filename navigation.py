# Hospital map with coordinates
HOSPITAL_MAP = {
    'Entrance': (0, 0),
    'Reception': (5, 0),
    'Cardiology': (10, 5),
    'Neurology': (10, 10),
    'Pediatrics': (5, 15),
    'Orthopedics': (15, 5),
    'General Medicine': (15, 10),
    'Pharmacy': (20, 5),
    'Emergency': (0, 10),
    'Radiology': (5, 20),
    'Laboratory': (10, 20),
    'Cafeteria': (20, 15)
}

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def get_directions(start, end):
    """Get turn-by-turn directions"""
    if start not in HOSPITAL_MAP:
        return f"❌ '{start}' is not a valid location!"
    
    if end not in HOSPITAL_MAP:
        return f"❌ '{end}' is not a valid location!"
    
    start_pos = HOSPITAL_MAP[start]
    end_pos = HOSPITAL_MAP[end]
    
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    
    directions = []
    directions.append(f"\n📍 From {start} to {end}:")
    
    # Horizontal movement
    if dx > 0:
        directions.append(f"   → Walk {dx} meters East")
    elif dx < 0:
        directions.append(f"   ← Walk {abs(dx)} meters West")
    
    # Vertical movement
    if dy > 0:
        directions.append(f"   ↓ Walk {dy} meters South")
    elif dy < 0:
        directions.append(f"   ↑ Walk {abs(dy)} meters North")
    
    # Calculate distance
    distance = calculate_distance(start_pos, end_pos)
    directions.append(f"\n📏 Total distance: {distance:.1f} meters")
    
    # Estimated time (assuming 1 m/s walking speed)
    estimated_time = distance / 60  # minutes
    directions.append(f"⏱️ Estimated time: {estimated_time:.1f} minutes")
    
    return '\n'.join(directions)

def find_nearest_facility(current_location, facility_type):
    """Find nearest facility of a specific type"""
    if current_location not in HOSPITAL_MAP:
        return None, None
    
    current_pos = HOSPITAL_MAP[current_location]
    
    # Filter facilities based on type
    if facility_type.lower() == 'department':
        facilities = ['Cardiology', 'Neurology', 'Pediatrics', 'Orthopedics', 'General Medicine']
    elif facility_type.lower() == 'service':
        facilities = ['Pharmacy', 'Radiology', 'Laboratory', 'Emergency']
    else:
        facilities = list(HOSPITAL_MAP.keys())
    
    nearest = None
    min_distance = float('inf')
    
    for facility in facilities:
        if facility != current_location:
            distance = calculate_distance(current_pos, HOSPITAL_MAP[facility])
            if distance < min_distance:
                min_distance = distance
                nearest = facility
    
    return nearest, min_distance

def navigation_system():
    """Main navigation menu"""
    print("\n" + "="*50)
    print("🗺️ INDOOR NAVIGATION SYSTEM")
    print("="*50)
    
    print("\n📍 Available Locations:")
    for location in HOSPITAL_MAP.keys():
        print(f"   • {location}")
    
    print("\nOptions:")
    print("1. Get directions between locations")
    print("2. Find nearest facility")
    print("3. Show hospital map")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == '1':
        start = input("Starting location: ").strip()
        end = input("Destination: ").strip()
        print(get_directions(start, end))
        
    elif choice == '2':
        current = input("Current location: ").strip()
        print("\nFind nearest:")
        print("1. Department")
        print("2. Service (Pharmacy, Emergency, etc.)")
        type_choice = input("Select (1/2): ")
        
        facility_type = 'department' if type_choice == '1' else 'service'
        nearest, distance = find_nearest_facility(current, facility_type)
        
        if nearest:
            print(f"\n📍 Nearest {facility_type}: {nearest}")
            print(f"📏 Distance: {distance:.1f} meters")
            print(get_directions(current, nearest))
        else:
            print("❌ Could not find nearest facility!")
            
    elif choice == '3':
        print("\n" + "="*50)
        print("HOSPITAL MAP LAYOUT")
        print("="*50)
        print("\nCoordinate System (X, Y):")
        print("-" * 40)
        for location, coords in HOSPITAL_MAP.items():
            print(f"{location:<20} → ({coords[0]:>2}, {coords[1]:>2})")
        print("\nLegend:")
        print("  X-axis: East-West direction")
        print("  Y-axis: North-South direction")
        print("  Entrance at (0,0)")
    
    else:
        print("❌ Invalid option!")