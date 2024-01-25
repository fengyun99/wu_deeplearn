#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/24 10:07
# @Author   : FengYun
# @File     : ip_change_send_mail.py
# @Software : PyCharm
import requests
import smtplib
from email.mime.text import MIMEText
import os


def get_external_ip():
    ip = requests.get("https://api.ipify.org").text
    return ip


def send_email(new_ip, recipients, sender_email, email_password):
    msg = MIMEText('New IP address of the server is ' + new_ip)
    msg['Subject'] = 'IP address of the server changed'
    msg['From'] = sender_email

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, email_password)

    for recipient in recipients:
        msg['To'] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())

    server.quit()


def check_ip_change():
    current_ip = get_external_ip()
    ip_store_path = '/path/to/ip_store.txt'

    if os.path.isfile(ip_store_path):
        with open(ip_store_path, 'r') as file:
            stored_ip = file.read()
            if current_ip != stored_ip:
                send_email(current_ip, ['recipient1@example.com', 'recipient2@example.com'], 'sender@example.com',
                           'email_password')
                with open(ip_store_path, 'w') as file:
                    file.write(current_ip)
    else:
        with open(ip_store_path, 'w') as file:
            file.write(current_ip)


check_ip_change()
