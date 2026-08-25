import sqlite3
import os

def create_database():
    """Create database and all tables"""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT DEFAULT 'patient',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            doctor_name TEXT NOT NULL,
            department TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Emergency records table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emergencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            location TEXT,
            emergency_type TEXT,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Payments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            appointment_id INTEGER,
            amount REAL NOT NULL,
            payment_method TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (appointment_id) REFERENCES appointments (id)
        )
    ''')
    
    # Prescriptions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prescriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            file_path TEXT NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database 'hospital.db' created successfully!")
    print("✅ All tables created!")

def create_uploads_folder():
    """Create uploads folder"""
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("✅ 'uploads' folder created successfully!")
    else:
        print("ℹ️ 'uploads' folder already exists!")

if __name__ == "__main__":
    print("="*50)
    print("Setting up Smart Hospital System...")
    print("="*50)
    
    # Create database
    create_database()
    
    # Create uploads folder
    create_uploads_folder()
    
    print("\n" + "="*50)
    print("✅ Setup completed successfully!")
    print("="*50)
    print("\nYou can now run: python main.py")