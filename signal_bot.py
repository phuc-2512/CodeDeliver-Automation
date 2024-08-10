import firebase_admin
from firebase_admin import credentials, db
import time
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Đường dẫn đến tệp JSON key bạn đã tải từ Firebase
cred = credentials.Certificate(r"C:\Users\phanv\OneDrive\Tài liệu\firebase-adminsdk.json")

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python1-39843-default-rtdb.firebaseio.com'
})

# Biến toàn cục để lưu trữ dữ liệu mới nhất
latest_data = None

# Hàm để kiểm tra tín hiệu từ server
def check_signal():
    global latest_data
    ref = db.reference('payments/')
    snapshot = ref.get()
    if snapshot:
        print("Dữ liệu hiện tại:")
        latest_data = snapshot
        # Ghi dữ liệu vào tệp để chia sẻ với các bot khác
        with open("latest_data.json", "w", encoding="utf-8") as f:
            json.dump(latest_data, f, ensure_ascii=False, indent=4)
        for key, value in snapshot.items():
            email = value.get('email', 'N/A')
            payment_date = value.get('paymentDate', 'N/A')
            expiry_date = value.get('expiryDate', 'N/A')
            account_id = value.get('accountId', 'N/A')
            print(f"Email: {email}, Payment Date: {payment_date}, Expiry Date: {expiry_date}, Account ID: {account_id}")
    else:
        print("Không có dữ liệu hiện tại")
