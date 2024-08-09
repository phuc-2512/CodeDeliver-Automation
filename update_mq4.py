# update_mq4.py

def update_mq4_file(file_path, new_id, new_gmail, new_expiration_time):
    """Cập nhật các thông số id, gmail, và thời gian hết hạn trong tệp .mq4"""
    
    # Đọc nội dung tệp .mq4
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Thay thế các thông số
    content = content.replace("input string ID = \"\";", f"input string ID = \"{new_id}\";")
    content = content.replace("input string Gmail = \"\";", f"input string Gmail = \"{new_gmail}\";")
    content = content.replace("input string ExpirationTime = \"\";", f"input string ExpirationTime = \"{new_expiration_time}\";")

    # Ghi lại nội dung vào tệp .mq4
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"Đã cập nhật các thông số trong tệp {file_path} thành công!")
