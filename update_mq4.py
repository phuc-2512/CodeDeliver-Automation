import json
from data_fetcher import fetch_latest_data
import sys

sys.stdout.reconfigure(encoding='utf-8')

def update_mq4_file(file_path):
    """Cập nhật các thông số id và thời gian hết hạn trong tệp .mq4 từ dữ liệu mới nhất"""
    
    # Lấy dữ liệu mới nhất từ data_fetcher
    latest_data = fetch_latest_data()
    
    if latest_data:
        print("Đã nhận được dữ liệu từ data_fetcher.")  # Thêm dòng log mới
        new_id = latest_data.get('accountId', '')
        new_expiration_time = latest_data.get('expiryDate', '')
        
        # Đọc nội dung tệp .mq4
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Thay thế các thông số ID và ExpirationTime
        content = content.replace('input string ID = "";', f'input string ID = "{new_id}";')
        content = content.replace('input string ExpirationTime = "";', f'input string ExpirationTime = "{new_expiration_time}";')

        # Ghi lại nội dung vào tệp .mq4
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"Đã cập nhật các thông số ID ({new_id}) và ExpirationTime ({new_expiration_time}) trong tệp {file_path} thành công!")
    else:
        print("Không thể cập nhật tệp .mq4 do không có dữ liệu mới.")

if __name__ == "__main__":
    mq4_file_path = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    update_mq4_file(mq4_file_path)