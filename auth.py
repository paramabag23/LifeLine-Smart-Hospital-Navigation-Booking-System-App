import sqlite3
import hashlib
import re
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_phone(phone):
    return len(phone) >= 10 and phone.isdigit()

def signup():
    """User registration"""
    print("\n" + "="*50)
    print("📝 NEW USER REGISTRATION")
    print("="*50)
    
    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    password = input("Password: ").strip()
    confirm_password = input("Confirm Password: ").strip()
    
    # Validations
    if not name or not email or not phone or not password:
        print("❌ All fields are required!")
        return False
    
    if not validate_email(email):
        print("❌ Invalid email format!")
        return False
    
    if not validate_phone(phone):
        print("❌ Phone number must be at least 10 digits!")
        return False
    
    if password != confirm_password:
        print("❌ Passwords do not match!")
        return False
    
    if len(password) < 6:
        print("❌ Password must be at least 6 characters!")
        return False
    
    # User type selection
    print("\nUser Type:")
    print("1. Patient")
    print("2. Doctor")
    user_type_choice = input("Select (1/2): ")
    user_type = "doctor" if user_type_choice == "2" else "patient"
    
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO users (name, email, phone, password, user_type)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, hash_password(password), user_type))
        
        conn.commit()
        print(f"\n✅ Registration successful! You can now login as {user_type}.")
        conn.close()
        return True
        
    except sqlite3.IntegrityError:
        print("❌ Email already registered!")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def login():
    """User login"""
    print("\n" + "="*50)
    print("🔐 LOGIN")
    print("="*50)
    
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, name, email, user_type FROM users 
            WHERE email = ? AND password = ?
        ''', (email, hash_password(password)))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            print(f"\n✅ Welcome back, {user[1]}!")
            return {'id': user[0], 'name': user[1], 'email': user[2], 'user_type': user[3]}
        else:
            print("❌ Invalid email or password!")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None