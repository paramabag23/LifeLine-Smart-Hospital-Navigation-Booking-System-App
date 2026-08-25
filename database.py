# # import sqlite3
# # import hashlib
# # import os

# # def hash_password(password):
# #     """Hash password using SHA-256"""
# #     return hashlib.sha256(password.encode()).hexdigest()

# # def setup_database():
# #     """Create all necessary tables"""
# #     conn = sqlite3.connect('hospital.db')
# #     cursor = conn.cursor()
    
# #     # Users table
# #     cursor.execute('''
# #         CREATE TABLE IF NOT EXISTS users (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             name TEXT NOT NULL,
# #             email TEXT UNIQUE NOT NULL,
# #             phone TEXT NOT NULL,
# #             password TEXT NOT NULL,
# #             user_type TEXT DEFAULT 'patient',
# #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# #         )
# #     ''')
    
# #     # Appointments table
# #     cursor.execute('''
# #         CREATE TABLE IF NOT EXISTS appointments (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             user_id INTEGER NOT NULL,
# #             doctor_name TEXT NOT NULL,
# #             department TEXT NOT NULL,
# #             appointment_date TEXT NOT NULL,
# #             appointment_time TEXT NOT NULL,
# #             status TEXT DEFAULT 'pending',
# #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #             FOREIGN KEY (user_id) REFERENCES users (id)
# #         )
# #     ''')
    
# #     # Emergency records table
# #     cursor.execute('''
# #         CREATE TABLE IF NOT EXISTS emergencies (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             user_id INTEGER NOT NULL,
# #             location TEXT,
# #             emergency_type TEXT,
# #             status TEXT DEFAULT 'active',
# #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #             FOREIGN KEY (user_id) REFERENCES users (id)
# #         )
# #     ''')
    
# #     # Payments table
# #     cursor.execute('''
# #         CREATE TABLE IF NOT EXISTS payments (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             user_id INTEGER NOT NULL,
# #             appointment_id INTEGER,
# #             amount REAL NOT NULL,
# #             payment_method TEXT,
# #             status TEXT DEFAULT 'pending',
# #             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #             FOREIGN KEY (user_id) REFERENCES users (id),
# #             FOREIGN KEY (appointment_id) REFERENCES appointments (id)
# #         )
# #     ''')
    
# #     # Prescriptions table
# #     cursor.execute('''
# #         CREATE TABLE IF NOT EXISTS prescriptions (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             user_id INTEGER NOT NULL,
# #             file_path TEXT NOT NULL,
# #             uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #             FOREIGN KEY (user_id) REFERENCES users (id)
# #         )
# #     ''')
    
# #     conn.commit()
# #     conn.close()
# #     print("✅ Database setup completed!")

# # if __name__ == "__main__":
# #     # Create uploads directory
# #     if not os.path.exists('uploads'):
# #         os.makedirs('uploads')
# #     setup_database()/










