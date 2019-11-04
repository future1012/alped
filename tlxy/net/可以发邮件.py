from email.mime.text import MIMEText
from email.header import Header
mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1> 这是一封HTML格式邮件</h1>

        </body>
        </html>
        """

msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
from_addr = "532606021@qq.com"
from_pwd = "vbtepcggjsxrbihg"


# 构建邮件接受者信息
#to_addr = "719580406@qq.com"
to_addr = "tengyue1023@163.com"

#MTA服务器地址
smtp_srv = "smtp.qq.com"

msg = MIMEText('快来开会', 'plain', 'utf-8')
msg['From'] = Header("532606021@qq.com", 'utf-8')
msg['To'] = Header("tengyue1023@163.com", 'utf-8')

subject = '公司年会'
msg['Subject'] = Header(subject, 'utf-8')

try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)