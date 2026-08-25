
# import tkinter as tk
# from tkinter import ttk, messagebox, Toplevel, scrolledtext
# import sqlite3
# import hashlib
# from datetime import datetime
# import os
# import random
# import math

# class HospitalApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("LifeLine+ Smart Hospital System")
#         self.root.geometry("1200x700")
#         self.root.configure(bg='#f0f0f0')
        
#         # Center window
#         self.center_window()
        
#         # Initialize database
#         self.init_db()
        
#         # Show login window
#         self.show_login()
    
#     def center_window(self):
#         self.root.update_idletasks()
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f'{width}x{height}+{x}+{y}')
    
#     def init_db(self):
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
        
#         # Users table
#         c.execute('''CREATE TABLE IF NOT EXISTS users
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                       name TEXT, email TEXT UNIQUE, 
#                       phone TEXT, password TEXT, user_type TEXT)''')
        
#         # Appointments table
#         c.execute('''CREATE TABLE IF NOT EXISTS appointments
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                       user_id INTEGER, doctor_name TEXT,
#                       department TEXT, date TEXT, time TEXT, status TEXT)''')
        
#         # Emergency table
#         c.execute('''CREATE TABLE IF NOT EXISTS emergencies
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                       user_id INTEGER, location TEXT,
#                       emergency_type TEXT, created_at TEXT)''')
        
#         # Payments table
#         c.execute('''CREATE TABLE IF NOT EXISTS payments
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                       user_id INTEGER, appointment_id INTEGER,
#                       amount REAL, method TEXT, status TEXT, date TEXT)''')
        
#         conn.commit()
#         conn.close()
        
#         if not os.path.exists('uploads'):
#             os.makedirs('uploads')
    
#     def hash_password(self, pwd):
#         return hashlib.sha256(pwd.encode()).hexdigest()
    
#     def show_login(self):
#         for w in self.root.winfo_children():
#             w.destroy()
        
#         # Header
#         header = tk.Frame(self.root, bg='#2c3e50', height=120)
#         header.pack(fill='x')
#         tk.Label(header, text="🏥 LifeLine+", font=('Arial', 32, 'bold'), 
#                 bg='#2c3e50', fg='white').pack(pady=25)
#         tk.Label(header, text="Smart Hospital Navigation & Booking System", 
#                 font=('Arial', 12), bg='#2c3e50', fg='#bdc3c7').pack()
        
#         # Login Frame
#         frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
#         frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=380)
        
#         tk.Label(frame, text="🔐 Login to Your Account", font=('Arial', 18, 'bold'), 
#                 bg='white', fg='#2c3e50').pack(pady=20)
        
#         tk.Label(frame, text="Email:", bg='white', font=('Arial', 11)).pack()
#         self.login_email = tk.Entry(frame, width=30, font=('Arial', 11))
#         self.login_email.pack(pady=5)
        
#         tk.Label(frame, text="Password:", bg='white', font=('Arial', 11)).pack()
#         self.login_pass = tk.Entry(frame, width=30, show='*', font=('Arial', 11))
#         self.login_pass.pack(pady=5)
        
#         tk.Button(frame, text="Login", command=self.do_login,
#                  bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
#                  width=20, height=1).pack(pady=10)
        
#         tk.Button(frame, text="Create New Account", command=self.show_signup,
#                  bg='#27ae60', fg='white', font=('Arial', 11), 
#                  width=20, height=1).pack()
    
#     def do_login(self):
#         email = self.login_email.get()
#         pwd = self.login_pass.get()
        
#         if not email or not pwd:
#             messagebox.showerror("Error", "Please enter email and password!")
#             return
        
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         c.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?",
#                   (email, self.hash_password(pwd)))
#         user = c.fetchone()
#         conn.close()
        
#         if user:
#             self.current_user = user
#             messagebox.showinfo("Success", f"Welcome {user[1]}!")
#             self.show_dashboard()
#         else:
#             messagebox.showerror("Error", "Invalid credentials!")
    
#     def show_signup(self):
#         for w in self.root.winfo_children():
#             w.destroy()
        
#         # Header
#         header = tk.Frame(self.root, bg='#2c3e50', height=80)
#         header.pack(fill='x')
#         tk.Label(header, text="📝 Create New Account", font=('Arial', 24, 'bold'), 
#                 bg='#2c3e50', fg='white').pack(pady=20)
        
#         # Signup Frame
#         frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
#         frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=550)
        
#         tk.Label(frame, text="Registration Form", font=('Arial', 18, 'bold'), 
#                 bg='white', fg='#2c3e50').pack(pady=15)
        
#         fields = ['Full Name', 'Email', 'Phone', 'Password', 'Confirm Password']
#         self.signup_entries = {}
        
#         for f in fields:
#             tk.Label(frame, text=f+':', bg='white', font=('Arial', 11)).pack()
#             e = tk.Entry(frame, width=35, font=('Arial', 11))
#             e.pack(pady=3)
#             if 'Password' in f:
#                 e.config(show='*')
#             self.signup_entries[f.lower()] = e
        
#         tk.Label(frame, text="User Type:", bg='white', font=('Arial', 11)).pack()
#         self.user_type = ttk.Combobox(frame, values=['Patient', 'Doctor'], width=33, font=('Arial', 11))
#         self.user_type.set('Patient')
#         self.user_type.pack(pady=5)
        
#         tk.Button(frame, text="Register", command=self.do_register,
#                  bg='#27ae60', fg='white', font=('Arial', 11, 'bold'), 
#                  width=20).pack(pady=15)
        
#         tk.Button(frame, text="Back to Login", command=self.show_login,
#                  bg='#95a5a6', fg='white', font=('Arial', 11), 
#                  width=20).pack()
    
#     def do_register(self):
#         name = self.signup_entries['full name'].get()
#         email = self.signup_entries['email'].get()
#         phone = self.signup_entries['phone'].get()
#         pwd = self.signup_entries['password'].get()
#         confirm = self.signup_entries['confirm password'].get()
#         utype = self.user_type.get().lower()
        
#         if not all([name, email, phone, pwd]):
#             messagebox.showerror("Error", "All fields required!")
#             return
        
