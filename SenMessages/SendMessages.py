from twilio.rest import Client
from datetime import date

account_sid = 'AC516441baa6222b38489c36ef49a7fd00'
auth_token = '40b5abc9ee46a31c15195148786763b3'
mensajante = 'whatsapp:+14155238886'
remitente = 'whatsapp:+18292555212'
client = Client(account_sid, auth_token)

def SendOneMessage():
    
    fecha = date.today()
    message = client.messages.create(
        from_=f'{mensajante}',
        body=f'La cartelera de hoy {fecha.strftime("%Y-%m-%d")}',
        to=f"{remitente}"
    )
  
    
def SendMessage(movie):
    Hours = DisplayHours(movie.Hours)
    message = client.messages.create(
      from_=f'{mensajante}',
      body= f"""
    
       {movie.Name}
       {movie.Languaje}
       {movie.Genres}
       {movie.Rated}
       {Hours}
     
    
      """,
      to=f'{remitente}'
    )
    print("sended")
  
  
  
def DisplayHours(movie):
    stri = ""
    for m in movie:
        stri += m + ' - '
    return stri

