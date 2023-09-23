import imaplib
import email
from email.header import decode_header
import os
from datetime import date, timedelta

# 配置
username = "lispzhen@163.com"
password = "7979248839"  # 请替换为你的邮箱密码
imap_server = "imap.163.com"
port = 993

# 计算前一天的日期
yesterday = date.today() - timedelta(days=1)
yesterday_str = yesterday.strftime("%d-%b-%Y")  # 不再需要编码为UTF-8

# 连接到IMAP服务器
mail = imaplib.IMAP4_SSL(imap_server, port)
mail.login(username, password)

# 网易邮箱的特点，强制ID语句
imaplib.Commands["ID"] = "NONAUTH"
mail._simple_command("ID", '("name" "test" "version" "0.0.1")')

# 选择邮箱
mail.select("inbox")

# 定义搜索条件（特定发件人、邮件标题和前一天日期），不再需要编码为UTF-8
from_email = "\"hj6009@checd.com\""
subject_criteria = "\"航浚6009轮 * 报表\""

# 构建搜索条件，使用SENTON来指定日期
search_criteria = f'(FROM {from_email} SUBJECT {subject_criteria} SENTON "{yesterday_str}")'

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
