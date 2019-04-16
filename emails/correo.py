__author__ = 'srv'

import smtplib
import datetime
import locale
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

username = 'uveventrue@gmail.com'  # Email Address from the email you want to send an email
password = 'h0latr1p'  # Password
server = smtplib.SMTP('')
from_addr = username
p_nombre = "Juan pardo amargo"
p_factura = "80629.pdf"

locale.setlocale(locale.LC_ALL, '')
mydate = datetime.datetime.now()

print(mydate.strftime('%B'))



"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

# Create the body of the message (a HTML version for formatting).
html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="1671.4">
  <style type="text/css">
    p.p1 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 14.7px Calibri; color: #453ccc; -webkit-text-stroke: #453ccc}}
    p.p2 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #453ccc; -webkit-text-stroke: #453ccc; min-height: 14.0px}}
    p.p3 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #453ccc; -webkit-text-stroke: #453ccc}}
    p.p4 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.7px Arial; color: #453ccc; -webkit-text-stroke: #453ccc}}
    p.p5 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 9.0px Helvetica; color: #3170b9; -webkit-text-stroke: #3170b9}}
    span.s1 {{font-kerning: none}}
    span.s2 {{font: 12.8px Helvetica; font-kerning: none; color: #0b5ab2; -webkit-text-stroke: 0px #0b5ab2}}
    span.s3 {{font: 9.0px Helvetica; text-decoration: underline ; font-kerning: none; color: #3586ff; -webkit-text-stroke: 0px #3586ff}}
  </style>
</head>
<body bgcolor="white">
<p class="p1"><span class="s1">Buenas {nombre},</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">Adjuntamos factura mensual.</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">Un saludo.</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p3"><span class="s1">--<span class="Apple-converted-space"> </span></span></p>
<p class="p4"><span class="s1"><b>PROREYMON, S.L</b>.</span></p>
<p><img src="cid:image1"></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p4"><span class="s1">C.I.F. B78561099</span></p>
<p class="p4"><span class="s1">C/. Moreras núm. 48 - bajo</span></p>
<p class="p4"><span class="s1">28300 - ARANJUEZ (Madrid)</span></p>
<p class="p5"><span class="s2"><i>     </i></span><span class="s1"><i>Este mensaje y sus archivos adjuntos son confidenciales y únicamente podrán ser usados por la persona o entidad a la que van dirigidos. Este mensaje puede contener información confidencial o legalmente protegida. No hay renuncia a la confidencialidad o secreto profesional por cualquier transmisión defectuosa o errónea. Si usted ha recibido este mensaje por error, notifíquelo inmediatamente al remitente.</i></span></p>
<p class="p5"><span class="s1"><i>     Le informamos que sus datos personales son tratados por PROREYMON S.L con la finalidad de gestionar y mantener las relaciones profesionales que nos unen con Usted.</i></span></p>
<p class="p5"><span class="s1"><i>Sus datos podrán ser cedidos a las entidades y administraciones públicas necesarias para la realización de dicha gestión. Este tratamiento de datos es necesario para mantener dicha relación profesional. Los datos se eliminarán cuando finalicen los plazos de prescripción marcados por la ley, conservándose únicamente para atender posibles reclamaciones. Usted puede ejercer sus derechos de acceso, rectificación, cancelación, oposición, portabilidad y limitación del tratamiento de sus datos dirigiéndose a PROREYMON S.L, C/ de las Moreras 48 bj 28300 Aranjuez (Madrid) o a </i><a href="mailto:proreymon@gmail.com"><span class="s3"><i>proreymon@gmail.com</i></span></a><i>, acompañando copia de su DNI acreditando debidamente su identidad. En cualquier situación, Usted tiene derecho a presentar una reclamación ante la Agencia Española de Protección de Datos (AEPD).</i></span></p>
</body>
</html>
""".format(nombre=p_nombre.partition(' ')[0])


# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg, p_factura, p_nombre):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

# Read email list txt
email_list = [line.strip() for line in open('email.txt')]

for to_addrs in email_list:
    msg = MIMEMultipart()

    msg['Subject'] = "Factura mensual " +  mydate.strftime('%B')
    msg['From'] = from_addr
    msg['To'] = to_addrs
    


    # Attach HTML to the email
    body = MIMEText(html, 'html')
    msg.attach(body)

    
    # Attach Cover Letter to the email
    cover_letter = MIMEApplication(open(p_factura, "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename=p_factura)
    msg.attach(cover_letter)

    # This example assumes the image is in the current directory
    fp = open('unnamed.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    try:
        send_mail(username, password, from_addr, to_addrs, msg, p_factura, p_nombre)
        print ("Email successfully sent to", to_addrs)
    except SMTPAuthenticationError:
        print ('SMTPAuthenticationError')
        print ("Email not sent to", to_addrs)
