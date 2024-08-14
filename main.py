import time
import os
import json
import logging
from signal_bot import check_signal
from data_fetcher import fetch_latest_data
from update_mq4 import update_mq4_file
from create_mq4 import create_mq4_file
from zip_util import zip_file
from email_util import send_email_with_attachment
import sys

sys.stdout.reconfigure(encoding='utf-8')

def setup_logging():
    # Tạo một formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Thiết lập file handler
    file_handler = logging.FileHandler('app.log', encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Thiết lập console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Lấy root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Thêm cả hai handlers vào logger
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

# Gọi hàm này ở đầu script của bạn
setup_logging()


def run_process():
    try:
        progress = 0
        update_progress(progress)
        logging.info("Bắt đầu quá trình xử lý")
    
    # Chạy bot kiểm tra tín hiệu từ server
        check_signal()
        progress += 20
        update_progress(progress)
        logging.info("Đã kiểm tra tín hiệu từ server")
    
        fetch_latest_data()
        progress += 20
        update_progress(progress)
        logging.info("Đã lấy dữ liệu mới nhất")
    
     # Tên bot và đường dẫn tệp .mq4
        bot_name = "MyBot"
        mq4_file_path = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    
    # Tạo tệp .mq4 với các giá trị mặc định
        create_mq4_file(mq4_file_path, bot_name)
        progress += 20
        update_progress(progress)
        logging.info(f"Đã tạo tệp MQ4: {mq4_file_path}")

    # Cập nhật tệp .mq4 với các thông số mới
        update_mq4_file(mq4_file_path)
        progress += 20
        update_progress(progress)
        logging.info("Đã cập nhật tệp MQ4 với thông số mới")

    # Đường dẫn tới file bạn muốn đóng gói
        file_to_zip = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.ex4"
    
    # Đường dẫn tới file .zip sẽ được tạo
        output_zip = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.zip"

    # Đóng gói file
        zip_file(file_to_zip, output_zip)
    
    # Kiểm tra file zip đã được tạo
        if os.path.exists(output_zip):
            logging.info(f"File zip đã được tạo thành công tại {output_zip}")
        else:
            logging.error("Lỗi: File zip chưa được tạo.")
            return
    
        progress += 10
        update_progress(progress)
    
    # delay 5s
        time.sleep(5)

    # Gửi email với file zip đính kèm
        send_email_with_attachment(output_zip)
        progress = 100
        update_progress(progress)
        logging.info("Đã gửi email với file đính kèm")

    except Exception as e:
        logging.error(f"Lỗi trong quá trình xử lý: {str(e)}")
        update_progress(-1)  # Sử dụng -1 để chỉ ra lỗi

def update_progress(progress):
    with open('progress.json', 'w') as f:
        json.dump({'progress': progress}, f)

if __name__ == "__main__":
    run_process()