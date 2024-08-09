import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')


def send_email_with_attachment(to_email, subject, body, attachment_path):
    """Gửi email với file đính kèm"""
    from_email = "phanvanphuc251220082@gmail.com"
    password = "dkvv ykyh fmvz ymtb"

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
        # Đảm bảo rằng tên file được mã hóa đúng cách
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