from GetTodaysMoviesLogic.GetTodaysMovies import GetTodaysMovies
from SenMessages.SendMessages import SendMessage
import schedule
import time


schedule.every().day.at('21:43').do(GetTodaysMovies)

while True:
     schedule.run_pending()
     time.sleep(1)
#print(len(TodaysMovies))