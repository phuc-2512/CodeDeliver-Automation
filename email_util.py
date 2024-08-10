import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

def get_latest_data():
    try:
        with open("latest_data.json", "r", encoding="utf-8") as f:
            latest_data = json.load(f)
            latest_key = list(latest_data.keys())[-1]
            return latest_data[latest_key]
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to read latest data.")
        return None

def send_email_with_attachment(attachment_path):
    """Gửi email với file đính kèm"""
    latest_data = get_latest_data()
    if not latest_data:
        return

    to_email = latest_data.get('email')
    account_id = latest_data.get('accountId', 'N/A')
    expiry_date = latest_data.get('expiryDate', 'N/A')

    from_email = "phanvanphuc251220082@gmail.com"
    password = "dkvv ykyh fmvz ymtb"

    subject = "Vui lòng check lại gmail để nhận sản phẩm"
    body = f"""
    Xin chào,

    Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi. Dưới đây là thông tin về tài khoản của bạn:

    ID tài khoản: {account_id}
    Ngày hết hạn bot MQL4: {expiry_date}

    Vui lòng kiểm tra file đính kèm để nhận sản phẩm của bạn.

    Trân trọng,
    Đội ngũ hỗ trợ
    """

    # Tạo đối tượng MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Thêm phần nội dung vào email với UTF-8 encoding
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Mở file đính kèm và thêm vào email
    if not os.path.isfile(attachment_path):
        print(f"Lỗi: File đính kèm {attachment_path} không tồn tại.")
        return

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        filename = os.path.basename(attachment_path).encode('utf-8')
        part.add_header('Content-Disposition', f'attachment; filename="{filename.decode("utf-8")}"')
        msg.attach(part)

    # Kết nối với Gmail SMTP server và gửi email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string().encode('utf-8')
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Đã gửi email đến {to_email} với file đính kèm {os.path.basename(attachment_path)}")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

if __name__ == "__main__":
    attachment_path = r"C:\Users\phanv\OneDrive\Đính kèm\b.zip"  # Update this path as needed
    send_email_with_attachment(attachment_path)