# Send a message to a user
from django.core.mail import send_mail
from django.core      import serializers


# Print the message
def preview_message(emailFrom, emailTo, title, body_lines):
    print 'From:',emailFrom
    print '\nTo:',emailTo
    print '\nSubject:',title
    print '\nBody:\n    ','\n    '.join(body_lines)


# Get the title from the message
def get_title(title):
    title = title.replace('* ','')
    title = title.replace(' *','')
    title = title.replace ('-*-muse-*-', '')
    title = title.replace ('-*- muse -*-', '')
    title = title.rstrip()
    return title


# Read the current message
def read_message(path):
    emailFrom = 'mark.b.seaman@gmail.com'
    emailTo   = 'mdseaman.c125c@m.evernote.com'
    message   = open(path).read().split('\n')
    title     = get_title(message[0])
    body      = '\n'.join(message[1:]).replace('**','')
    preview_message(emailFrom, emailTo, title, message[1:])
    return [ emailFrom, emailTo, title, body ]


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
    from sys import argv
    if len(argv)>3:
        path = argv[3]
        emailFrom, emailTo, title, body = read_message(path)
        if send(emailFrom, emailTo, title, body):
            print 'successfully sent message'
        else:
            print 'failed to send message'
    else:
        print 'usage: rs evernote file-path'

    exit(0)
