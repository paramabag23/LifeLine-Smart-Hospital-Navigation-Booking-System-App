import sqlite3
from datetime import datetime
import time

def trigger_emergency(user_id, user_name):
    """One-click emergency system"""
    print("\n" + "="*50)
    print("🚨 EMERGENCY MODE ACTIVATED 🚨")
    print("="*50)
    
    print("\n⚠️  EMERGENCY PROTOCOL INITIATED ⚠️")
    time.sleep(1)
    
    # Get user location (simulated)
    print("\n📍 Detecting your location...")
    time.sleep(1)
    
    locations = ['Entrance', 'Reception', 'Cardiology', 'Emergency']
    import random
    location = random.choice(locations)
    
    print(f"📍 Your location: {location}")
    
    # Get emergency type
    print("\n🚑 Emergency Type:")
    print("1. Medical Emergency")
    print("2. Accident")
    print("3. Cardiac Arrest")
    print("4. Breathing Difficulty")
    print("5. Other")
    
    emergency_type_choice = input("\nSelect type (1-5): ")
    
    emergency_types = {
        '1': 'Medical Emergency',
        '2': 'Accident',
        '3': 'Cardiac Arrest',
        '4': 'Breathing Difficulty',
        '5': 'Other'
    }
    
    emergency_type = emergency_types.get(emergency_type_choice, 'Medical Emergency')
    
    # Save to database
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO emergencies (user_id, location, emergency_type)
            VALUES (?, ?, ?)
        ''', (user_id, location, emergency_type))
        
        conn.commit()
        conn.close()
    except:
        pass
    
    # Emergency response
    print("\n🚨 ACTIVATING EMERGENCY RESPONSE TEAM...")
    time.sleep(1)
    
    print("\n✅ Emergency team has been notified!")
    print(f"📋 Details:")
    print(f"   • Patient: {user_name}")
    print(f"   • Location: {location}")
    print(f"   • Emergency Type: {emergency_type}")
    print(f"   • Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Navigation to nearest emergency services
    print("\n🗺️  DIRECTIONS TO NEAREST EMERGENCY SERVICES:")
    from navigation import get_directions
    print(get_directions(location, 'Emergency'))
    
    # Instructions
    print("\n📋 INSTRUCTIONS:")
    print("   1. Stay calm and wait for medical team")
    print("   2. Do not move if you have injuries")
    print("   3. Medical team will arrive shortly")
    print("   4. Emergency team has been dispatched to your location")
    
    print("\n" + "="*50)
    print("🚑 HELP IS ON THE WAY! 🚑")
    print("="*50)
    
    return True

def view_emergency_history(user_id):
    """View user's emergency history"""
    print("\n" + "="*50)
    print("📋 EMERGENCY HISTORY")
    print("="*50)
    
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, location, emergency_type, status, created_at
            FROM emergencies 
            WHERE user_id = ?
            ORDER BY created_at DESC
        ''', (user_id,))
        
        emergencies = cursor.fetchall()
        conn.close()
        
        if not emergencies:
            print("No emergency records found.")
            return
        
        print(f"\n{'ID':<5} {'Location':<15} {'Type':<20} {'Status':<10} {'Time':<20}")
        print("-" * 75)
        
        for emergency in emergencies:
            print(f"{emergency[0]:<5} {emergency[1]:<15} {emergency[2]:<20} {emergency[3]:<10} {emergency[4]:<20}")
            
    except Exception as e:
        print(f"❌ Error: {e}")