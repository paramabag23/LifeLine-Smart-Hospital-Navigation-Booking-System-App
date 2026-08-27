🏥 LifeLine+ — Smart Hospital Management System


A Python-based hospital management system that supports patient registration, appointment booking, payments, emergency response, indoor navigation, GPS distance calculation, and an AI-based symptom checker.
The project currently contains two separate implementations of the system. Please read the Project Structure section below before running anything, as they are not interchangeable.

---

<img width="793" height="715" alt="Screenshot 2026-08-27 213052" src="https://github.com/user-attachments/assets/52ea02f6-f800-4c22-b4dd-bebee28efab7" />

<img width="1445" height="847" alt="Screenshot 2026-08-27 213138" src="https://github.com/user-attachments/assets/17d28e14-489b-4f7a-b07b-ec6fffa97b97" />

📌 Overview

Component	Interface	Entry Point	Status

Desktop GUI App	Tkinter (windowed)	`main.py` or `database.py`	✅ Complete, self-contained

Console Module Set	Terminal / CLI (text menus)	`setup.py` (setup only)	⚠️ Modules complete, but no CLI entry point ties login → dashboard together yet

Both versions implement the same feature set but use different, incompatible database schemas (see Database Schema). Do not mix and match — pick one version and run its own setup.

---




✨ Features

🔐 User Authentication — registration and login for Patients and Doctors, with SHA-256 password hashing

📅 Appointment Booking — select department, doctor, date, and time slot; conflict checking prevents double-booking

📋 Appointment Management — view and cancel existing appointments

💰 Payments — simulated payment flow (Card / UPI / Net Banking / Cash) with transaction IDs and payment history

🚨 One-Click Emergency SOS — logs an emergency recordwith type and (simulated) location, and shows dispatch/response information

🗺️ Indoor Navigation — directions and distance between hospital locations using a coordinate-based map

📍 GPS Distance Calculator — Haversine-formula distance from the user's (simulated) location to the hospital, with nearest-parking lookup and travel time estimates

🤖 AI Health Assistant — basic keyword-based symptom checker that suggests a department, gives care tips, and recommends other hospital services

---
🗂 Project Structure
```
├── main.py           # Desktop GUI app (Tkinter) — LifeLine+ main entry point
├── database.py        # Alternate/duplicate GUI app — resets hospital.db on every run
├── hospital.db         # SQLite database (created automatically; included here with sample data)
│
├── setup.py            # Creates hospital.db + uploads/ folder for the CONSOLE module set
├── auth.py             # Console: signup() / login()
├── booking.py          # Console: book_appointment(), view_appointments(), cancel_appointment()
├── dashboard.py        # Console: patient_dashboard() / doctor_dashboard() text menus
├── payment.py          # Console: make_payment(), view_payment_history()
├── emergency.py        # Console: trigger_emergency(), view_emergency_history()
├── navigation.py       # Console: indoor navigation / directions engine
├── gps_module.py       # Console: GPS distance calculator (Haversine formula)
└── ai_module.py        # Console: AI symptom checker & service suggestions
```
About `main.py` vs `database.py`
These two files are near-duplicates of the same Tkinter desktop application ("LifeLine+ Smart Hospital System"). The key difference:
`main.py` — keeps existing data; creates `hospital.db` only if it doesn't already exist.
`database.py` — deletes and recreates `hospital.db` on every launch. Use this only when you want a fresh, empty database (⚠️ this permanently erases all existing users, appointments, payments, and emergency records).
About the console module set
`auth.py`, `booking.py`, `dashboard.py`, `payment.py`, `emergency.py`, `navigation.py`, `gps_module.py`, and `ai_module.py` are designed to work together as a text-menu (terminal) version of the same system — `dashboard.py` imports from all the others. However, no script in this project currently calls `auth.login()`/`auth.signup()` and then hands off to `dashboard.patient_dashboard()`, so there isn't yet a runnable entry point for this version. To use it, you would need to add a small driver script, for example:
```python
# app.py (example — not included in the project)
from auth import signup, login
from dashboard import patient_dashboard, doctor_dashboard

def main():
    print("1. Login  2. Sign Up")
    choice = input("Select: ")
    user = signup() if choice == "2" else None
    user = login() if choice == "1" else user
    if user:
        if user['user_type'] == 'doctor':
            doctor_dashboard(user)
        else:
            patient_dashboard(user)

if __name__ == "__main__":
    main()
```
---
🛠 Requirements
Python 3.7+
No third-party packages required — the project only uses the Python standard library:
`tkinter` (GUI)
`sqlite3` (database)
`hashlib`, `re`, `math`, `random`, `datetime`, `time`, `os`
> `tkinter` ships with most standard Python installations. On some Linux distributions you may need to install it separately, e.g. `sudo apt install python3-tk`.
---
🚀 Getting Started
Option A — Run the Desktop GUI App (recommended)
```bash
# Keeps existing data (creates hospital.db only if missing)
python main.py
```
or, to start with a completely fresh database:
```bash
# ⚠️ WARNING: deletes any existing hospital.db and all its data
python database.py
```
The app will open a login window. Click "Create New Account" to register as a Patient or Doctor, then log in to access the dashboard, booking, payments, emergency, navigation, GPS calculator, and AI assistant screens.
Option B — Set Up the Console Module Set
```bash
# Creates hospital.db (with the console-version schema) and an uploads/ folder
python setup.py
```
After this, you can import and call the individual modules directly (e.g. from a Python shell or your own driver script — see the example above), since a ready-made CLI entry point is not yet included.
---
🗄 Database Schema
⚠️ The GUI version and console version use different schemas. Running `setup.py` after already using `main.py`/`database.py` (or vice versa) on the same `hospital.db` file may cause errors due to missing/extra columns.
GUI version (`main.py` / `database.py`):
Table	Columns
`users`	id, name, email, phone, password, user_type
`appointments`	id, user_id, doctor_name, department, appointment_date, appointment_time, status
`emergencies`	id, user_id, location, emergency_type, created_at
`payments`	id, user_id, appointment_id, amount, payment_method, status, created_at
Console version (`setup.py`):
Table	Columns
`users`	id, name, email, phone, password, user_type, created_at
`appointments`	id, user_id, doctor_name, department, appointment_date, appointment_time, status, created_at
`emergencies`	id, user_id, location, emergency_type, status, created_at
`payments`	id, user_id, appointment_id, amount, payment_method, status, created_at
`prescriptions`	id, user_id, file_path, uploaded_at
Passwords are stored as SHA-256 hashes in both versions (not reversible, but not salted — for demonstration purposes only, not production-grade security).
---
🏥 Available Departments & Doctors
Department	Doctors
Cardiology	Dr. Smith, Dr. Johnson, Dr. Williams
Neurology	Dr. Brown, Dr. Jones, Dr. Garcia
Pediatrics	Dr. Miller, Dr. Davis, Dr. Rodriguez
Orthopedics	Dr. Wilson, Dr. Martinez, Dr. Anderson
General Medicine	Dr. Taylor, Dr. Thomas, Dr. Moore
Available time slots: 09:00, 10:00, 11:00, 14:00, 15:00, 16:00
---
⚠️ Known Limitations
This is a prototype/demo project — payments are simulated (no real payment gateway integration).
GPS coordinates and user location are simulated/randomized, not read from an actual device.
Passwords are hashed but not salted.
The GUI and console versions maintain separate, incompatible databases and should not be run against the same `hospital.db` file.
The console module set has no built-in entry point connecting login to the dashboard (see above).
---
📄 License
Add your license of choice here (e.g., MIT).
👤 Author
Add your name / course details here.
