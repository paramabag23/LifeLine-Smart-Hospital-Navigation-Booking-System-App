import os
import sys
from datetime import datetime

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(user):
    """Display dashboard header"""
    print("="*60)
    print(f"🏥 SMART HOSPITAL MANAGEMENT SYSTEM")
    print(f"👋 Welcome, {user['name']} ({user['user_type'].upper()})")
    print(f"📅 {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}")
    print("="*60)

def patient_dashboard(user):
    """Patient dashboard"""
    while True:
        clear_screen()
        show_header(user)
        
        print("\n📋 MAIN MENU:")
        print("="*40)
        print("1. 📅 Book Appointment")
        print("2. 📋 View My Appointments")
        print("3. ❌ Cancel Appointment")
        print("4. 🗺️ Indoor Navigation")
        print("5. 🚨 Emergency (One-Click)")
        print("6. 💰 Make Payment")
        print("7. 📜 Payment History")
        print("8. 🤖 AI Health Assistant")
        print("9. 🗺️ GPS & Distance Calculator")
        print("10. 📊 View Emergency History")
        print("11. 🚪 Logout")
        print("="*40)
        
        choice = input("\nEnter your choice (1-11): ").strip()
        
        if choice == '1':
            from booking import book_appointment
            book_appointment(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            from booking import view_appointments
            view_appointments(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            from booking import cancel_appointment
            cancel_appointment(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            from navigation import navigation_system
            navigation_system()
            input("\nPress Enter to continue...")
            
        elif choice == '5':
            from emergency import trigger_emergency
            trigger_emergency(user['id'], user['name'])
            input("\nPress Enter to continue...")
            
        elif choice == '6':
            from booking import view_appointments
            appointments = view_appointments(user['id'])
            if appointments:
                try:
                    app_id = int(input("\nEnter appointment ID to pay: "))
                    from payment import make_payment
                    make_payment(user['id'], app_id, 500)
                except ValueError:
                    print("❌ Invalid input!")
            input("\nPress Enter to continue...")
            
        elif choice == '7':
            from payment import view_payment_history
            view_payment_history(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '8':
            from ai_module import HealthAssistant
            assistant = HealthAssistant()
            assistant.analyze_symptoms()
            input("\nPress Enter to continue...")
            
        elif choice == '9':
            from gps_module import distance_calculator
            distance_calculator()
            input("\nPress Enter to continue...")
            
        elif choice == '10':
            from emergency import view_emergency_history
            view_emergency_history(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '11':
            print("\n👋 Logging out...")
            break
            
        else:
            print("❌ Invalid choice! Please try again.")
            input("\nPress Enter to continue...")

def doctor_dashboard(user):
    """Doctor dashboard (simplified)"""
    while True:
        clear_screen()
        show_header(user)
        
        print("\n📋 DOCTOR MENU:")
        print("="*40)
        print("1. 👨‍⚕️ View Today's Appointments")
        print("2. 📋 View All Appointments")
        print("3. 🗺️ Indoor Navigation")
        print("4. 🚨 Emergency Alert")
        print("5. 🤖 AI Assistant")
        print("6. 🚪 Logout")
        print("="*40)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            from booking import view_appointments
            view_appointments(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            from booking import view_appointments
            view_appointments(user['id'])
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            from navigation import navigation_system
            navigation_system()
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\n🚨 Emergency alerts will be displayed here")
            input("\nPress Enter to continue...")
            
        elif choice == '5':
            from ai_module import HealthAssistant
            assistant = HealthAssistant()
            assistant.analyze_symptoms()
            input("\nPress Enter to continue...")
            
        elif choice == '6':
            print("\n👋 Logging out...")
            break
            
        else:
            print("❌ Invalid choice!")
            input("\nPress Enter to continue...")