import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import sqlite3
import hashlib
from datetime import datetime
import os
import random

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LifeLine+ Smart Hospital System")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')
        self.center_window()
        
        # Delete old database if exists
        if os.path.exists('hospital.db'):
            os.remove('hospital.db')
        
        self.init_database()
        self.show_login()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def init_database(self):
        """Create fresh database with correct schema"""
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        
        # Users table
        c.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT DEFAULT 'patient'
        )''')
        
        # Appointments table
        c.execute('''CREATE TABLE appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            doctor_name TEXT NOT NULL,
            department TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )''')
        
        # Emergency table
        c.execute('''CREATE TABLE emergencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            location TEXT,
            emergency_type TEXT,
            created_at TEXT
        )''')
        
        # Payments table
        c.execute('''CREATE TABLE payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            appointment_id INTEGER,
            amount REAL NOT NULL,
            payment_method TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT
        )''')
        
        conn.commit()
        conn.close()
        
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        
        print("✅ Fresh database created successfully!")
    
    def hash_password(self, pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()
    
    def show_login(self):
        for w in self.root.winfo_children():
            w.destroy()
        
        # Header
        header = tk.Frame(self.root, bg='#2c3e50', height=120)
        header.pack(fill='x')
        tk.Label(header, text="🏥 LifeLine+", font=('Arial', 32, 'bold'), 
                bg='#2c3e50', fg='white').pack(pady=25)
        tk.Label(header, text="Smart Hospital Navigation & Booking System", 
                font=('Arial', 12), bg='#2c3e50', fg='#bdc3c7').pack()
        
        # Login Frame
        frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
        frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=380)
        
        tk.Label(frame, text="🔐 Login to Your Account", font=('Arial', 18, 'bold'), 
                bg='white', fg='#2c3e50').pack(pady=20)
        
        tk.Label(frame, text="Email:", bg='white', font=('Arial', 11)).pack()
        self.login_email = tk.Entry(frame, width=30, font=('Arial', 11))
        self.login_email.pack(pady=5)
        
        tk.Label(frame, text="Password:", bg='white', font=('Arial', 11)).pack()
        self.login_pass = tk.Entry(frame, width=30, show='*', font=('Arial', 11))
        self.login_pass.pack(pady=5)
        
        tk.Button(frame, text="Login", command=self.do_login,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
                 width=20).pack(pady=10)
        
        tk.Button(frame, text="Create New Account", command=self.show_signup,
                 bg='#27ae60', fg='white', font=('Arial', 11), 
                 width=20).pack()
    
    def do_login(self):
        email = self.login_email.get()
        pwd = self.login_pass.get()
        
        if not email or not pwd:
            messagebox.showerror("Error", "Please enter email and password!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?",
                  (email, self.hash_password(pwd)))
        user = c.fetchone()
        conn.close()
        
        if user:
            self.current_user = user
            messagebox.showinfo("Success", f"Welcome {user[1]}!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")
    
    def show_signup(self):
        for w in self.root.winfo_children():
            w.destroy()
        
        header = tk.Frame(self.root, bg='#2c3e50', height=80)
        header.pack(fill='x')
        tk.Label(header, text="📝 Create New Account", font=('Arial', 24, 'bold'), 
                bg='#2c3e50', fg='white').pack(pady=20)
        
        frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
        frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=550)
        
        tk.Label(frame, text="Registration Form", font=('Arial', 18, 'bold'), 
                bg='white', fg='#2c3e50').pack(pady=15)
        
        fields = ['Full Name', 'Email', 'Phone', 'Password', 'Confirm Password']
        self.signup_entries = {}
        
        for f in fields:
            tk.Label(frame, text=f+':', bg='white', font=('Arial', 11)).pack()
            e = tk.Entry(frame, width=35, font=('Arial', 11))
            e.pack(pady=3)
            if 'Password' in f:
                e.config(show='*')
            self.signup_entries[f.lower()] = e
        
        tk.Label(frame, text="User Type:", bg='white', font=('Arial', 11)).pack()
        self.user_type = ttk.Combobox(frame, values=['Patient', 'Doctor'], width=33, font=('Arial', 11))
        self.user_type.set('Patient')
        self.user_type.pack(pady=5)
        
        tk.Button(frame, text="Register", command=self.do_register,
                 bg='#27ae60', fg='white', font=('Arial', 11, 'bold'), 
                 width=20).pack(pady=15)
        
        tk.Button(frame, text="Back to Login", command=self.show_login,
                 bg='#95a5a6', fg='white', font=('Arial', 11), 
                 width=20).pack()
    
    def do_register(self):
        name = self.signup_entries['full name'].get()
        email = self.signup_entries['email'].get()
        phone = self.signup_entries['phone'].get()
        pwd = self.signup_entries['password'].get()
        confirm = self.signup_entries['confirm password'].get()
        utype = self.user_type.get().lower()
        
        if not all([name, email, phone, pwd]):
            messagebox.showerror("Error", "All fields required!")
            return
        
        if pwd != confirm:
            messagebox.showerror("Error", "Passwords don't match!")
            return
        
        if len(pwd) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
                      (name, email, phone, self.hash_password(pwd), utype))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful! Please login.")
            self.show_login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")
        conn.close()
    
    def show_dashboard(self):
        for w in self.root.winfo_children():
            w.destroy()
        
        # Sidebar
        sidebar = tk.Frame(self.root, bg='#2c3e50', width=250)
        sidebar.pack(side='left', fill='y')
        
        tk.Label(sidebar, text=f"👤 {self.current_user[1]}", 
                font=('Arial', 14, 'bold'), bg='#2c3e50', fg='white').pack(pady=20)
        tk.Label(sidebar, text=f"({self.current_user[3].upper()})", 
                font=('Arial', 10), bg='#2c3e50', fg='#bdc3c7').pack()
        
        tk.Frame(sidebar, bg='#34495e', height=2).pack(fill='x', pady=20)
        
        menus = [
            ("🏠 Dashboard", self.show_welcome),
            ("📅 Book Appointment", self.book_appointment),
            ("📋 My Appointments", self.view_appointments),
            ("🗺️ Indoor Navigation", self.show_navigation),
            ("🚨 Emergency", self.emergency),
            ("💰 Make Payment", self.show_payments),
            ("📜 Payment History", self.payment_history),
            ("🤖 AI Assistant", self.ai_assistant),
            ("📍 GPS Distance", self.gps_calculator),
            ("🚪 Logout", self.show_login)
        ]
        
        for text, cmd in menus:
            btn = tk.Button(sidebar, text=text, command=cmd,
                           bg='#2c3e50', fg='white', relief='flat',
                           anchor='w', padx=20, pady=10, font=('Arial', 11))
            btn.pack(fill='x')
        
        self.main = tk.Frame(self.root, bg='#f0f0f0')
        self.main.pack(side='left', expand=True, fill='both', padx=20, pady=20)
        self.show_welcome()
    
    def show_welcome(self):
        self.clear_main()
        
        welcome_frame = tk.Frame(self.main, bg='#f0f0f0')
        welcome_frame.pack(expand=True)
        
        tk.Label(welcome_frame, text=f"Welcome to LifeLine+, {self.current_user[1]}!", 
                font=('Arial', 28, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=30)
        
        tk.Label(welcome_frame, text="Your One-Stop Smart Hospital Management System", 
                font=('Arial', 14), bg='#f0f0f0', fg='#7f8c8d').pack()
        
        # Stats
        stats_frame = tk.Frame(welcome_frame, bg='#f0f0f0')
        stats_frame.pack(pady=50)
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (self.current_user[0],))
        result = c.fetchone()
        appointments = result[0] if result else 0
        conn.close()
        
        stats = [
            ("📅 Appointments", appointments),
            ("🏥 Departments", 5),
            ("👨‍⚕️ Doctors", 12),
            ("⭐ Rating", "4.8/5")
        ]
        
        for i, (label, value) in enumerate(stats):
            frame = tk.Frame(stats_frame, bg='white', relief='ridge', bd=2)
            frame.grid(row=0, column=i, padx=15, pady=10, ipadx=25, ipady=20)
            tk.Label(frame, text=str(value), font=('Arial', 24, 'bold'), 
                    bg='white', fg='#3498db').pack()
            tk.Label(frame, text=label, font=('Arial', 12), 
                    bg='white', fg='#7f8c8d').pack()
    
    def book_appointment(self):
        self.clear_main()
        
        tk.Label(self.main, text="📅 Book Appointment", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=40, ipady=40)
        
        doctors = {
            'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
            'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
            'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
            'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
            'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
        }
        
        time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
        
        dept_var = tk.StringVar()
        doctor_var = tk.StringVar()
        date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        time_var = tk.StringVar()
        
        # Department
        tk.Label(frame, text="Department:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10, sticky='w')
        dept_combo = ttk.Combobox(frame, textvariable=dept_var, values=list(doctors.keys()), width=35, font=('Arial', 11))
        dept_combo.grid(row=0, column=1, pady=10, padx=10)
        
        # Doctor
        tk.Label(frame, text="Doctor:", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10, sticky='w')
        doctor_combo = ttk.Combobox(frame, textvariable=doctor_var, width=35, font=('Arial', 11))
        doctor_combo.grid(row=1, column=1, pady=10, padx=10)
        
        def update_doctors(*args):
            dept = dept_var.get()
            if dept in doctors:
                doctor_combo['values'] = doctors[dept]
        dept_var.trace('w', update_doctors)
        
        # Date
        tk.Label(frame, text="Date:", font=('Arial', 12, 'bold')).grid(row=2, column=0, pady=10, padx=10, sticky='w')
        date_entry = tk.Entry(frame, textvariable=date_var, width=38, font=('Arial', 11))
        date_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Time
        tk.Label(frame, text="Time:", font=('Arial', 12, 'bold')).grid(row=3, column=0, pady=10, padx=10, sticky='w')
        time_combo = ttk.Combobox(frame, textvariable=time_var, values=time_slots, width=35, font=('Arial', 11))
        time_combo.grid(row=3, column=1, pady=10, padx=10)
        
        def save_booking():
            dept = dept_var.get()
            doctor = doctor_var.get()
            date = date_var.get()
            time_slot = time_var.get()
            
            if not dept:
                messagebox.showerror("Error", "Please select a department!")
                return
            if not doctor:
                messagebox.showerror("Error", "Please select a doctor!")
                return
            if not date:
                messagebox.showerror("Error", "Please enter date!")
                return
            if not time_slot:
                messagebox.showerror("Error", "Please select time!")
                return
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            # Check for duplicate booking
            c.execute("SELECT * FROM appointments WHERE doctor_name=? AND appointment_date=? AND appointment_time=? AND status != 'cancelled'",
                     (doctor, date, time_slot))
            existing = c.fetchone()
            
            if existing:
                messagebox.showerror("Error", "This time slot is already booked!\nPlease choose another time.")
                conn.close()
                return
            
            # Insert appointment
            c.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
                     (self.current_user[0], doctor, dept, date, time_slot, 'pending'))
            conn.commit()
            app_id = c.lastrowid
            conn.close()
            
            messagebox.showinfo("Success", f"✅ Appointment Booked!\n\nID: {app_id}\nDoctor: {doctor}\nDepartment: {dept}\nDate: {date}\nTime: {time_slot}")
            
            # Clear form
            dept_var.set('')
            doctor_var.set('')
            time_var.set('')
            
            if messagebox.askyesno("Payment", "Would you like to make payment now?"):
                self.show_payments()
        
        tk.Button(frame, text="Book Appointment", command=save_booking,
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                 width=25).grid(row=4, column=0, columnspan=2, pady=20)
    
    def view_appointments(self):
        self.clear_main()
        
        tk.Label(self.main, text="📋 My Appointments", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC",
                  (self.current_user[0],))
        apps = c.fetchall()
        conn.close()
        
        if not apps:
            tk.Label(self.main, text="No appointments found!", font=('Arial', 14),
                    bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
            return
        
        # Create a frame with scrollbar
        tree_frame = tk.Frame(self.main, bg='#f0f0f0')
        tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Add scrollbars
        scroll_y = ttk.Scrollbar(tree_frame, orient='vertical')
        scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal')
        
        # Create Treeview with both scrollbars
        columns = ('ID', 'Doctor Name', 'Department', 'Date', 'Time', 'Status')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                           yscrollcommand=scroll_y.set, 
                           xscrollcommand=scroll_x.set)
        
        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)
        
        # Set column headings
        tree.heading('ID', text='ID')
        tree.heading('Doctor Name', text='👨‍⚕️ Doctor Name')
        tree.heading('Department', text='🏥 Department')
        tree.heading('Date', text='📅 Date')
        tree.heading('Time', text='⏰ Time')
        tree.heading('Status', text='📌 Status')
        
        # Set column widths
        tree.column('ID', width=50, anchor='center')
        tree.column('Doctor Name', width=200, anchor='center')
        tree.column('Department', width=150, anchor='center')
        tree.column('Date', width=120, anchor='center')
        tree.column('Time', width=120, anchor='center')
        tree.column('Status', width=120, anchor='center')
        
        # Add data with colored status
        for app in apps:
            status = app[5]
            if status == 'pending':
                status_display = '🟡 Pending'
            elif status == 'confirmed':
                status_display = '🟢 Confirmed'
            elif status == 'cancelled':
                status_display = '🔴 Cancelled'
            else:
                status_display = status
            
            values = (app[0], app[1], app[2], app[3], app[4], status_display)
            tree.insert('', 'end', values=values)
        
        # Grid layout
        tree.grid(row=0, column=0, sticky='nsew')
        scroll_y.grid(row=0, column=1, sticky='ns')
        scroll_x.grid(row=1, column=0, sticky='ew')
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Cancel section
        cancel_frame = tk.Frame(self.main, bg='#f0f0f0')
        cancel_frame.pack(pady=20)
        
        tk.Label(cancel_frame, text="Enter Appointment ID to cancel:", 
                font=('Arial', 11, 'bold'), bg='#f0f0f0').pack(side='left', padx=10)
        cancel_id = tk.Entry(cancel_frame, width=15, font=('Arial', 11), relief='solid', bd=1)
        cancel_id.pack(side='left', padx=10)
        
        def cancel_booking():
            app_id = cancel_id.get()
            if not app_id:
                messagebox.showerror("Error", "Please enter appointment ID!")
                return
            
            try:
                app_id = int(app_id)
            except:
                messagebox.showerror("Error", "Please enter a valid ID number!")
                return
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            c.execute("SELECT status FROM appointments WHERE id=? AND user_id=?", (app_id, self.current_user[0]))
            app = c.fetchone()
            
            if not app:
                messagebox.showerror("Error", "Appointment not found!")
                conn.close()
                return
            
            if app[0] == 'cancelled':
                messagebox.showerror("Error", "Appointment already cancelled!")
                conn.close()
                return
            
            c.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", (app_id, self.current_user[0]))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", f"✅ Appointment #{app_id} cancelled successfully!")
            cancel_id.delete(0, tk.END)
            self.view_appointments()
        
        tk.Button(cancel_frame, text="Cancel Appointment", command=cancel_booking,
                 bg='#e74c3c', fg='white', font=('Arial', 11, 'bold'), 
                 width=20, height=1, relief='raised', bd=2).pack(side='left', padx=10)
        
        tk.Button(cancel_frame, text="🔄 Refresh", command=self.view_appointments,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
                 width=15, height=1, relief='raised', bd=2).pack(side='left', padx=10)
    
    def show_payments(self):
        self.clear_main()
        
        tk.Label(self.main, text="💰 Make Payment", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT id, doctor_name, department, appointment_date, appointment_time FROM appointments WHERE user_id=? AND status='pending'",
                  (self.current_user[0],))
        pending_apps = c.fetchall()
        conn.close()
        
        if not pending_apps:
            tk.Label(self.main, text="No pending appointments for payment!", 
                    font=('Arial', 14), bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
            tk.Button(self.main, text="Book an Appointment", command=self.book_appointment,
                     bg='#3498db', fg='white', font=('Arial', 12, 'bold'), 
                     width=20, height=1).pack(pady=20)
            return
        
        payment_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        payment_frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(payment_frame, text="Select Appointment for Payment:", 
                font=('Arial', 12, 'bold'), bg='white').grid(row=0, column=0, pady=10, padx=10, sticky='w')
        
        # Show doctor name and department in the list
        app_list = [f"ID:{app[0]} - {app[1]} ({app[2]}) - {app[3]} {app[4]}" for app in pending_apps]
        app_var = tk.StringVar()
        app_combo = ttk.Combobox(payment_frame, textvariable=app_var, values=app_list, 
                                 width=50, font=('Arial', 11))
        app_combo.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(payment_frame, text="Amount (₹):", font=('Arial', 12, 'bold'), 
                bg='white').grid(row=1, column=0, pady=10, padx=10, sticky='w')
        amount_entry = tk.Entry(payment_frame, width=20, font=('Arial', 11))
        amount_entry.insert(0, "500")
        amount_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')
        
        tk.Label(payment_frame, text="Payment Method:", font=('Arial', 12, 'bold'), 
                bg='white').grid(row=2, column=0, pady=10, padx=10, sticky='w')
        method_var = tk.StringVar(value='UPI')
        method_combo = ttk.Combobox(payment_frame, textvariable=method_var, 
                                   values=['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash'], 
                                   width=28, font=('Arial', 11))
        method_combo.grid(row=2, column=1, pady=10, padx=10, sticky='w')
        
        def process_payment():
            if not app_var.get():
                messagebox.showerror("Error", "Please select an appointment!")
                return
            
            try:
                # Extract appointment ID from the selected item
                app_id = app_var.get().split('-')[0].replace('ID:', '').strip()
                amount = float(amount_entry.get())
                method = method_var.get()
            except:
                messagebox.showerror("Error", "Invalid input!")
                return
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            # Insert payment
            c.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
                     (self.current_user[0], app_id, amount, method, 'completed', 
                      datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            # Update appointment status
            c.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (app_id,))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "✅ Payment successful!\nYour appointment is confirmed.")
            self.show_payments()
        
        tk.Button(payment_frame, text="Pay Now", command=process_payment,
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                 width=20, height=1).grid(row=3, column=0, columnspan=2, pady=20)
    
    def payment_history(self):
        self.clear_main()
        
        tk.Label(self.main, text="📜 Payment History", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        
        # Get payment history with doctor name and department from appointments table
        c.execute("""
            SELECT p.id, p.appointment_id, a.doctor_name, a.department, 
                   p.amount, p.payment_method, p.status, p.created_at 
            FROM payments p
            LEFT JOIN appointments a ON p.appointment_id = a.id
            WHERE p.user_id=? 
            ORDER BY p.id DESC
        """, (self.current_user[0],))
        payments = c.fetchall()
        conn.close()
        
        if not payments:
            tk.Label(self.main, text="No payment records found!", font=('Arial', 14),
                    bg='#f0f0f0', fg='#7f8c8d').pack(pady=50)
            return
        
        tree_frame = tk.Frame(self.main, bg='#f0f0f0')
        tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        scroll_y = ttk.Scrollbar(tree_frame, orient='vertical')
        scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal')
        
        # Updated columns with Doctor and Department
        columns = ('ID', 'Appointment ID', 'Doctor Name', 'Department', 'Amount (₹)', 'Method', 'Status', 'Date')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                           yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)
        
        # Set column headings
        tree.heading('ID', text='ID')
        tree.heading('Appointment ID', text='Appointment ID')
        tree.heading('Doctor Name', text='👨‍⚕️ Doctor')
        tree.heading('Department', text='🏥 Department')
        tree.heading('Amount (₹)', text='Amount (₹)')
        tree.heading('Method', text='Method')
        tree.heading('Status', text='Status')
        tree.heading('Date', text='Date')
        
        # Set column widths
        tree.column('ID', width=50, anchor='center')
        tree.column('Appointment ID', width=100, anchor='center')
        tree.column('Doctor Name', width=180, anchor='center')
        tree.column('Department', width=150, anchor='center')
        tree.column('Amount (₹)', width=100, anchor='center')
        tree.column('Method', width=120, anchor='center')
        tree.column('Status', width=100, anchor='center')
        tree.column('Date', width=180, anchor='center')
        
        total = 0
        for payment in payments:
            # payment structure: (id, appointment_id, doctor_name, department, amount, method, status, created_at)
            status_display = '✅ Completed' if payment[6] == 'completed' else '⏳ Pending'
            doctor_name = payment[2] if payment[2] else 'N/A'
            department = payment[3] if payment[3] else 'N/A'
            
            values = (payment[0], payment[1], doctor_name, department, 
                     f'₹{payment[4]}', payment[5], status_display, payment[7])
            tree.insert('', 'end', values=values)
            total += payment[4]
        
        tree.grid(row=0, column=0, sticky='nsew')
        scroll_y.grid(row=0, column=1, sticky='ns')
        scroll_x.grid(row=1, column=0, sticky='ew')
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Total amount
        total_frame = tk.Frame(self.main, bg='#f0f0f0')
        total_frame.pack(pady=20)
        tk.Label(total_frame, text=f"💰 Total Amount Paid: ₹{total}", 
                font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#27ae60').pack()
        
        # Refresh button
        tk.Button(self.main, text="🔄 Refresh", command=self.payment_history,
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
                 width=15, height=1).pack(pady=10)
    
    def show_navigation(self):
        self.clear_main()
        
        tk.Label(self.main, text="🗺️ Indoor Navigation", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 
                    'Pediatrics', 'Orthopedics', 'Emergency', 'Pharmacy', 'Cafeteria']
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(frame, text="📍 Current Location:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10)
        start = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
        start.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(frame, text="🎯 Destination:", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10)
        end = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
        end.grid(row=1, column=1, pady=10, padx=10)
        
        directions = tk.Text(frame, height=10, width=55, font=('Arial', 10), bg='#f0f0f0', relief='solid', bd=1)
        directions.grid(row=2, column=0, columnspan=2, pady=20, padx=10)
        
        def get_directions():
            s = start.get()
            e = end.get()
            if s and e:
                directions.delete(1.0, tk.END)
                directions.insert(1.0, f"""
📍 DIRECTIONS from {s} to {e}
{'='*40}

→ Walk straight towards the main corridor
→ Take the elevator to the appropriate floor
→ Follow the color-coded signs:
   • Blue signs - Medical departments
   • Green signs - Services
→ Turn right at the main junction
→ You have reached {e}

⏱️ Estimated time: 5-10 minutes
📏 Approximate distance: 50-200 meters

💡 Tip: Follow the green line on the floor
""")
        
        tk.Button(frame, text="🗺️ Get Directions", command=get_directions,
                 bg='#3498db', fg='white', font=('Arial', 12, 'bold'), 
                 width=25, height=1).grid(row=3, column=0, columnspan=2, pady=10)
    
    def emergency(self):
        self.clear_main()
        
        frame = tk.Frame(self.main, bg='#ff4444', relief='ridge', bd=3)
        frame.pack(expand=True, fill='both', padx=50, pady=50)
        
        tk.Label(frame, text="🚨 EMERGENCY MODE 🚨", font=('Arial', 32, 'bold'), 
                bg='#ff4444', fg='white').pack(pady=30)
        tk.Label(frame, text="⚠️ This is for real emergencies only!", 
                font=('Arial', 16), bg='#ff4444', fg='yellow').pack()
        
        # Emergency type selection
        tk.Label(frame, text="Select Emergency Type:", font=('Arial', 14), 
                bg='#ff4444', fg='white').pack(pady=10)
        emergency_types = ['Medical Emergency', 'Accident', 'Cardiac Arrest', 
                          'Breathing Difficulty', 'Other']
        emergency_var = tk.StringVar(value='Medical Emergency')
        emergency_combo = ttk.Combobox(frame, textvariable=emergency_var, 
                                       values=emergency_types, width=30, font=('Arial', 12))
        emergency_combo.pack(pady=10)
        
        def activate():
            emergency_type = emergency_var.get()
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            c.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
                     (self.current_user[0], "Hospital Location", emergency_type, 
                      datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            conn.close()
            
            msg = Toplevel(self.root)
            msg.title("🚑 Emergency Response")
            msg.geometry("500x400")
            msg.configure(bg='#ff4444')
            
            # Center window
            msg.update_idletasks()
            x = (msg.winfo_screenwidth() // 2) - (500 // 2)
            y = (msg.winfo_screenheight() // 2) - (400 // 2)
            msg.geometry(f'500x400+{x}+{y}')
            
            tk.Label(msg, text="🚑 EMERGENCY TEAM DISPATCHED!", 
                    font=('Arial', 18, 'bold'), bg='#ff4444', fg='white').pack(pady=30)
            tk.Label(msg, text=f"Patient: {self.current_user[1]}", 
                    font=('Arial', 14), bg='#ff4444', fg='white').pack(pady=5)
            tk.Label(msg, text=f"Emergency Type: {emergency_type}", 
                    font=('Arial', 14), bg='#ff4444', fg='white').pack(pady=5)
            tk.Label(msg, text="⏱️ Estimated arrival: 5 minutes", 
                    font=('Arial', 14), bg='#ff4444', fg='yellow').pack(pady=20)
            tk.Label(msg, text="📋 Stay calm and do not move if injured", 
                    font=('Arial', 12), bg='#ff4444', fg='white').pack(pady=10)
            tk.Button(msg, text="OK", command=msg.destroy, 
                     bg='white', fg='#ff4444', font=('Arial', 12, 'bold'), 
                     width=15, height=1).pack(pady=20)
        
        tk.Button(frame, text="🚑 ACTIVATE EMERGENCY 🚑", command=activate,
                 font=('Arial', 20, 'bold'), bg='#cc0000', fg='white', 
                 width=30, height=2, relief='raised', bd=3).pack(pady=30)
    
    def ai_assistant(self):
        self.clear_main()
        
        tk.Label(self.main, text="🤖 AI Health Assistant", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(frame, text="Describe your symptoms:", font=('Arial', 12, 'bold')).pack(anchor='w')
        symptoms = tk.Text(frame, height=5, width=55, font=('Arial', 11), relief='solid', bd=1)
        symptoms.pack(pady=10, fill='x')
        
        tk.Label(frame, text="Analysis Results:", font=('Arial', 12, 'bold')).pack(anchor='w', pady=(10,0))
        result = tk.Text(frame, height=10, width=55, font=('Arial', 11), bg='#f0f0f0', relief='solid', bd=1)
        result.pack(pady=10, fill='both', expand=True)
        
        def analyze():
            text = symptoms.get(1.0, tk.END).lower()
            result.delete(1.0, tk.END)
            
            advice = ""
            departments = []
            
            if 'fever' in text:
                advice += "• 🤒 Fever: Rest and stay hydrated. Monitor temperature.\n"
                departments.append("General Medicine")
            if 'cough' in text:
                advice += "• 🤧 Cough: Use mask, avoid cold drinks, steam inhalation.\n"
                departments.append("General Medicine")
            if 'headache' in text:
                advice += "• 🤕 Headache: Rest in dark room, stay hydrated.\n"
                departments.append("Neurology")
            if 'chest' in text:
                advice += "• ⚠️ Chest pain: SEEK IMMEDIATE MEDICAL ATTENTION!\n"
                departments.append("Cardiology (Emergency)")
            if 'back' in text:
                advice += "• 💪 Back pain: Apply ice pack, gentle stretching.\n"
                departments.append("Orthopedics")
            if 'stomach' in text or 'vomiting' in text:
                advice += "• 🍽️ Stomach issues: Avoid spicy food, drink ORS.\n"
                departments.append("Gastroenterology")
            if 'cold' in text or 'flu' in text:
                advice += "• 😷 Cold/Flu: Take steam, drink warm fluids, rest.\n"
                departments.append("General Medicine")
            
            if advice:
                result.insert(1.0, f"📊 SYMPTOM ANALYSIS\n{'='*40}\n\n{advice}")
                if departments:
                    result.insert(tk.END, f"\n\n💡 Recommended Department(s): {', '.join(departments)}")
                result.insert(tk.END, f"\n\n📅 Please book an appointment with a doctor.")
            else:
                result.insert(1.0, "📊 No specific symptoms detected.\n\n💡 Consider a general health checkup.\n📅 Book an appointment with a doctor.")
        
        tk.Button(frame, text="🔍 Analyze Symptoms", command=analyze,
                 bg='#9b59b6', fg='white', font=('Arial', 12, 'bold'), 
                 width=25, height=1).pack(pady=10)
    
    def gps_calculator(self):
        self.clear_main()
        
        tk.Label(self.main, text="📍 GPS Distance Calculator", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
        
        tk.Label(frame, text="📍 Select your location:", font=('Arial', 12, 'bold')).pack(anchor='w')
        location = ttk.Combobox(frame, values=locations, width=35, font=('Arial', 11))
        location.pack(pady=10, anchor='w')
        
        result = tk.Text(frame, height=10, width=55, font=('Arial', 11), bg='#f0f0f0', relief='solid', bd=1)
        result.pack(pady=10, fill='both', expand=True)
        
        def calculate():
            loc = location.get()
            if loc:
                dist = random.uniform(1, 15)
                result.delete(1.0, tk.END)
                result.insert(1.0, f"""
📍 DISTANCE FROM {loc.upper()} TO HOSPITAL
{'='*40}

📏 Distance: {dist:.1f} kilometers

🚗 BY CAR:
• Driving time: {dist * 2:.0f} minutes
• Parking available at hospital

🚶 BY WALK:
• Walking time: {dist * 12:.0f} minutes
• Walking route available

🚑 BY AMBULANCE:
• Emergency response: {dist * 1.5:.0f} minutes

💰 ESTIMATED COST:
• Taxi/Uber: ₹{dist * 15:.0f} - ₹{dist * 20:.0f}

💡 TIPS:
• Add 10-15 minutes for traffic
• Hospital has free parking
• Emergency entrance on east side
""")
        
        tk.Button(frame, text="📍 Calculate Distance", command=calculate,
                 bg='#3498db', fg='white', font=('Arial', 12, 'bold'), 
                 width=25, height=1).pack(pady=10)
    
    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()





# at first run this in terminal then run ---  Remove-Item hospital.db -ErrorAction SilentlyContinue