#         if pwd != confirm:
#             messagebox.showerror("Error", "Passwords don't match!")
#             return
        
#         if len(pwd) < 6:
#             messagebox.showerror("Error", "Password must be at least 6 characters!")
#             return
        
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         try:
#             c.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
#                       (name, email, phone, self.hash_password(pwd), utype))
#             conn.commit()
#             messagebox.showinfo("Success", "Registration successful! Please login.")
#             self.show_login()
#         except sqlite3.IntegrityError:
#             messagebox.showerror("Error", "Email already exists!")
#         conn.close()
    
#     def show_dashboard(self):
#         for w in self.root.winfo_children():
#             w.destroy()
        
#         # Sidebar
#         sidebar = tk.Frame(self.root, bg='#2c3e50', width=250)
#         sidebar.pack(side='left', fill='y')
        
#         # User info
#         tk.Label(sidebar, text=f"👤 {self.current_user[1]}", 
#                 font=('Arial', 14, 'bold'), bg='#2c3e50', fg='white').pack(pady=20)
#         tk.Label(sidebar, text=f"({self.current_user[3].upper()})", 
#                 font=('Arial', 10), bg='#2c3e50', fg='#bdc3c7').pack()
        
#         tk.Frame(sidebar, bg='#34495e', height=2).pack(fill='x', pady=20)
        
#         # Menu buttons
#         menus = [
#             ("🏠 Dashboard", self.show_welcome),
#             ("📅 Book Appointment", self.book_appointment),
#             ("📋 My Appointments", self.view_appointments),
#             ("🗺️ Indoor Navigation", self.show_navigation),
#             ("🚨 Emergency", self.emergency),
#             ("💰 Make Payment", self.show_payments),
#             ("📜 Payment History", self.payment_history),
#             ("🤖 AI Health Assistant", self.ai_assistant),
#             ("📍 GPS Distance", self.gps_calculator),
#             ("🚪 Logout", self.show_login)
#         ]
        
#         for text, cmd in menus:
#             btn = tk.Button(sidebar, text=text, command=cmd,
#                            bg='#2c3e50', fg='white', relief='flat',
#                            anchor='w', padx=20, pady=10, font=('Arial', 11))
#             btn.pack(fill='x')
        
#         # Main content area
#         self.main = tk.Frame(self.root, bg='#f0f0f0')
#         self.main.pack(side='left', expand=True, fill='both', padx=20, pady=20)
        
#         self.show_welcome()
    
#     def show_welcome(self):
#         self.clear_main()
        
#         welcome_frame = tk.Frame(self.main, bg='#f0f0f0')
#         welcome_frame.pack(expand=True)
        
#         tk.Label(welcome_frame, text=f"Welcome to LifeLine+, {self.current_user[1]}!", 
#                 font=('Arial', 28, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=30)
        
#         tk.Label(welcome_frame, text="Your One-Stop Smart Hospital Management System", 
#                 font=('Arial', 14), bg='#f0f0f0', fg='#7f8c8d').pack()
        
#         # Stats
#         stats_frame = tk.Frame(welcome_frame, bg='#f0f0f0')
#         stats_frame.pack(pady=50)
        
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         c.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (self.current_user[0],))
#         appointments = c.fetchone()[0]
#         conn.close()
        
#         stats = [
#             ("📅 Appointments", appointments),
#             ("🏥 Departments", 5),
#             ("👨‍⚕️ Doctors", 12),
#             ("⭐ Rating", "4.8/5")
#         ]
        
#         for i, (label, value) in enumerate(stats):
#             frame = tk.Frame(stats_frame, bg='white', relief='ridge', bd=2)
#             frame.grid(row=0, column=i, padx=15, pady=10, ipadx=25, ipady=20)
#             tk.Label(frame, text=str(value), font=('Arial', 24, 'bold'), 
#                     bg='white', fg='#3498db').pack()
#             tk.Label(frame, text=label, font=('Arial', 12), 
#                     bg='white', fg='#7f8c8d').pack()
    
#     def book_appointment(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="📅 Book Appointment", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         # Create main frame
#         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
#         frame.pack(pady=20, padx=50, ipadx=30, ipady=30)
        
#         doctors = {
#             'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
#             'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
#             'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
#             'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
#             'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
#         }
        
#         time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
        
#         # Variables
#         self.dept_var = tk.StringVar()
#         self.doctor_var = tk.StringVar()
#         self.date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
#         self.time_var = tk.StringVar()
        
#         # Department
#         tk.Label(frame, text="Department:", font=('Arial', 12)).grid(row=0, column=0, pady=10, padx=10, sticky='w')
#         dept_combo = ttk.Combobox(frame, textvariable=self.dept_var, values=list(doctors.keys()), width=30, font=('Arial', 11))
#         dept_combo.grid(row=0, column=1, pady=10, padx=10)
        
#         # Doctor
#         tk.Label(frame, text="Doctor:", font=('Arial', 12)).grid(row=1, column=0, pady=10, padx=10, sticky='w')
#         self.doctor_combo = ttk.Combobox(frame, textvariable=self.doctor_var, width=30, font=('Arial', 11))
#         self.doctor_combo.grid(row=1, column=1, pady=10, padx=10)
        
#         def update_doctors(*args):
#             dept = self.dept_var.get()
#             if dept in doctors:
#                 self.doctor_combo['values'] = doctors[dept]
#         self.dept_var.trace('w', update_doctors)
        
#         # Date
#         tk.Label(frame, text="Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=2, column=0, pady=10, padx=10, sticky='w')
#         date_entry = tk.Entry(frame, textvariable=self.date_var, width=33, font=('Arial', 11))
#         date_entry.grid(row=2, column=1, pady=10, padx=10)
        
#         # Time
#         tk.Label(frame, text="Time:", font=('Arial', 12)).grid(row=3, column=0, pady=10, padx=10, sticky='w')
#         time_combo = ttk.Combobox(frame, textvariable=self.time_var, values=time_slots, width=30, font=('Arial', 11))
#         time_combo.grid(row=3, column=1, pady=10, padx=10)
        
#         def save_appointment():
#             dept = self.dept_var.get()
#             doctor = self.doctor_var.get()
#             date = self.date_var.get()
#             time_slot = self.time_var.get()
            
