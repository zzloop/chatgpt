import imaplib
import email
from email.header import decode_header
import os
from datetime import date

# 配置
username = "barranquilla_checd@163.com"
password = "BLJYxmb2021"  # 请替换为你的邮箱密码
imap_server = "imap.163.com"
port = 993

# 定义当天日期
today = date.today()
today_str = today.strftime("%d-%b-%Y")

# 连接到IMAP服务器
mail = imaplib.IMAP4_SSL(imap_server, port)
mail.login(username, password)
mail.select("inbox")

# 定义搜索条件（特定发件人、邮件标题和当天日期）
search_criteria = f'(FROM "hj6009@checd.com" SUBJECT "航浚6009轮 * 报表" SINCE "{today_str}")'

# 搜索邮件
status, email_ids = mail.search(None, search_criteria)

if status == "OK":
    for email_id in email_ids[0].split():
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        if status == "OK":
            msg = email.message_from_bytes(msg_data[0][1])
            subject, encoding = decode_header(msg["Subject"])[0]
            subject = subject.decode(encoding) if encoding else subject
            print(f"Subject: {subject}")

            for part in msg.walk():
                if part.get_content_maintype() == "multipart":
                    continue
                if part.get("Content-Disposition") is None:
                    continue

                filename = part.get_filename()
                if filename:
                    # 创建文件夹并保存附件到桌面上的“报表”文件夹
                    desktop_path = os.path.expanduser("~/Desktop")
                    folder_path = os.path.join(desktop_path, "报表")
                    os.makedirs(folder_path, exist_ok=True)
                    file_path = os.path.join(folder_path, filename)

                    with open(file_path, "wb") as attachment_file:
                        attachment_file.write(part.get_payload(decode=True))
                    print(f"Attachment saved: {file_path}")

# 关闭连接
mail.logout()
