# from twilio.rest import Client 
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

fecha = date.today()
User = " " #EMAIL USED TO SEND THE EMAILS
Port = 587 # PORT TO USE FROM YOUR HOST
Host ="smtp.gmail.com" # SERVER UTILIZE TO SEN THE EMAILS
Reciver = "" # WHO IS GOING TO RECEIVE THEMAIL
Password = "" # PASSWORD TO AUTHENTICATE YOUR EMAIL -- NOTE YOU WILL NEED TO CREATE A GOOGLE APP PASWORD TO GET A VALID PASSWORD TTO USE HERE
def SendMessage(movies):
    conectiom =  smtplib.SMTP(Host,Port)
    conectiom.starttls()
    conectiom.login(user=User, password=Password)
    conectiom.set_debuglevel(True)
    messageBody = """
    <html>
     <head><head>
     <body>
    """
    for movie in movies:
        messageBody += f"""
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 10px;">
    <tr>
        <td align="center">
            <img src="{movie.ImageUrl}" width="100%" style="max-width: 500px; height: auto; border-radius: 10px;" alt="{movie.Name}">
        </td>
    </tr>
    <tr>
        <td style="font-family: Arial, sans-serif; font-size: 16px; color: #333333; padding: 10px;">
            <p><strong>Nombre:</strong> {movie.Name}</p>
            <p><strong>Lenguaje:</strong> {movie.Languaje}</p>
            <p><strong>Género:</strong> {movie.Genres}</p>
            <p><strong>Rating:</strong> {movie.Rated}</p>
            <p><strong>Horarios:</strong> {movie.Hours}</p>
        </td>
    </tr>
</table>
      """
    
    messageBody += f"""
    </body>
    </html>
    """
    
    message = MIMEMultipart( "alternative");
    message['To'] = Reciver ;
    message['From'] = User;
    message['Subject'] = f"La cartelera de hoy {fecha.strftime("%Y-%m-%d")}"
    message.attach(MIMEText(messageBody, "html"))
    try:
         conectiom.sendmail(
         from_addr=User,
        to_addrs=[Reciver], 
        msg= message.as_string()
         )
    finally:
      conectiom.quit()
      conectiom.close()
      print("sended")
  
  
  
