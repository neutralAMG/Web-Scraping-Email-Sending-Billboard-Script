from selenium import webdriver
from selenium.webdriver.common.by import By
from Model.MoviesObjet import Movie
from SenMessages.SendMessages import SendMessage
from SenMessages.SendMessages import SendOneMessage
import time


#Add the timer like class to handle the scheduling of tasks

#Add the background service 

# Add the whatsapp sending message funcionality

#Make the background service activate at 9:00 AM and send the massages 
def GetTodaysMovies():
  
  driver = webdriver.Chrome()
  driver.get("https://caribbeancinemas.com/gt/theater/galeria-360/")
  MoviesForToday = []
  
  mainDiv =  driver.find_element(By.CLASS_NAME, "grid")
  horarios = mainDiv.find_elements(By.CLASS_NAME, 'ROW')
  
  CurrentMovie = 1
  
  SendOneMessage()
 
  for x in horarios:
      # Add Description by clicking on the ver mas link
      
      imageUrl = x.find_element(By.XPATH,f'//*[@id="horarios"]/div[{CurrentMovie}]/div/div/div[1]/a[1]/img').get_property('src')
      title = x.find_element(By.XPATH,f'//*[@id="horarios"]/div[{CurrentMovie}]/div/div/div[2]/h1/b').text
      languaje = x.find_element(By.XPATH,f'//*[@id="horarios"]/div[{CurrentMovie}]/div/div/div[2]/h5/i').text
      genres = x.find_element(By.XPATH,f'//*[@id="horarios"]/div[{CurrentMovie}]/div/div/div[2]/div[1]/h5/span[1]').text
      rated = x.find_element(By.XPATH,f'//*[@id="horarios"]/div[{CurrentMovie}]/div/div/div[2]/div[1]/h5/span[2]').text
      Hours = []
      hours = x.find_elements(By.CLASS_NAME,f'myButton2')

      for y in hours:
         Hours.append(y.text)
         
      newMovie = Movie(imageUrl,title, languaje, genres, rated, Hours)
      time.sleep(1)
      SendMessage(newMovie)
      MoviesForToday.append(newMovie) 
      CurrentMovie+= 1    
  return MoviesForToday


