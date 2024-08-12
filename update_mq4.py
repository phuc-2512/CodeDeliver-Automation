import json
from data_fetcher import fetch_latest_data
import sys
import subprocess
import os
import logging
import chardet


# Thiết lập logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

sys.stdout.reconfigure(encoding='utf-8')

def update_mq4_file(file_path):
    """Cập nhật các thông số id và thời gian hết hạn trong tệp .mq4 từ dữ liệu mới nhất"""
    
    if not os.path.exists(file_path):
        logging.error(f"Lỗi: File MQ4 không tồn tại tại đường dẫn: {file_path}")
        return

    # Lấy dữ liệu mới nhất từ data_fetcher
    latest_data = fetch_latest_data()
    
    if latest_data:
        logging.info("Đã nhận được dữ liệu từ data_fetcher.")
        new_id = latest_data.get('accountId', '')
        new_expiration_time = latest_data.get('expiryDate', '')
        
        # Đọc nội dung tệp .mq4
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Thay thế các thông số ID và ExpirationTime
            content = content.replace('input string ID = "";', f'input string ID = "{new_id}";')
            content = content.replace('input string ExpirationTime = "";', f'input string ExpirationTime = "{new_expiration_time}";')

            # Ghi lại nội dung vào tệp .mq4
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            
            logging.info(f"Đã cập nhật các thông số ID ({new_id}) và ExpirationTime ({new_expiration_time}) trong tệp {file_path} thành công!")
        except IOError as e:
            logging.error(f"Lỗi khi đọc/ghi file MQ4: {str(e)}")
            return
        
        # Biên dịch file MQ4
        compile_mq4(file_path)
    else:
        logging.warning("Không thể cập nhật tệp .mq4 do không có dữ liệu mới.")

def compile_mq4(file_path):
    """Biên dịch file MQ4 sử dụng MetaEditor từ dòng lệnh"""
    try:
        # Tìm đường dẫn MetaEditor
        metaeditor_paths = [
            r"C:\Program Files\MetaTrader 4\metaeditor.exe",
            r"C:\Program Files (x86)\IG MetaTrader 4 Terminal\metaeditor.exe"
        ]
        metaeditor_path = next((path for path in metaeditor_paths if os.path.exists(path)), None)
        
        if not metaeditor_path:
            logging.error("Lỗi: Không tìm thấy MetaEditor. Vui lòng cung cấp đường dẫn chính xác.")
            return

        logging.info(f"Đang sử dụng MetaEditor tại: {metaeditor_path}")

        # Sử dụng subprocess.list2cmdline để xử lý đúng các ký tự đặc biệt trong đường dẫn
        compile_command = subprocess.list2cmdline([metaeditor_path, f"/compile:{file_path}", "/log"])
        logging.debug(f"Lệnh biên dịch: {compile_command}")
        
        # Sử dụng subprocess.run với encoding='utf-8' và errors='replace'
        result = subprocess.run(compile_command, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')

        if result.returncode == 0:
            logging.info(f"Đã biên dịch thành công file {file_path}")
            logging.debug("Output: " + result.stdout)
        else:
            logging.error(f"Lỗi khi biên dịch file {file_path}")
            logging.error("Error: " + result.stderr)
            
        # Kiểm tra file log của MetaEditor
        log_file = os.path.splitext(file_path)[0] + '.log'
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r', encoding='utf-16', errors='replace') as f:
                    log_content = f.read()
                logging.debug(f"Nội dung file log MetaEditor:\n{log_content}")
            except Exception as e:
                logging.error(f"Không thể đọc file log: {str(e)}")
        else:
            logging.warning(f"Không tìm thấy file log tại {log_file}")

    except Exception as e:
        logging.exception(f"Lỗi không mong đợi khi biên dịch file MQ4: {str(e)}")

if __name__ == "__main__":
    # Sử dụng đường dẫn tuyệt đối
    mq4_file_path = r"C:\Users\phanv\OneDrive\Đính kèm\MyBot.mq4"
    if os.path.exists(mq4_file_path):
        update_mq4_file(mq4_file_path)
    else:
        logging.error(f"Lỗi: Không tìm thấy file MQ4 tại đường dẫn: {mq4_file_path}")