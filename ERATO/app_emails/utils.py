from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from email.utils import make_msgid
import mimetypes

def send_qr(qr, to):

    html = render_to_string(template_name='emails/QR_code.html',context={ 'qr': qr })
    subject, from_email= 'QR code', 'eratoservices@gmail.com'

    html_part = MIMEMultipart(_subtype='related')

    body = MIMEText(html, _subtype='html')
    html_part.attach(body)

    # This example assumes the image is in the current directory
    fp = open(qr, 'rb')
    msgImage = MIMEImage(fp.read(), _subtype="png")
    fp.close()

    """
    fp = open('assets/images/logo/ERATO.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<logo_erato>')

    msg = EmailMessage(subject, None, from_email, [to])
    msg.attach(html_part)
    msg.attach(msgImage)
    """

    msgImage.add_header('Content-ID', '<image1>')
    html_part.attach(msgImage)

    msg = EmailMessage(subject, html, from_email, [to])
    msg.attach_file(qr)
    msg.send()

def send_third(username, to):
    html = render_to_string(template_name='emails/third.html',context={ 'username': username })
    subject, from_email= 'Security mail', 'eratoservices@gmail.com'

    html_part = MIMEMultipart(_subtype='related')

    body = MIMEText(html, _subtype='html')
    html_part.attach(body)

    msg = EmailMessage(subject, None, from_email, [to])
    msg.attach(html_part)
    msg.send()
