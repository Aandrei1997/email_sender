import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Calinescu'
email['to'] = 'andrei.calinescu97@yahoo.com'
email['subject'] = 'You won 1 000 000 dollars!'

email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('defaultforfun1234@gmail.com', 'Andrew1234$$')
  smtp.send_message(email)
  print('Email sent')