#             # Validation
#             if not dept:
#                 messagebox.showerror("Error", "Please select a department!")
#                 return
#             if not doctor:
#                 messagebox.showerror("Error", "Please select a doctor!")
#                 return
#             if not date:
#                 messagebox.showerror("Error", "Please enter a date!")
#                 return
#             if not time_slot:
#                 messagebox.showerror("Error", "Please select a time slot!")
#                 return
            
#             # Check if slot is available
#             conn = sqlite3.connect('hospital.db')
#             c = conn.cursor()
#             c.execute("SELECT * FROM appointments WHERE doctor_name=? AND date=? AND time=? AND status != 'cancelled'",
#                       (doctor, date, time_slot))
#             existing = c.fetchone()
            
#             if existing:
#                 messagebox.showerror("Error", "This time slot is already booked!\nPlease choose another time.")
#                 conn.close()
#                 return
            
#             # Book appointment
#             c.execute('''INSERT INTO appointments (user_id, doctor_name, department, date, time, status)
#                          VALUES (?,?,?,?,?,?)''',
#                       (self.current_user[0], doctor, dept, date, time_slot, 'pending'))
#             conn.commit()
#             appointment_id = c.lastrowid
#             conn.close()
            
#             messagebox.showinfo("Success", f"✅ Appointment Booked Successfully!\n\nID: {appointment_id}\nDoctor: {doctor}\nDate: {date}\nTime: {time_slot}\n\nPlease make payment to confirm your appointment.")
            
#             # Clear form
#             self.dept_var.set('')
#             self.doctor_var.set('')
#             self.time_var.set('')
            
#             # Ask if user wants to pay now
#             if messagebox.askyesno("Payment", "Would you like to make payment now?"):
#                 self.show_payments()
#             else:
#                 self.view_appointments()
        
#         tk.Button(frame, text="Book Appointment", command=save_appointment,
#                  bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
#                  width=25, height=1).grid(row=4, column=0, columnspan=2, pady=20)
    
#     def view_appointments(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="📋 My Appointments", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         c.execute("SELECT id, doctor_name, department, date, time, status FROM appointments WHERE user_id=? ORDER BY id DESC",
#                   (self.current_user[0],))
#         apps = c.fetchall()
#         conn.close()
        
#         if not apps:
#             tk.Label(self.main, text="No appointments found!", font=('Arial', 14),
#                     bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
#             return
        
#         # Treeview frame
#         tree_frame = tk.Frame(self.main, bg='#f0f0f0')
#         tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
#         # Scrollbars
#         scroll_y = ttk.Scrollbar(tree_frame, orient='vertical')
#         scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal')
        
#         columns = ('ID', 'Doctor', 'Department', 'Date', 'Time', 'Status')
#         tree = ttk.Treeview(tree_frame, columns=columns, show='headings', 
#                            yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
#         scroll_y.config(command=tree.yview)
#         scroll_x.config(command=tree.xview)
        
#         for col in columns:
#             tree.heading(col, text=col)
#             tree.column(col, width=150)
        
#         for app in apps:
#             tree.insert('', 'end', values=app)
        
#         tree.grid(row=0, column=0, sticky='nsew')
#         scroll_y.grid(row=0, column=1, sticky='ns')
#         scroll_x.grid(row=1, column=0, sticky='ew')
        
#         tree_frame.grid_rowconfigure(0, weight=1)
#         tree_frame.grid_columnconfigure(0, weight=1)
        
#         # Cancel section
#         cancel_frame = tk.Frame(self.main, bg='#f0f0f0')
#         cancel_frame.pack(pady=20)
        
#         tk.Label(cancel_frame, text="Enter Appointment ID to cancel:", font=('Arial', 11)).pack(side='left', padx=10)
#         self.cancel_id = tk.Entry(cancel_frame, width=15, font=('Arial', 11))
#         self.cancel_id.pack(side='left', padx=10)
        
#         def cancel_appointment():
#             app_id = self.cancel_id.get()
#             if not app_id:
#                 messagebox.showerror("Error", "Please enter appointment ID!")
#                 return
            
#             conn = sqlite3.connect('hospital.db')
#             c = conn.cursor()
#             c.execute("SELECT status FROM appointments WHERE id=? AND user_id=?", (app_id, self.current_user[0]))
#             app = c.fetchone()
            
#             if not app:
#                 messagebox.showerror("Error", "Appointment not found!")
#                 conn.close()
#                 return
            
#             if app[0] == 'cancelled':
#                 messagebox.showerror("Error", "Appointment is already cancelled!")
#                 conn.close()
#                 return
            
#             c.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", 
#                      (app_id, self.current_user[0]))
#             conn.commit()
#             conn.close()
            
#             messagebox.showinfo("Success", f"Appointment #{app_id} cancelled successfully!")
#             self.cancel_id.delete(0, tk.END)
#             self.view_appointments()
        
#         tk.Button(cancel_frame, text="Cancel Appointment", command=cancel_appointment,
#                  bg='#e74c3c', fg='white', font=('Arial', 11), width=20).pack(side='left', padx=10)
    
