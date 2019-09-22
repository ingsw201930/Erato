import psycopg2
from datetime import date
from app_emails.utils import send_qr
from app_date.QR import generateQR

try:
    connection = psycopg2.connect(user = "django",
                                  password = "eratoerato",
                                  host = "localhost",
                                  port = "5432",
                                  database = "erato")

    cursor = connection.cursor()

    print("Succesful connection")
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    today = date.today()
    print("Today's date:", today)

    query = 'SELECT * FROM app_date_date WHERE state="started" AND end >=  today'
    cursor.execute(query)

    mobile_records = cursor.fetchall()

    for row in mobile_records:
       query_2 = 'SELECT third_email FROM app_sw_sw WHERE id=% ' % (row[5])
       cursor.execute(query_2)
       qr = generateQR(cursor.fetchall()[0])
       send_qr(qr, row[0])

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
