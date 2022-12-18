import time

def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print("Time ist zu ende!")

if __name__ == '__main__':
   user_time = int(input("Geben Sie eine Zeit in Sekunden ein: "))
   countdown(user_time)