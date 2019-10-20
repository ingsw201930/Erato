from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from email.utils import make_msgid
import mimetypes

def send_third(to):

    print("Sending security email to "+to)
    html = render_to_string(template_name='emails/third_email.html',context={})
    subject, from_email= 'Security email', 'eratoservices@gmail.com'

    html_part = MIMEMultipart(_subtype='related')

    body = MIMEText(html, _subtype='html')
    html_part.attach(body)

    fp = open('assets/images/logo/ERATO.jpg', 'rb')
    msgLogo = MIMEImage(fp.read())
    fp.close()
    msgLogo.add_header('Content-ID', '<logo_erato>')

    msg = EmailMessage(subject, None, from_email, [to])
    msg.attach(msgLogo)
    msg.attach(html_part)
    msg.attach(msgImage)
    msg.send()

def send_qr(qr, to):

    print("Sending qr to "+to)
    print("QR saved in "+qr)
    html = render_to_string(template_name='emails/qr_code.html',context={})
    subject, from_email= 'QR code', 'eratoservices@gmail.com'

    html_part = MIMEMultipart(_subtype='related')

    body = MIMEText(html, _subtype='html')
    html_part.attach(body)

    # This example assumes the image is in the current directory
    fp = open(qr, 'rb')
    msgImage = MIMEImage(fp.read(), _subtype="png")
    fp.close()

    fp = open('assets/images/logo/ERATO.jpg', 'rb')
    msgLogo = MIMEImage(fp.read())
    fp.close()
    msgLogo.add_header('Content-ID', '<logo_erato>')

    msgImage.add_header('Content-ID', '<qr_code>')
    html_part.attach(msgImage)

    msg = EmailMessage(subject, None, from_email, [to])
    msg.attach(msgLogo)
    msg.attach(html_part)
    msg.attach(msgImage)
    msg.send()
