from django.core.mail import send_mail


# Send email
def send(emailFrom, emailTo, title, body):
    try:
        send_mail(title, body, emailFrom, emailTo.split(","), fail_silently=False)
        return True
    except Exception as exc:
        print("Email sending failed: %s" % str(exc))
        return False


# Run the main job
def run():
    if send('mark.b.seaman@gmail.com', 'mark.b.seaman@gmail.com', 'Test message', 'Life is short; live well'):
        print 'successfully sent message'
    else:
        print 'failed to send message'
 