#     def show_payments(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="💰 Make Payment", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         # Get pending appointments
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         c.execute("SELECT id, doctor_name, department, date, time FROM appointments WHERE user_id=? AND status='pending'",
#                   (self.current_user[0],))
#         pending_apps = c.fetchall()
#         conn.close()
        
#         if not pending_apps:
#             tk.Label(self.main, text="No pending appointments for payment!", 
#                     font=('Arial', 14), bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
            
#             # Show all appointments button
#             tk.Button(self.main, text="View My Appointments", command=self.view_appointments,
#                      bg='#3498db', fg='white', font=('Arial', 12), width=20).pack(pady=20)
#             return
        
#         # Payment frame
#         payment_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
#         payment_frame.pack(pady=20, padx=50, ipadx=30, ipady=30)
        
#         tk.Label(payment_frame, text="Select Appointment for Payment:", font=('Arial', 12, 'bold'), 
#                 bg='white').grid(row=0, column=0, pady=10, padx=10, sticky='w')
        
#         app_list = [f"ID:{app[0]} - {app[1]} - {app[3]} {app[4]}" for app in pending_apps]
#         self.payment_app_var = tk.StringVar()
#         app_combo = ttk.Combobox(payment_frame, textvariable=self.payment_app_var, 
#                                  values=app_list, width=45, font=('Arial', 11))
#         app_combo.grid(row=0, column=1, pady=10, padx=10)
        
#         tk.Label(payment_frame, text="Amount (₹):", font=('Arial', 12), bg='white').grid(row=1, column=0, pady=10, padx=10, sticky='w')
#         self.amount_entry = tk.Entry(payment_frame, width=20, font=('Arial', 11))
#         self.amount_entry.insert(0, "500")
#         self.amount_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')
        
#         tk.Label(payment_frame, text="Payment Method:", font=('Arial', 12), bg='white').grid(row=2, column=0, pady=10, padx=10, sticky='w')
#         self.method_var = tk.StringVar(value='UPI')
#         method_combo = ttk.Combobox(payment_frame, textvariable=self.method_var, 
#                                     values=['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash'], 
#                                     width=28, font=('Arial', 11))
#         method_combo.grid(row=2, column=1, pady=10, padx=10, sticky='w')
        
#         def process_payment():
#             if not self.payment_app_var.get():
#                 messagebox.showerror("Error", "Please select an appointment!")
#                 return
            
#             # Extract appointment ID
#             try:
#                 app_id = self.payment_app_var.get().split('-')[0].replace('ID:', '').strip()
#                 amount = float(self.amount_entry.get())
#                 method = self.method_var.get()
#             except:
#                 messagebox.showerror("Error", "Invalid input!")
#                 return
            
#             # Process payment
#             conn = sqlite3.connect('hospital.db')
#             c = conn.cursor()
            
#             # Insert payment record
#             c.execute("INSERT INTO payments (user_id, appointment_id, amount, method, status, date) VALUES (?,?,?,?,?,?)",
#                       (self.current_user[0], app_id, amount, method, 'completed', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
#             # Update appointment status
#             c.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (app_id,))
            
#             conn.commit()
#             conn.close()
            
#             # Generate transaction ID
#             trans_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
#             messagebox.showinfo("Payment Successful", 
#                                f"✅ Payment Completed!\n\n"
#                                f"Amount: ₹{amount}\n"
#                                f"Method: {method}\n"
#                                f"Transaction ID: {trans_id}\n\n"
#                                f"Your appointment has been confirmed.")
            
#             self.show_payments()
        
#         tk.Button(payment_frame, text="Pay Now", command=process_payment,
#                  bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
#                  width=20).grid(row=3, column=0, columnspan=2, pady=20)
    
#     def payment_history(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="📜 Payment History", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         conn = sqlite3.connect('hospital.db')
#         c = conn.cursor()
#         c.execute("SELECT id, appointment_id, amount, method, status, date FROM payments WHERE user_id=? ORDER BY id DESC",
#                   (self.current_user[0],))
#         payments = c.fetchall()
#         conn.close()
        
#         if not payments:
#             tk.Label(self.main, text="No payment records found!", font=('Arial', 14),
#                     bg='#f0f0f0', fg='#7f8c8d').pack(pady=50)
#             return
        
#         # Treeview
#         tree_frame = tk.Frame(self.main, bg='#f0f0f0')
#         tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
#         scroll_y = ttk.Scrollbar(tree_frame, orient='vertical')
#         scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal')
        
#         columns = ('ID', 'Appointment ID', 'Amount (₹)', 'Method', 'Status', 'Date')
#         tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
#                            yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
#         scroll_y.config(command=tree.yview)
#         scroll_x.config(command=tree.xview)
        
#         for col in columns:
#             tree.heading(col, text=col)
#             tree.column(col, width=150)
        
#         total_amount = 0
#         for payment in payments:
#             tree.insert('', 'end', values=payment)
#             total_amount += payment[2]
        
#         tree.grid(row=0, column=0, sticky='nsew')
#         scroll_y.grid(row=0, column=1, sticky='ns')
#         scroll_x.grid(row=1, column=0, sticky='ew')
        
#         tree_frame.grid_rowconfigure(0, weight=1)
#         tree_frame.grid_columnconfigure(0, weight=1)
        
#         # Total amount
#         total_frame = tk.Frame(self.main, bg='#f0f0f0')
#         total_frame.pack(pady=20)
#         tk.Label(total_frame, text=f"Total Amount Paid: ₹{total_amount}", 
#                 font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#27ae60').pack()
    
#     def show_navigation(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="🗺️ Indoor Navigation", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 
#                     'Pediatrics', 'Orthopedics', 'Emergency', 'Pharmacy', 'Cafeteria']
        
#         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
#         frame.pack(pady=20, padx=50, ipadx=20, ipady=20, fill='both', expand=True)
        
#         # Left side
#         left_frame = tk.Frame(frame, bg='white')
#         left_frame.pack(side='left', padx=20, pady=20, fill='both', expand=True)
        
#         tk.Label(left_frame, text="📍 Current Location:", font=('Arial', 12, 'bold'), bg='white').pack(anchor='w')
#         self.nav_start = ttk.Combobox(left_frame, values=locations, width=30, font=('Arial', 11))
#         self.nav_start.pack(pady=5, anchor='w')
        
#         tk.Label(left_frame, text="🎯 Destination:", font=('Arial', 12, 'bold'), bg='white').pack(anchor='w', pady=(10,0))
#         self.nav_end = ttk.Combobox(left_frame, values=locations, width=30, font=('Arial', 11))
#         self.nav_end.pack(pady=5, anchor='w')
        
#         # Directions text
#         self.directions_text = tk.Text(left_frame, height=12, width=50, font=('Arial', 10), bg='#f0f0f0')
#         self.directions_text.pack(pady=20)
        
#         # Right side - Map
#         right_frame = tk.Frame(frame, bg='#ecf0f1', relief='ridge', bd=1)
#         right_frame.pack(side='right', padx=20, pady=20, fill='both', expand=True)
        
#         tk.Label(right_frame, text="Hospital Map", font=('Arial', 14, 'bold'), bg='#ecf0f1').pack(pady=10)
        
#         map_text = tk.Text(right_frame, height=15, width=35, font=('Courier', 9), bg='#ecf0f1')
#         map_text.pack(padx=10, pady=10)
        
#         hospital_map = """
#     ┌────────────────────────────────────┐
#     │      [Entrance]                    │
#     │         ↓                          │
#     │      [Reception]                   │
#     │    ↙      ↓      ↘                │
#     │[Cardiology] [Emergency] [Pharmacy] |
#     │    ↓         ↓                     │
#     │[Neurology] [Orthopedics]           │
#     │    ↓                               │
#     │[Pediatrics]                        │
#     └────────────────────────────────────┘
#         """
#         map_text.insert('1.0', hospital_map)
#         map_text.config(state='disabled')
        
#         def get_directions():
#             start = self.nav_start.get()
#             end = self.nav_end.get()
            
#             if not start or not end:
#                 messagebox.showerror("Error", "Please select both locations!")
#                 return
            
#             self.directions_text.delete(1.0, tk.END)
            
#             directions = f"""
# 📍 DIRECTIONS from {start} to {end}
# {'='*50}

# → Walk straight towards the main corridor
# → Take the elevator to the appropriate floor
# → Follow the color-coded signs:
#    • Blue signs - Medical departments
#    • Green signs - Services
# → Turn right/left as per the signboards
# → You have reached {end}

# 📏 Approximate distance: 50-200 meters
# ⏱️ Estimated time: 2-8 minutes

# 💡 Tip: Follow the green line on the floor
#             """
#             self.directions_text.insert(1.0, directions)
        
#         tk.Button(frame, text="Get Directions", command=get_directions,
#                  bg='#3498db', fg='white', font=('Arial', 12, 'bold'), 
#                  width=20).pack(pady=20)
    
#     def emergency(self):
#         self.clear_main()
        
#         emergency_frame = tk.Frame(self.main, bg='#ff4444', relief='ridge', bd=3)
#         emergency_frame.pack(expand=True, fill='both', padx=50, pady=50)
        
#         tk.Label(emergency_frame, text="🚨 EMERGENCY MODE 🚨", 
#                 font=('Arial', 32, 'bold'), bg='#ff4444', fg='white').pack(pady=30)
        
#         tk.Label(emergency_frame, text="⚠️ This is for real emergencies only!", 
#                 font=('Arial', 14), bg='#ff4444', fg='yellow').pack()
        
#         # Emergency type
#         tk.Label(emergency_frame, text="Select Emergency Type:", 
#                 font=('Arial', 14), bg='#ff4444', fg='white').pack(pady=10)
        
#         emergency_types = ['Medical Emergency', 'Accident', 'Cardiac Arrest', 'Breathing Difficulty', 'Other']
#         self.emergency_type = tk.StringVar(value='Medical Emergency')
#         emergency_combo = ttk.Combobox(emergency_frame, textvariable=self.emergency_type, 
#                                        values=emergency_types, width=30, font=('Arial', 12))
#         emergency_combo.pack(pady=10)
        
#         def activate_emergency():
#             emergency_type = self.emergency_type.get()
            
#             # Save to database
#             conn = sqlite3.connect('hospital.db')
#             c = conn.cursor()
#             c.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
#                       (self.current_user[0], "Hospital Location", emergency_type, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#             conn.commit()
#             conn.close()
            
#             # Show response window
#             response = Toplevel(self.root)
#             response.title("🚑 Emergency Response")
#             response.geometry("500x450")
#             response.configure(bg='#ff4444')
            
#             # Center window
#             response.update_idletasks()
#             x = (response.winfo_screenwidth() // 2) - (500 // 2)
#             y = (response.winfo_screenheight() // 2) - (450 // 2)
#             response.geometry(f'500x450+{x}+{y}')
            
#             tk.Label(response, text="🚑 EMERGENCY TEAM DISPATCHED!", 
#                     font=('Arial', 18, 'bold'), bg='#ff4444', fg='white').pack(pady=20)
            
#             tk.Label(response, text=f"Patient: {self.current_user[1]}", 
#                     font=('Arial', 14), bg='#ff4444', fg='white').pack(pady=5)
#             tk.Label(response, text=f"Emergency Type: {emergency_type}", 
#                     font=('Arial', 14), bg='#ff4444', fg='white').pack(pady=5)
#             tk.Label(response, text="⏱️ Estimated arrival: 5 minutes", 
#                     font=('Arial', 14), bg='#ff4444', fg='yellow').pack(pady=10)
            
#             instructions = """
# 📋 INSTRUCTIONS:
# • Stay calm and don't panic
# • Do not move if you have injuries
# • Keep your phone accessible
# • Medical help is arriving shortly
# • Ambulance has been dispatched
#             """
#             tk.Label(response, text=instructions, font=('Arial', 11), 
#                     bg='#ff4444', fg='white', justify='left').pack(pady=20)
            
#             tk.Button(response, text="OK", command=response.destroy,
#                      font=('Arial', 12, 'bold'), bg='white', fg='#ff4444', 
#                      width=15).pack(pady=10)
        
#         tk.Button(emergency_frame, text="🚑 ACTIVATE EMERGENCY 🚑", command=activate_emergency,
#                  font=('Arial', 18, 'bold'), bg='#cc0000', fg='white',
#                  width=30, height=2).pack(pady=30)
    
#     def ai_assistant(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="🤖 AI Health Assistant", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
#         frame.pack(pady=20, padx=50, ipadx=20, ipady=20, fill='both', expand=True)
        
#         tk.Label(frame, text="Describe your symptoms:", font=('Arial', 12, 'bold'), 
#                 bg='white').pack(anchor='w', pady=10)
        
#         self.symptoms_text = scrolledtext.ScrolledText(frame, height=5, width=60, font=('Arial', 11))
#         self.symptoms_text.pack(pady=10, fill='x')
        
#         tk.Label(frame, text="Analysis Results:", font=('Arial', 12, 'bold'), 
#                 bg='white').pack(anchor='w', pady=10)
        
#         self.result_text = scrolledtext.ScrolledText(frame, height=10, width=60, font=('Arial', 11), bg='#f0f0f0')
#         self.result_text.pack(pady=10, fill='both', expand=True)
        
#         def analyze():
#             symptoms = self.symptoms_text.get(1.0, tk.END).lower()
#             self.result_text.delete(1.0, tk.END)
            
#             result = "📊 SYMPTOM ANALYSIS\n"
#             result += "="*50 + "\n\n"
            
#             advice = {
#                 'fever': ('🤒 Fever', '• Rest and stay hydrated\n• Monitor temperature\n• Take paracetamol if > 101°F'),
#                 'cough': ('🤧 Cough', '• Use mask\n• Avoid cold drinks\n• Steam inhalation'),
#                 'headache': ('🤕 Headache', '• Rest in dark room\n• Stay hydrated\n• Avoid screen time'),
#                 'chest': ('⚠️ Chest Pain', '• SEEK IMMEDIATE MEDICAL ATTENTION!'),
#                 'back': ('💪 Back Pain', '• Apply ice pack\n• Gentle stretching\n• Maintain posture'),
#                 'cold': ('😷 Cold', '• Steam inhalation\n• Drink warm fluids\n• Take rest'),
#                 'stomach': ('🍽️ Stomach Issue', '• Avoid spicy food\n• Drink ORS\n• Eat bland food'),
#             }
            
#             found = False
#             departments = set()
            
#             for key, (title, text) in advice.items():
#                 if key in symptoms:
#                     found = True
#                     result += f"{title}\n{text}\n\n"
#                     if 'chest' in key:
#                         departments.add('Cardiology (Emergency)')
#                     elif 'fever' in key or 'cold' in key:
#                         departments.add('General Medicine')
#                     elif 'headache' in key:
#                         departments.add('Neurology')
#                     elif 'back' in key:
#                         departments.add('Orthopedics')
            
#             if not found:
#                 result += "No specific symptoms detected.\n• General checkup recommended\n"
#                 departments.add('General Medicine')
            
#             result += "\n" + "="*50 + "\n"
#             result += f"💡 Recommended: {', '.join(departments)}\n"
#             result += "📅 Book an appointment with a doctor"
            
#             self.result_text.insert(1.0, result)
        
#         tk.Button(frame, text="Analyze Symptoms", command=analyze,
#                  bg='#9b59b6', fg='white', font=('Arial', 12, 'bold'), 
#                  width=25).pack(pady=10)
    
#     def gps_calculator(self):
#         self.clear_main()
        
#         tk.Label(self.main, text="📍 GPS Distance Calculator", font=('Arial', 24, 'bold'),
#                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
#         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
#         frame.pack(pady=20, padx=50, ipadx=30, ipady=30, fill='both', expand=True)
        
#         locations = {
#             'Downtown': (28.6139, 77.2090),
#             'North Side': (28.6500, 77.2300),
#             'South Side': (28.5800, 77.1900),
#             'East End': (28.6200, 77.2500),
#             'West End': (28.6000, 77.1700)
#         }
        
#         tk.Label(frame, text="Select Your Location:", font=('Arial', 12, 'bold'), 
#                 bg='white').pack(anchor='w', pady=10)
        
#         self.gps_location = ttk.Combobox(frame, values=list(locations.keys()), width=30, font=('Arial', 11))
#         self.gps_location.pack(anchor='w', pady=5)
        
#         self.gps_result = tk.Text(frame, height=12, width=60, font=('Arial', 11), bg='#f0f0f0')
#         self.gps_result.pack(pady=20)
        
#         def calculate():
#             location = self.gps_location.get()
#             if not location:
#                 messagebox.showerror("Error", "Please select your location!")
#                 return
            
#             distance = random.uniform(0.5, 15.0)
            
#             self.gps_result.delete(1.0, tk.END)
#             result = f"""
# 📍 Location: {location}
# 🏥 Hospital: City Hospital

# 📏 Distance: {distance:.1f} km

# 🚗 By Car: {distance * 2:.0f} minutes
# 🚶 By Walk: {distance * 12:.0f} minutes
# 🚑 Ambulance: {distance * 1.5:.0f} minutes

# 💰 Estimated Fare: ₹{distance * 15:.0f}

# 💡 Hospital has free parking
# 💡 Emergency entrance on east side
#             """
#             self.gps_result.insert(1.0, result)
        
#         tk.Button(frame, text="Calculate Distance", command=calculate,
#                  bg='#3498db', fg='white', font=('Arial', 12, 'bold'), 
#                  width=25).pack(pady=10)
    
#     def clear_main(self):
#         for widget in self.main.winfo_children():
#             widget.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HospitalApp(root)
#     root.mainloop()





















































































import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import sqlite3
import hashlib
from datetime import datetime
import os

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LifeLine+ Smart Hospital System")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')
        self.center_window()
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
        """Create database with all tables"""
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        
        # Users table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT DEFAULT 'patient'
        )''')
        
        # Appointments table
        c.execute('''CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            doctor_name TEXT NOT NULL,
            department TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )''')
        
        # Emergency table
        c.execute('''CREATE TABLE IF NOT EXISTS emergencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            location TEXT,
            emergency_type TEXT,
            created_at TEXT
        )''')
        
        # Payments table
        c.execute('''CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            appointment_id INTEGER,
            amount REAL NOT NULL,
            payment_method TEXT,
            status TEXT DEFAULT 'pending',
            payment_date TEXT
        )''')
        
        conn.commit()
        conn.close()
        
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        
        print("Database created successfully!")
    
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
                 width=20, height=1).pack(pady=10)
        
        tk.Button(frame, text="Create New Account", command=self.show_signup,
                 bg='#27ae60', fg='white', font=('Arial', 11), 
                 width=20, height=1).pack()
    
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
        appointments = c.fetchone()[0]
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
        
        # Create form frame
        form_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        form_frame.pack(pady=30, padx=50, ipadx=40, ipady=40)
        
        doctors = {
            'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
            'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
            'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
            'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
            'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
        }
        
        time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
        
        # Variables
        dept_var = tk.StringVar()
        doctor_var = tk.StringVar()
        date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        time_var = tk.StringVar()
        
        # Department
        tk.Label(form_frame, text="Select Department:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10, sticky='w')
        dept_combo = ttk.Combobox(form_frame, textvariable=dept_var, values=list(doctors.keys()), width=35, font=('Arial', 11))
        dept_combo.grid(row=0, column=1, pady=10, padx=10)
        
        # Doctor
        tk.Label(form_frame, text="Select Doctor:", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10, sticky='w')
        doctor_combo = ttk.Combobox(form_frame, textvariable=doctor_var, width=35, font=('Arial', 11))
        doctor_combo.grid(row=1, column=1, pady=10, padx=10)
        
        def update_doctors(*args):
            dept = dept_var.get()
            if dept in doctors:
                doctor_combo['values'] = doctors[dept]
        dept_var.trace('w', update_doctors)
        
        # Date
        tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=('Arial', 12, 'bold')).grid(row=2, column=0, pady=10, padx=10, sticky='w')
        date_entry = tk.Entry(form_frame, textvariable=date_var, width=38, font=('Arial', 11))
        date_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Time
        tk.Label(form_frame, text="Select Time:", font=('Arial', 12, 'bold')).grid(row=3, column=0, pady=10, padx=10, sticky='w')
        time_combo = ttk.Combobox(form_frame, textvariable=time_var, values=time_slots, width=35, font=('Arial', 11))
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
            
            # Save to database
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            # Check if slot is available
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
            
            messagebox.showinfo("Success", f"✅ Appointment Booked Successfully!\n\nBooking ID: {app_id}\nDoctor: {doctor}\nDate: {date}\nTime: {time_slot}\n\nPlease make payment to confirm.")
            
            # Clear form
            dept_var.set('')
            doctor_var.set('')
            time_var.set('')
            
            # Ask for payment
            if messagebox.askyesno("Payment", "Would you like to make payment now?"):
                self.show_payments()
        
        tk.Button(form_frame, text="Book Appointment", command=save_booking,
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                 width=25, height=1).grid(row=4, column=0, columnspan=2, pady=20)
    
    def view_appointments(self):
        self.clear_main()
        
        tk.Label(self.main, text="📋 My Appointments", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        # Get appointments from database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC", 
                  (self.current_user[0],))
        appointments = c.fetchall()
        conn.close()
        
        if not appointments:
            tk.Label(self.main, text="No appointments found!", font=('Arial', 14),
                    bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
            return
        
        # Create treeview
        tree_frame = tk.Frame(self.main, bg='#f0f0f0')
        tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        columns = ('ID', 'Doctor', 'Department', 'Date', 'Time', 'Status')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        for app in appointments:
            tree.insert('', 'end', values=app)
        
        tree.pack(fill='both', expand=True)
        
        # Cancel appointment section
        cancel_frame = tk.Frame(self.main, bg='#f0f0f0')
        cancel_frame.pack(pady=20)
        
        tk.Label(cancel_frame, text="Enter Appointment ID to Cancel:", font=('Arial', 11)).pack(side='left', padx=10)
        cancel_id = tk.Entry(cancel_frame, width=15, font=('Arial', 11))
        cancel_id.pack(side='left', padx=10)
        
        def cancel_booking():
            app_id = cancel_id.get()
            if not app_id:
                messagebox.showerror("Error", "Please enter appointment ID!")
                return
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            c.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", (app_id, self.current_user[0]))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", f"Appointment #{app_id} cancelled successfully!")
            cancel_id.delete(0, tk.END)
            self.view_appointments()
        
        tk.Button(cancel_frame, text="Cancel Appointment", command=cancel_booking,
                 bg='#e74c3c', fg='white', font=('Arial', 11), width=20).pack(side='left', padx=10)
    
    def show_payments(self):
        self.clear_main()
        
        tk.Label(self.main, text="💰 Make Payment", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        # Get pending appointments
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
                     bg='#3498db', fg='white', font=('Arial', 12), width=20).pack(pady=20)
            return
        
        # Payment form
        payment_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        payment_frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(payment_frame, text="Select Appointment:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10, sticky='w')
        
        app_list = [f"ID:{app[0]} - {app[1]} - {app[3]} {app[4]}" for app in pending_apps]
        app_var = tk.StringVar()
        app_combo = ttk.Combobox(payment_frame, textvariable=app_var, values=app_list, width=40, font=('Arial', 11))
        app_combo.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(payment_frame, text="Amount (₹):", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10, sticky='w')
        amount_entry = tk.Entry(payment_frame, width=20, font=('Arial', 11))
        amount_entry.insert(0, "500")
        amount_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')
        
        tk.Label(payment_frame, text="Payment Method:", font=('Arial', 12, 'bold')).grid(row=2, column=0, pady=10, padx=10, sticky='w')
        method_var = tk.StringVar(value='UPI')
        method_combo = ttk.Combobox(payment_frame, textvariable=method_var, 
                                   values=['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash'], 
                                   width=28, font=('Arial', 11))
        method_combo.grid(row=2, column=1, pady=10, padx=10, sticky='w')
        
        def process_payment():
            if not app_var.get():
                messagebox.showerror("Error", "Please select an appointment!")
                return
            
            # Extract appointment ID
            app_id = app_var.get().split('-')[0].replace('ID:', '').strip()
            amount = float(amount_entry.get())
            method = method_var.get()
            
            # Save payment
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            c.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, payment_date) VALUES (?,?,?,?,?,?)",
                     (self.current_user[0], app_id, amount, method, 'completed', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            c.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (app_id,))
            conn.commit()
            conn.close()
            
            trans_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"
            messagebox.showinfo("Success", f"✅ Payment Successful!\n\nAmount: ₹{amount}\nMethod: {method}\nTransaction ID: {trans_id}\n\nYour appointment is confirmed!")
            
            self.show_payments()
        
        tk.Button(payment_frame, text="Pay Now", command=process_payment,
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
                 width=20).grid(row=3, column=0, columnspan=2, pady=20)
    
    def payment_history(self):
        self.clear_main()
        
        tk.Label(self.main, text="📜 Payment History", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT id, appointment_id, amount, payment_method, status, payment_date FROM payments WHERE user_id=? ORDER BY id DESC",
                  (self.current_user[0],))
        payments = c.fetchall()
        conn.close()
        
        if not payments:
            tk.Label(self.main, text="No payment records found!", font=('Arial', 14),
                    bg='#f0f0f0', fg='#7f8c8d').pack(pady=50)
            return
        
        tree_frame = tk.Frame(self.main, bg='#f0f0f0')
        tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        columns = ('ID', 'Appointment ID', 'Amount (₹)', 'Method', 'Status', 'Date')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        total = 0
        for payment in payments:
            tree.insert('', 'end', values=payment)
            total += payment[2]
        
        tree.pack(fill='both', expand=True)
        
        total_frame = tk.Frame(self.main, bg='#f0f0f0')
        total_frame.pack(pady=20)
        tk.Label(total_frame, text=f"Total Amount Paid: ₹{total}", 
                font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#27ae60').pack()
    
    def show_navigation(self):
        self.clear_main()
        
        tk.Label(self.main, text="🗺️ Indoor Navigation", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 'Emergency', 'Pharmacy']
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(frame, text="Current Location:", font=('Arial', 12)).grid(row=0, column=0, pady=10, padx=10)
        start = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
        start.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(frame, text="Destination:", font=('Arial', 12)).grid(row=1, column=0, pady=10, padx=10)
        end = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
        end.grid(row=1, column=1, pady=10, padx=10)
        
        directions = tk.Text(frame, height=8, width=50, font=('Arial', 10))
        directions.grid(row=2, column=0, columnspan=2, pady=20, padx=10)
        
        def get_directions():
            s = start.get()
            e = end.get()
            if s and e:
                directions.delete(1.0, tk.END)
                directions.insert(1.0, f"📍 From {s} to {e}\n\n→ Walk straight to main corridor\n→ Take elevator to appropriate floor\n→ Follow signs\n→ You have reached {e}\n\n⏱️ Estimated time: 5-10 minutes")
        
        tk.Button(frame, text="Get Directions", command=get_directions,
                 bg='#3498db', fg='white', font=('Arial', 12), width=20).grid(row=3, column=0, columnspan=2, pady=10)
    
    def emergency(self):
        self.clear_main()
        
        frame = tk.Frame(self.main, bg='#ff4444', relief='ridge', bd=3)
        frame.pack(expand=True, fill='both', padx=50, pady=50)
        
        tk.Label(frame, text="🚨 EMERGENCY MODE 🚨", font=('Arial', 28, 'bold'), 
                bg='#ff4444', fg='white').pack(pady=30)
        
        tk.Label(frame, text="⚠️ This is for real emergencies only!", 
                font=('Arial', 14), bg='#ff4444', fg='yellow').pack()
        
        def activate():
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            c.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
                     (self.current_user[0], "Hospital", "Medical Emergency", datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            conn.close()
            
            msg = Toplevel(self.root)
            msg.title("Emergency Response")
            msg.geometry("400x300")
            msg.configure(bg='#ff4444')
            tk.Label(msg, text="🚑 EMERGENCY TEAM DISPATCHED!", font=('Arial', 16, 'bold'), 
                    bg='#ff4444', fg='white').pack(pady=30)
            tk.Label(msg, text=f"Patient: {self.current_user[1]}", font=('Arial', 12), 
                    bg='#ff4444', fg='white').pack()
            tk.Label(msg, text="⏱️ Estimated arrival: 5 minutes", font=('Arial', 12), 
                    bg='#ff4444', fg='yellow').pack(pady=20)
            tk.Button(msg, text="OK", command=msg.destroy, bg='white', fg='black').pack(pady=20)
        
        tk.Button(frame, text="🚑 ACTIVATE EMERGENCY 🚑", command=activate,
                 font=('Arial', 18, 'bold'), bg='#cc0000', fg='white', 
                 width=30, height=2).pack(pady=30)
    
    def ai_assistant(self):
        self.clear_main()
        
        tk.Label(self.main, text="🤖 AI Health Assistant", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        tk.Label(frame, text="Describe your symptoms:", font=('Arial', 12)).pack()
        symptoms = tk.Text(frame, height=5, width=50, font=('Arial', 11))
        symptoms.pack(pady=10)
        
        result = tk.Text(frame, height=8, width=50, font=('Arial', 11), bg='#f0f0f0')
        result.pack(pady=10)
        
        def analyze():
            text = symptoms.get(1.0, tk.END).lower()
            result.delete(1.0, tk.END)
            
            advice = ""
            if 'fever' in text:
                advice += "• Fever: Rest and stay hydrated\n"
            if 'cough' in text:
                advice += "• Cough: Use mask, avoid cold\n"
            if 'headache' in text:
                advice += "• Headache: Rest in dark room\n"
            if 'chest' in text:
                advice += "⚠️ Chest pain: Seek immediate medical attention!\n"
            
            if advice:
                result.insert(1.0, f"Analysis:\n{advice}\n\nRecommended: Book a doctor's appointment")
            else:
                result.insert(1.0, "No specific symptoms detected. Consider a general checkup.")
        
        tk.Button(frame, text="Analyze", command=analyze,
                 bg='#9b59b6', fg='white', font=('Arial', 12), width=20).pack()
    
    def gps_calculator(self):
        self.clear_main()
        
        tk.Label(self.main, text="📍 GPS Distance Calculator", font=('Arial', 24, 'bold'),
                bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
        frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
        frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
        locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
        
        tk.Label(frame, text="Select your location:", font=('Arial', 12)).pack()
        location = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
        location.pack(pady=10)
        
        result = tk.Text(frame, height=8, width=50, font=('Arial', 11), bg='#f0f0f0')
        result.pack(pady=10)
        
        def calculate():
            loc = location.get()
            if loc:
                import random
                dist = random.uniform(1, 15)
                result.delete(1.0, tk.END)
                result.insert(1.0, f"📍 From {loc} to Hospital\n\n📏 Distance: {dist:.1f} km\n🚗 Driving: {dist*2:.0f} minutes\n🚶 Walking: {dist*12:.0f} minutes\n💰 Estimated fare: ₹{dist*15:.0f}")
        
        tk.Button(frame, text="Calculate", command=calculate,
                 bg='#3498db', fg='white', font=('Arial', 12), width=20).pack()
    
    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()