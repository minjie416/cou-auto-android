from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from os.path import basename
import smtplib
import time

__author__ = 'kzhu'



class Utility():


    def get_index(self,str,list):
        index = 0
        for index in range(0,len(list)):
            if str in list[index]:
                break
        if (index == len(list)-1): #No such str in the list
            index = -1
        return index

    def send_mail_with_attachment(self,smtp_server,email_from,email_to,subject,plain,fileToSend):
        today = time.strftime("%Y%m%d")
        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = email_to
        msg['Subject'] =subject +" "+today
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=basename(fileToSend))
        msg.attach(attachment)
        part1 = MIMEText(plain, 'plain')
        msg.attach(part1)
        server = smtplib.SMTP(smtp_server)
        server.sendmail(email_from, email_to, msg.as_string())
        server.close()

    def send_mail(self,email_from,email_to,subject,smtp_server,html):
        today = time.strftime("%Y%m%d")
        msg = MIMEMultipart('alternative')
        msg["From"] = email_from
        msg["To"] = email_to
        msg['Subject'] = subject +" "+today
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
        server = smtplib.SMTP(smtp_server) #"10.75.106.10:25"
        server.sendmail(email_from, email_to, msg.as_string())
        server.close()