# Send a message to a user
from django.core.mail import send_mail
from django.core      import serializers


# Print the message
def preview_message(m):
    print 'From:',m[0]
    print '\nTo:',m[1]
    print '\nSubject:',m[2]
    print '\nBody:\n    ','\n    '.join(m[3:])


# Read the current message
def read_message():
    print 'sent message'
    f = '/home/seaman/Projects/thumper/app/data/send_message'
    m = open(f).read().split('\n')
    preview_message(m)
    return m


# Send email
def send(message):
    try:
        text = '\n'.join(message[3:])
        to =   message[1].split(",")
        send_mail(message[2], text, message[0], to, fail_silently=False)
        return True
    except Exception as exc:
        print("Email sending failed: %s" % str(exc))
        return False


# Run the main job
def run():
    if send(read_message()):
        print 'successfully sent message'
    else:
        print 'failed to send message'
