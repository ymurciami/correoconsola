import fire
import smtplib
from email.message import EmailMessage

class CorreoClass(object):

  def correo(self,Sender_Email,Password, Reciever_Email, asunto, mensaje, nombrearchivo):
    
    newMessage = EmailMessage()                         
    newMessage['Subject'] =asunto
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content(mensaje) 
    files = [nombrearchivo]

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as smtp:
      smtp.starttls()
      smtp.login(Sender_Email, Password)              
      smtp.send_message(newMessage) 
    return "Se envio correctamente"

if __name__ == '__main__':
  fire.Fire(CorreoClass)

#python correo.py correo 'CorreoSale@hotmail.com' 'ContraseñaCorreosale' 'CorreoVa@gmail.com' 'Asunto' 'Mensaje' 'Archivo'