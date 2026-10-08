import sqlite3
from datetime import datetime


def ensure_payment_schema():
    """Support both legacy created_at and current payment_date columns."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    columns = [row[1] for row in cursor.execute('PRAGMA table_info(payments)')]
    if 'payment_date' not in columns:
        cursor.execute('ALTER TABLE payments ADD COLUMN payment_date TEXT')
    if 'created_at' not in columns:
        cursor.execute('ALTER TABLE payments ADD COLUMN created_at TEXT')
    conn.commit()
    conn.close()


def get_payment_timestamp_column():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    columns = [row[1] for row in cursor.execute('PRAGMA table_info(payments)')]
    conn.close()
    if 'payment_date' in columns:
        return 'payment_date'
    if 'created_at' in columns:
        return 'created_at'
    return 'payment_date'


def make_payment(user_id, appointment_id, amount):
    """Simulate payment processing"""
    ensure_payment_schema()
    timestamp_col = get_payment_timestamp_column()

    print("\n" + "="*50)
    print("💰 PAYMENT PROCESSING")
    print("="*50)

    print(f"\nAppointment ID: {appointment_id}")
    print(f"Amount: ₹{amount}")

    print("\nPayment Methods:")
    print("1. Credit/Debit Card")
    print("2. UPI (Google Pay, PhonePe, etc.)")
    print("3. Net Banking")
    print("4. Cash at Hospital")

    method_choice = input("\nSelect payment method (1-4): ")

    payment_methods = {
        '1': 'Card',
        '2': 'UPI',
        '3': 'Net Banking',
        '4': 'Cash'
    }

    payment_method = payment_methods.get(method_choice, 'Unknown')

    # Simulate payment processing
    print("\n⏳ Processing payment...")
    import time
    time.sleep(2)

    # Generate transaction ID
    transaction_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Save to database
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        cursor.execute(
            f"INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, {timestamp_col}) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, appointment_id, amount, payment_method, 'completed', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )

        conn.commit()

        # Update appointment status
        cursor.execute('''
            UPDATE appointments SET status = 'confirmed'
            WHERE id = ?
        ''', (appointment_id,))

        conn.commit()
        conn.close()

        print("\n✅ PAYMENT SUCCESSFUL!")
        print(f"📋 Transaction ID: {transaction_id}")
        print(f"💳 Method: {payment_method}")
        print(f"💰 Amount: ₹{amount}")

        # Send confirmation
        print("\n📧 Payment receipt sent to your registered email")

        return True

    except Exception as e:
        print(f"❌ Payment failed: {e}")
        return False


def view_payment_history(user_id):
    """View user's payment history"""
    print("\n" + "="*50)
    print("📋 PAYMENT HISTORY")
    print("="*50)

    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT p.id, p.amount, p.payment_method, p.status, COALESCE(p.payment_date, p.created_at) AS payment_date, a.doctor_name
            FROM payments p
            LEFT JOIN appointments a ON p.appointment_id = a.id
            WHERE p.user_id = ?
            ORDER BY COALESCE(p.payment_date, p.created_at) DESC
        ''', (user_id,))

        payments = cursor.fetchall()
        conn.close()

        if not payments:
            print("No payment records found.")
            return

        print(f"\n{'ID':<5} {'Amount':<10} {'Method':<12} {'Status':<10} {'Doctor':<20} {'Date':<20}")
        print("-" * 85)

        for payment in payments:
            doctor = payment[5] if payment[5] else 'N/A'
            print(f"{payment[0]:<5} ₹{payment[1]:<8} {payment[2]:<12} {payment[3]:<10} {doctor:<20} {payment[4]:<20}")

    except Exception as e:
        print(f"❌ Error: {e}")