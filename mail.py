import imaplib

# 配置
username = "lispzhen@163.com"
password = "7979248839"  # 请替换为你的邮箱密码
imap_server = "imap.163.com"
port = 993

# 连接到IMAP服务器
mail = imaplib.IMAP4_SSL(imap_server, port)

# 尝试登录
try:
    mail.login(username, password)
    print("Login successful")
except imaplib.IMAP4.error as e:
    print(f"Login failed: {e}")

# 列出邮箱
status, mailbox_list = mail.list()
if status == "OK":
    print("Mailboxes:")
    for mailbox in mailbox_list:
        print(mailbox.decode("utf-8"))

# 关闭连接
mail.logout()
