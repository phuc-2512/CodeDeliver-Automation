import zipfile
import os

def zip_file(file_to_zip, output_zip):
    """Đóng gói file thành file .zip"""
    if not os.path.isfile(file_to_zip):
        print(f"Lỗi: File {file_to_zip} không tồn tại.")
        return

    with zipfile.ZipFile(output_zip, 'w') as zipf:
        zipf.write(file_to_zip, os.path.basename(file_to_zip))
        print(f"Đã đóng gói {file_to_zip} thành {output_zip}")
