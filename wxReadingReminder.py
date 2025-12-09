import requests
import urllib3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from email.header import Header

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 加载环境变量
load_dotenv()

# 邮件配置
EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.qq.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'sender_email': os.getenv('SENDER_EMAIL'),
    # pifdgnckwiwddcff
    'sender_password': os.getenv('SENDER_PASSWORD'),
    'receiver_email': os.getenv('RECEIVER_EMAIL')
}

# 信息配置
INFO_CONFIG = {
    'guomai_token': os.getenv('GUOMAI_TOKEN')
}

print(f"从环境变量加载的GUOMAI_TOKEN: {os.getenv('GUOMAI_TOKEN')}")

def send_email(subject, content):
    """发送邮件通知"""
    msg = MIMEMultipart()
    # 关键：正确设置From字段（中文别名+编码处理）
    # 用Header处理中文别名，确保符合RFC2047编码标准
    alias = Header('温馨提醒', 'utf-8').encode()  # 中文别名编码
    sender_email = EMAIL_CONFIG['sender_email']
    msg['From'] = f'{alias} <{sender_email}>'  # 格式：编码后的别名 <实际邮箱>
    # msg['From'] = EMAIL_CONFIG['sender_email']
    msg['To'] = EMAIL_CONFIG['receiver_email']
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'html'))
    print(f"token: {INFO_CONFIG['token']}")
    
    try:
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        print(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.send_message(msg)
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

def sign_in():
    url = "https://mallapi.guomai.cc/user/sign_in"

    headers = {
        "Host": "mallapi.guomai.cc",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541510) XWEB/17071",
        "xweb_xhr": "1",
        "channel": "1",
        "content-type": "application/json",
        "versions": "v5",
        "token": INFO_CONFIG['guomai_token'],
        "accept": "*/*",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://servicewechat.com/wx1c34390acfc8422d/96/page-frame.html",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=1, i"
    }

    try:
        # 添加 verify=False 跳过SSL验证
        response = requests.get(url, headers=headers, verify=False)

        print(f"状态码: {response.status_code}")
        print("响应内容:")
        print(response.text)
        # 邮件内容
        html_content = response.text
        # 发送邮件
        # 设置邮件标题
        subject = f"果麦签到&微信读书挑战提醒"
        send_email(subject, html_content)
        return response

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None


if __name__ == "__main__":
    result = sign_in()
