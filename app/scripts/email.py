from django.core.mail import send_mail
from sys import stdin,argv


# Send email
def send_email_message (emailFrom, emailTo, title, body):
    try:
        send_mail(title, body, emailFrom, emailTo.split(","), fail_silently=False)
        print 'successfully sent message'
    except Exception as exc:
        print("Email sending failed: %s" % str(exc))
        print 'failed to send message'


# Run the main job
def run():

    to = 'mark.b.seaman@gmail.com'
    if len(argv)>3:
        to = argv[3]
        print('TO: '+to)

    subject = 'Message from Mark'
    if len(argv)>4:
        subject = argv[4]
        print('SUBJECT: '+subject)

    text = stdin.read()
    print('mark.b.seaman@gmail.com', to, subject, '%d characters'%len(text))
    send_email_message('mark.b.seaman@gmail.com', to, subject, text)
 
    exit(0)