import time
import psycopg2
from datetime import date
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from email.utils import make_msgid
import mimetypes

from django.template import Template, Context
from django.conf import settings

import os
import django

from datetime import datetime

def send_third(to):

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ERATO.settings')
    django.setup()
    print("Sending email...")
    print("Rendering template")

    html = render_to_string(template_name='emails/third_email.html',context={ 'username': "An user " })
    subject, from_email= 'Security mail', 'eratoservices@gmail.com'
    html_part = MIMEMultipart(_subtype='related')

    print("Adding MIME")
    body = MIMEText(html, _subtype='html')
    html_part.attach(body)

    fp = open('assets/images/logo/ERATO.jpg', 'rb')
    msgLogo = MIMEImage(fp.read())
    fp.close()
    msgLogo.add_header('Content-ID', '<logo_erato>')

    msg = EmailMessage(subject, None, from_email, [to])
    msg.attach(html_part)
    msg.attach(msgLogo)

    print("Message created")
    print("Sending email to %s" % to)
    msg.send()
    print("Message sent")

while(True):
  try:
      connection = psycopg2.connect(user = "django",
                                    password = "django",
                                    host = "localhost",
                                    port = "5432",
                                    database = "erato")

      cursor = connection.cursor()

      print("Succesful connection")
      # Print PostgreSQL Connection properties
      print ( connection.get_dsn_parameters(),"\n")

      while(True):

        # Third_email, did, sid
        # Email de tercedo, id del date e id del sex_worker

        # 2019 - 08 - 07 02:00:00-05
        now = datetime.now()

        print("now =", now)
        # dd/mm/YY H:M:S
        time_now = str(now.strftime("\'%Y-%m-%d %H:%M:%S-00\'"))
        print("date and time =", time_now)

        #query = "SELECT third_email, did, sid FROM app_sw_sw RIGHT JOIN (SELECT app_date_date.id AS did, sw_id AS sid FROM app_date_date INNER JOIN app_sw_service ON app_sw_service.id=app_date_date.service_id WHERE state='requested' ) AS seses ON app_sw_sw.user_id = seses.sid;"
        query = "SELECT third_email, did, sid FROM app_sw_sw RIGHT JOIN (SELECT app_date_date.id AS did, sw_id AS sid FROM app_date_date INNER JOIN app_sw_service ON app_sw_service.id=app_date_date.service_id WHERE state='started' AND end_time < %s ) AS seses ON app_sw_sw.user_id = seses.sid;" % (time_now)
        cursor.execute(query)
        print("Query executed.")

        mobile_records = cursor.fetchall()

        for row in mobile_records:
          send_third(row[0])
          query = "UPDATE app_date_date SET state='timed out' WHERE id=%s" % row[1]
          cursor.execute(query)
        time.sleep(10)


  except (Exception, psycopg2.Error) as error :
      print ("Error while connecting to PostgreSQL", error)
      time.sleep(3)
  finally:
      #closing database connection.
          if(connection):
              cursor.close()
              connection.close()
              print("PostgreSQL connection is closed")
