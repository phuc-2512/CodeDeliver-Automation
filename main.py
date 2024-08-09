import time
import os
from create_mq4 import create_mq4_file
from zip_util import zip_file
from email_util import send_email_with_attachment
import sys
sys.stdout.reconfigure(encoding='utf-8')


if __name__ == "__main__":
    # Tên bot và đường dẫn tệp .mq4
    bot_name = "MyBot"
    mq4_file_path = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"

     # Các thông số cho bot
    bot_id = "123456"
    gmail = "example@gmail.com"
    expiration_time = "2024-12-31"

    # Tạo tệp .mq4 với các thông số id, gmail, và thời gian hết hạn
    create_mq4_file(mq4_file_path, bot_name, bot_id, gmail, expiration_time)
    
    # Đường dẫn tới file bạn muốn đóng gói
    file_to_zip = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    
    # Đường dẫn tới file .zip sẽ được tạo
    output_zip = r"C:\Users\phanv\OneDrive\Đính kèm\b.zip"
    
    # Địa chỉ email người nhận
    to_email = "phanvanphuc25122008@gmail.com"
    
    # Tiêu đề email
    subject = "File EX4 đã được đóng gói"
    
    # Nội dung email
    body = "Vui lòng kiểm tra file đính kèm."

    # Đóng gói file
    zip_file(file_to_zip, output_zip)
    
    # Kiểm tra file zip đã được tạo
    if os.path.exists(output_zip):
        print(f"File zip đã được tạo thành công tại {output_zip}")
    else:
        print("Lỗi: File zip chưa được tạo.")
        exit(1)
    
    # delay 5s
    time.sleep(5)

    # Gửi email với file zip đính kèm và bắt lỗi nếu có
    try:
        send_email_with_attachment(to_email, subject, body, output_zip)
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")