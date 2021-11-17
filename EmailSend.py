import smtplib
from email.message import EmailMessage

email = EmailMessage()#Declaramos la variable del correo que más tarde se va a enviar
email['from'] = 'Ruben Martinez'#Aquel que envia el correo.
email['to'] = '' #Aqui se escribe el correo al que se va a enviar.
email['subject'] = 'Haz ganado 1,000,000 de dolares!' #El asunto del mensaje.

email.set_content('Soy un maestro del lenguaje Python')#Contenido del mensaje.

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp: #Declaramos y escojemos el host y el puerto.
    smtp.ehlo()
    smtp.starttls()
    smtp.login('elrabaneichon@gmail.com', '1Qaz2wsx1010!')#IMPORTANTE, debido a las nuevas politicas de google, hay que activar el uso de aplicacioes terceras.
    #Claro está que desde la cuenta y password con los que enviaremos el mensaje.
    smtp.send_message(email) #Ahora con el metodo 'send_message' lo encviaremos.
    print('Soy el Jefe maestro :v') #Una instruccion adicional para verificar el buen funcionamiento del codigo anterior.