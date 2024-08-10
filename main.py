import time
import os
from signal_bot import check_signal
from data_fetcher import fetch_latest_data
from update_mq4 import update_mq4_file
from create_mq4 import create_mq4_file
from zip_util import zip_file
from email_util import send_email_with_attachment
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')


def run_process():
    progress = 0
    update_progress(progress)
    
    # Chạy bot kiểm tra tín hiệu từ server
    check_signal()
    progress += 20
    update_progress(progress)
    
    fetch_latest_data()
    progress += 20
    update_progress(progress)
    
     # Tên bot và đường dẫn tệp .mq4
    bot_name = "MyBot"
    mq4_file_path = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    
    # Tạo tệp .mq4 với các giá trị mặc định
    create_mq4_file(mq4_file_path, bot_name)
    progress += 20
    update_progress(progress)

    # Cập nhật tệp .mq4 với các thông số mới
    update_mq4_file(mq4_file_path)
    progress += 20
    update_progress(progress)

    # Đường dẫn tới file bạn muốn đóng gói
    file_to_zip = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    
    # Đường dẫn tới file .zip sẽ được tạo
    output_zip = r"C:\Users\phanv\OneDrive\Đính kèm\b.zip"

    # Đóng gói file
    zip_file(file_to_zip, output_zip)
    
    # Kiểm tra file zip đã được tạo
    if os.path.exists(output_zip):
        print(f"File zip đã được tạo thành công tại {output_zip}")
    else:
        print("Lỗi: File zip chưa được tạo.")
        return
    
    progress += 10
    update_progress(progress)
    
    # delay 5s
    time.sleep(5)

    # Gửi email với file zip đính kèm và bắt lỗi nếu có
    try:
        send_email_with_attachment(output_zip)
        progress = 100
        update_progress(progress)
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

def update_progress(progress):
    with open('progress.json', 'w') as f:
        json.dump({'progress': progress}, f)

if __name__ == "__main__":
    run_process()