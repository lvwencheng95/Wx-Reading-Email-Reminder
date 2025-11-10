# Wx-Reding-Email-Reminder
微信读书邮件提醒

参加365阅读挑战，容易某天太忙没读书，由于某一两天没读，导致挑战失败，太可惜了。设置邮件提醒，每天晚上21:30进行阅读提醒（当前还不知道如何获取当前阅读时长，现在就是固定的每天某一时刻发送邮件进行提醒）

# 使用说明
## 1、fork项目

## 2、配置信息
### （1）打开fork项目，选择setting
<img width="1719" height="807" alt="image" src="https://github.com/user-attachments/assets/730278e7-56c1-4021-a475-c9e2320f55c3" />

### （2）添加3个变量值，发送邮件邮箱、发送邮箱授权码和接收邮件邮箱
<img width="1701" height="845" alt="image" src="https://github.com/user-attachments/assets/ec7ba1f6-925e-4a66-9545-c055988110df" />


## 3、执行项目中Action，即可收到邮箱提醒

<img width="1717" height="763" alt="image" src="https://github.com/user-attachments/assets/1700cfcc-04c7-4d50-85ba-d0c12939a648" />

<img width="1736" height="744" alt="image" src="https://github.com/user-attachments/assets/6e36eed4-4d57-4f74-ab62-cddcc633d8b9" />


# 注意事项
## 1、邮箱授权码的获取
QQ 邮箱默认关闭第三方客户端的 SMTP 权限，需手动开启并使用授权码（而非登录密码）验证，步骤如下：
（1）登录 QQ 邮箱网页版（mail.qq.com）；
（2）点击右上角【设置】→【账户】；
（3）下拉找到 “POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务”，开启【SMTP 服务】；
（4）按提示验证（如短信验证），生成授权码（16 位字符串，需保存，用于替代密码）。

## 每日发送邮件的时间设置
<img width="1881" height="878" alt="image" src="https://github.com/user-attachments/assets/a415b961-d8af-4a4d-97aa-fb46f7639a2c" />
在main.yml中的cron进行时间的设置。

