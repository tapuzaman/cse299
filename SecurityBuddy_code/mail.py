import smtplib


def notify(x,y):
    gmail_user = 'sbuddy00723@gmail.com'
    gmail_password = 'Greenapple9'

    sent_from = gmail_user
    to = ['smashfu@gmail.com', 'bill@gmail.com']
    subject = 'Notification'
    body = "\nPeople entered building: " + str(x) + "\nPeople exited building: " + str(y)

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
