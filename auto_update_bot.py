from data_fetcher import fetch_latest_data
from update_mq4 import update_mq4_file
import json

def auto_update_bot(mq4_file_path):
    """
    Bot tự động cập nhật thông tin ID và ngày hết hạn từ data_fetcher vào tệp MQ4.
    """
    print("AutoUpdateBot đang chạy...")

    # Lấy dữ liệu mới nhất
    try:
        with open("latest_data.json", "r", encoding="utf-8") as f:
            latest_data = json.load(f)
            latest_key = list(latest_data.keys())[-1]
            latest_entry = latest_data[latest_key]

        new_id = latest_entry.get('accountId', '')
        new_expiration_time = latest_entry.get('expiryDate', '')

        if not new_id or not new_expiration_time:
            print("Không tìm thấy ID hoặc ngày hết hạn hợp lệ.")
            return

        # Cập nhật tệp MQ4
        update_mq4_file(mq4_file_path, new_id, new_expiration_time)
        print(f"Đã cập nhật tệp MQ4 với ID: {new_id} và ngày hết hạn: {new_expiration_time}")

    except FileNotFoundError:
        print("Không tìm thấy tệp dữ liệu mới nhất.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc dữ liệu từ tệp JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")

