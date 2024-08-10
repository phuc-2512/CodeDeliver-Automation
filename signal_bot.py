import firebase_admin
from firebase_admin import credentials, db
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Đường dẫn đến tệp JSON key bạn đã tải từ Firebase
cred = credentials.Certificate(r"C:\Users\phanv\OneDrive\Tài liệu\firebase-adminsdk.json")

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python1-39843-default-rtdb.firebaseio.com'
})

# Hàm để kiểm tra tín hiệu từ server
def check_signal():
    ref = db.reference('payments/')
    snapshot = ref.get()
    if snapshot:
        print("Dữ liệu hiện tại:")
        for key, value in snapshot.items():
            email = value.get('email', 'N/A')
            payment_date = value.get('paymentDate', 'N/A')
            expiry_date = value.get('expiryDate', 'N/A')
            account_id = value.get('accountId', 'N/A')
            print(f"Email: {email}, Payment Date: {payment_date}, Expiry Date: {expiry_date}, Account ID: {account_id}")
    else:
        print("Không có dữ liệu hiện tại")

# Hàm để liên tục kiểm tra mỗi giây
def run_bot():
    print("Đang chạy bot để kiểm tra tín hiệu từ server...")
    last_snapshot = None
    while True:
        current_snapshot = db.reference('payments/').get()
        if current_snapshot != last_snapshot:
            print("Phát hiện thay đổi!")
            check_signal()
            last_snapshot = current_snapshot
        else:
            print("Không có thay đổi")
        time.sleep(1)  # Chờ 1 giây trước khi kiểm tra lại

