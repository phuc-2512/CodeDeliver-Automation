import time
import os
from zip_util import zip_file
from email_util import send_email_with_attachment

if __name__ == "__main__":
    # Đường dẫn tới file bạn muốn đóng gói
    file_to_zip = "C:\\Users\\phanv\\AppData\\Roaming\\MetaQuotes\\Terminal\\C142B020C05FAD9EEC4BE1375F709241\\MQL4\\Experts\\a.mq4"
    # Đường dẫn tới file .zip sẽ được tạo
    output_zip = "C:\\Users\\phanv\\OneDrive\\Desktop\\ab.zip"
    # Địa chỉ email người nhận
    to_email = "phanvanphuc25122008@gmail.com"
    # Tiêu đề email
    subject = "File EX4 đã được đóng gói"
    # Nội dung email
    body = "Vui lòng kiểm tra file đính kèm."

    # Đóng gói file
    zip_file(file_to_zip, output_zip)
    
    # delay 5s
    time.sleep(5)

    # Gửi email với file .zip đính kèm
    send_email_with_attachment(to_email, subject, body, output_zip)