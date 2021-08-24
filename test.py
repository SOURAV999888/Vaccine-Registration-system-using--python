import smtplib

gmail_user = 'gsaha123098@gmail.com'
gmail_password = 'gsaha123098/z.x'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(f'gsaha123098@gmail.com','saha93942@gmail.com','fffffffffffffffffffffffffffffff\ngggggggggggggggggggggg')
except Exception as e:
    print('Something went wrong...')
    print(e)