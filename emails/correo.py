#!/usr/bin/env python

"""correo.py: manda correos electronicos pidiendo el password por 
consola tomando la informacion de un dataframe Pandas, además el 
cuerpo del correo ha sido
confeccionado para una PYME."""

__author__ = 'Victor Sanchez Alonso'
__email__ = "victorsoyvicto@gmail.com"

import smtplib
import datetime
import locale
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import getpass
import extractor
import sys
import os

#Globals
server = smtplib.SMTP('')
subject = "Factura mensual"
firma_logo = "unnamed.jpg"
from_addr = "proreymon@gmail.com"
username = "alquien"
password = "uno"




def main():
    contBuzon = 0
    exitos = 0
    if len(sys.argv) == 4:
        #Si hay email remitente comenzamos, si no salimos.
        if sys.argv[3] and '@' in sys.argv[3]:
            # Pido el password
            pswd = getpass.getpass('Password:')
            global password  
            password = pswd # Password
            print('Extrayendo información de la base de datos...')
            df = extractor.extraerFilasExcel(sys.argv[1], sys.argv[2])
            
            print('Enviando correos electronicos desde: ' + sys.argv[3])
            global username
            username = sys.argv[3]
            for i in range(0, 4): #len(df)
                if "@" in df.CORRESPONDENCIA.loc[i]:
                    exitos = exitos + enviarCorreo(df.CLIENTE.loc[i], df.SALUDO.loc[i], df.CORRESPONDENCIA.loc[i], df.NOMBRE.loc[i])
                else:
                    print("Sin e-mail, echar al buzón de: " + df.NOMBRE.loc[i])
                    contBuzon = contBuzon + 1
            print("-------------")
            print("Total facturas : " + str(len(df)))
        else:
            print("Error en el email del remitente, error.")
    else:
        print ("FALTAN ARGUMENTOS DE ENTRADA (3): <BASE_DE_DATOS> <PESTAÑA> <REMITENTE_EMAIL>")
    print("Emails enviados: " + str(exitos))

def enviarCorreo(p_num_cliente, p_saludo, p_email, p_nombre):

    conExito = 0
    """
    SMTP Server Information
    1. Gmail.com: smtp.gmail.com:587
    2. Outlook.com: smtp-mail.outlook.com:587
    3. Office 365: outlook.office365.com
    Please verify your SMTP settings info.
    """
    # compongo el saludo
    saludo_formateado = "Buenos días "

    if p_saludo == "EMPRESA":
        saludo_formateado = saludo_formateado + p_nombre
    else: # Sr. o Sra.
        nombre_formateado = p_nombre.partition(' ')[0]
        nombre_formateado = nombre_formateado[0] + nombre_formateado[1:].lower()
        saludo_formateado = saludo_formateado + p_saludo + nombre_formateado

    # Create the body of the message (a HTML version for formatting).
    html = """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta http-equiv="Content-Style-Type" content="text/css">
      <title></title>
      <style type="text/css">
        p.p1 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 14.7px Calibri; color: #453ccc}}
        p.p2 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #453ccc min-height: 14.0px}}
        p.p3 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #453ccc}}
        p.p4 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 12.7px Arial; color: #453ccc}}
        p.p5 {{margin: 0.0px 0.0px 0.0px 0.0px; font: 9.0px Helvetica; color: #3170b9}}
        span.s1 {{font-kerning: none}}
        span.s2 {{font: 12.8px Helvetica; font-kerning: none; color: #0b5ab2}}
        span.s3 {{font: 9.0px Helvetica; text-decoration: underline ; font-kerning: none; color: #3586ff}}
      </style>
    </head>
    <body>
    <p class="p1"><span class="s1">{saludo},</span></p>
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
    <p class="p5"><span class="s1"><i>     </i></span><span class="s1"><i>Este mensaje y sus archivos adjuntos son confidenciales y únicamente podrán ser usados por la persona o entidad a la que van dirigidos. Este mensaje puede contener información confidencial o legalmente protegida. No hay renuncia a la confidencialidad o secreto profesional por cualquier transmisión defectuosa o errónea. Si usted ha recibido este mensaje por error, notifíquelo inmediatamente al remitente.</i></span></p>
    <p class="p5"><span class="s1"></span><br></p>
    <p class="p5"><span class="s1"><i>     Le informamos que sus datos personales son tratados por PROREYMON S.L con la finalidad de gestionar y mantener las relaciones profesionales que nos unen con Usted.</i></span></p>
    <p class="p5"><span class="s1"></span><br></p>
    <p class="p5"><span class="s1"><i>Sus datos podrán ser cedidos a las entidades y administraciones públicas necesarias para la realización de dicha gestión. Este tratamiento de datos es necesario para mantener dicha relación profesional. Los datos se eliminarán cuando finalicen los plazos de prescripción marcados por la ley, conservándose únicamente para atender posibles reclamaciones. Usted puede ejercer sus derechos de acceso, rectificación, cancelación, oposición, portabilidad y limitación del tratamiento de sus datos dirigiéndose a PROREYMON S.L, C/ de las Moreras 48 bj 28300 Aranjuez (Madrid) o a </i><a href="mailto:proreymon@gmail.com"><span class="s3"><i>proreymon@gmail.com</i></span></a><i>, acompañando copia de su DNI acreditando debidamente su identidad. En cualquier situación, Usted tiene derecho a presentar una reclamación ante la Agencia Española de Protección de Datos (AEPD).</i></span></p>
    </body>
    </html>
    """.format(saludo=saludo_formateado)


    # Function that send email.
    def send_mail(username, password, from_addr, to_addrs, msg):
        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()

    # Read email list txt
    #email_list = [line.strip() for line in open('email.txt')]

    #for to_addrs in email_list:
    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = p_email
    


    # Attach HTML to the email
    body = MIMEText(html, 'html')
    msg.attach(body)

    
    # Attach Cover Letter to the email

    cover_letter = MIMEApplication(open("../pdf/"+ p_num_cliente + ".pdf", "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename=p_num_cliente+".pdf")
    msg.attach(cover_letter)

    # This example assumes the image is in the current directory
    fp = open(firma_logo, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    try:
        send_mail(username, password, from_addr, p_email, msg)
        print ("Email enviado a: ", p_email)
        conExito = conExito + 1
    except smtplib.SMTPAuthenticationError:
        print ('SMTPAuthenticationError')
        print ("Email no enviado a: ", p_email)
        conExito = conExito - 1
    return conExito	

if __name__ == '__main__':
    main()


