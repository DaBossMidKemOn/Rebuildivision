#Created by Oli MacPherson and Ben O'Sullivan!
#For use with only 3 at the moment cause raw_input sucks
#Define voracious: wanting or devouring great quantities of food. (It's a big complicated word so it looks good in the game,)

import random
import time

drip = "let it drip"
bucket = "fetch a bucket"


def intro ():
  print("The world is changing. \n")
  time.sleep(2)
  print("Humanity's voracious appetite for and consumption of electricity born of burning coal and oil is releasing harmful gas into the atmosphere. \n")
  time.sleep(2)
  print("You will now experience the effects of this upon the world's climate. \n")
  time.sleep(2)
  print("Your objective is to survive as long as you can. \n")
  time.sleep(2)
  print("Good luck. \n")
  time.sleep(2)

def extreme_rain_1 ():
  print("The rain is bucketing down around you. You are sitting at home, snug inside your small, two-room house. The roof begins to leak, just a little. What do you do?")
  rain_1_answer_1()
def rain_1_answer_1 ():
  rain_1_answer_1 = input("Do you fetch a bucket and catch the water, or do you let it drip?") 
  if rain_1_answer_1.upper() == bucket.upper():
    print("You get a bucket and place it under the dripping ceiling. Water begins to collect in the bottom of the bucket.")
    time.sleep(2)
    extreme_rain_2()
  elif rain_1_answer_1.upper() == drip.upper():
    print("You sit back in your chair, content to let the rain drip. It's only a small leak after all.")
    time.sleep(2)
    rain_1_roof_leak_big()
  else:
    print("Invalid response. Please type either 'fetch a bucket' or 'let it drip'.")
    rain_1_answer_1()
    
intro()
extreme_rain_1()