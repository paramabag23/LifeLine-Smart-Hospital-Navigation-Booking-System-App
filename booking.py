import sqlite3
from datetime import datetime

# Available doctors
DOCTORS = {
    'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
    'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
    'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
    'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
    'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
}

TIME_SLOTS = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00']

def book_appointment(user_id):
    """Book a new appointment"""
    print("\n" + "="*50)
    print("📅 BOOK APPOINTMENT")
    print("="*50)
    
    # Select department
    print("\nAvailable Departments:")
    departments = list(DOCTORS.keys())
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")
    
    try:
        dept_choice = int(input("\nSelect department (number): ")) - 1
        if dept_choice < 0 or dept_choice >= len(departments):
            print("❌ Invalid selection!")
            return False
        
        department = departments[dept_choice]
        
        # Select doctor
        print(f"\nDoctors in {department}:")
        doctors = DOCTORS[department]
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")
        
        doc_choice = int(input("Select doctor (number): ")) - 1
        if doc_choice < 0 or doc_choice >= len(doctors):
            print("❌ Invalid selection!")
            return False
        
        doctor = doctors[doc_choice]
        
        # Select date
        print("\nAvailable dates (next 7 days):")
        date = input("Enter date (YYYY-MM-DD): ").strip()
        
        # Select time
        print("\nAvailable time slots:")
        for i, slot in enumerate(TIME_SLOTS, 1):
            print(f"{i}. {slot}")
        
        time_choice = int(input("Select time (number): ")) - 1
        if time_choice < 0 or time_choice >= len(TIME_SLOTS):
            print("❌ Invalid selection!")
            return False
        
        time_slot = TIME_SLOTS[time_choice]
        
        # Check if slot is available
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM appointments 
            WHERE doctor_name = ? AND appointment_date = ? AND appointment_time = ? 
            AND status != 'cancelled'
        ''', (doctor, date, time_slot))
        
        existing = cursor.fetchone()
        if existing:
            print("❌ This time slot is already booked!")
            conn.close()
            return False
        
        # Book appointment
        cursor.execute('''
            INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, doctor, department, date, time_slot))
        
        conn.commit()
        appointment_id = cursor.lastrowid
        conn.close()
        
        print(f"\n✅ Appointment booked successfully!")
        print(f"   ID: {appointment_id}")
        print(f"   Doctor: {doctor}")
        print(f"   Date: {date} at {time_slot}")
        
        # Ask for payment
        pay_now = input("\nWould you like to pay now? (yes/no): ").lower()
        if pay_now == 'yes':
            from payment import make_payment
            make_payment(user_id, appointment_id, 500)
        
        return True
        
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def view_appointments(user_id):
    """View user's appointments"""
    print("\n" + "="*50)
    print("📋 MY APPOINTMENTS")
    print("="*50)
    
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, doctor_name, department, appointment_date, appointment_time, status
            FROM appointments 
            WHERE user_id = ?
            ORDER BY appointment_date, appointment_time
        ''', (user_id,))
        
        appointments = cursor.fetchall()
        conn.close()
        
        if not appointments:
            print("No appointments found.")
            return []
        
        print(f"\n{'ID':<5} {'Doctor':<20} {'Department':<15} {'Date':<12} {'Time':<8} {'Status':<10}")
        print("-" * 80)
        
        for app in appointments:
            print(f"{app[0]:<5} {app[1]:<20} {app[2]:<15} {app[3]:<12} {app[4]:<8} {app[5]:<10}")
        
        return appointments
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def cancel_appointment(user_id):
    """Cancel an existing appointment"""
    appointments = view_appointments(user_id)
    
    if not appointments:
        return False
    
    try:
        app_id = int(input("\nEnter appointment ID to cancel: "))
        
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        # Check if appointment belongs to user
        cursor.execute('''
            SELECT status FROM appointments 
            WHERE id = ? AND user_id = ?
        ''', (app_id, user_id))
        
        app = cursor.fetchone()
        
        if not app:
            print("❌ Appointment not found!")
            conn.close()
            return False
        
        if app[0] == 'cancelled':
            print("❌ Appointment is already cancelled!")
            conn.close()
            return False
        
        # Cancel appointment
        cursor.execute('''
            UPDATE appointments SET status = 'cancelled' 
            WHERE id = ? AND user_id = ?
        ''', (app_id, user_id))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Appointment #{app_id} has been cancelled.")
        return True
        
    except ValueError:
        print("❌ Invalid input!")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False