#Created by Oli MacPherson and Ben O'Sullivan!
#For use with only Python 2 at the moment cause i cant be bothered changing all the raw_inputs.
#Define voracious: wanting or devouring great quantities of food. (It's a big complicated word so it looks good in the game,)

#git add -A
#git commit -m "CC"
#git push origin master

import random
import time
import sys

intro_phrases = ["The world is changing. \n",
                 "Humanity's voracious appetite for and consumption of electricity born of burning coal and oil is releasing harmful gas into the atmosphere. \n",
                 "You will now experience the effects of this upon the world's climate. \n",
                 "Your objective is to survive for as long as you can, in a world of violent climate change. \n",
                 "Good luck. \n"]
bucket="fetch a bucket"
drip="let it drip"

def intro ():
  for phrase in intro_phrases:
    print(phrase)
    time.sleep(2.5)

def route_choice_1 ():
  answer_routechoice1 = (raw_input("WHich way do you go?").replace(" ","")).upper()
  if answer_routechoice1 == "TOTHEOASIS":
    print("You run towards the glorious sight, splashing water from the bucket in your haste to reach it. Once ou arruive, however, it fades. It was a mirage.")
    time.sleep(3)
    print("You gaze at your now empty bucket, then sit, and weep.")
    print("You die of thirst. You have failed. Your score is 500 points.")
    sys.exit()
  if answer_routechoice1 == "TOTHEHOUSE":
    print("You stroll towards the house, drinking leisurely from the bucket as you do. You have made it to the door when you hear thundering feet behind you. You turn, and see a massive lizard thundering towards you.")
    time.sleep(4)
    housedoorchoice()
  else:
    print("Invalid answer. Please type either 'To the oasis'' or 'To the house'.")
def stuck_in_room_2 ():
  print("It seems you only have a few seconds until the door collapses. Do you leave the house through the back window, or climb through the trapdoor in the ceiling?")
  answer_stuckinroom = (raw_input().upper()).replace(" ", "")
  if answer_stuckinroom == "CLIMBTHROUGHTHETRAPDOOR":
    print("You scramble up to the trapdoor, and climb through. The roof, weakened by the downpour, cannot withstand your weight. You fall, and die in pain.")
  if answer_stuckinroom == "LEAVETHROUGHTHEWINDOW":
    print("You leap out of the window.")
    if bucketYorN == 1:
      print("The sun is shining down, blinding. The weather has changed significantly. Now, the sun-baked earth is rapidly drying out.")
      time.sleep(2)
      print("You walk for miles, unbearably thirsty, and eventually perish from dehydration.")
      print("You have failed. Your score is 450 points.")
      sys.exit()
    else:
      print("The sun shines down upon you. Suddenly thirsty, you drink from the bucket.")
      time.sleep(2)
      print("You begin to walk, and are faced with two routes. In the distance, their looms a beautiful oasis. To the left, however, their is a small house that seems uninhabited.")
      time.sleep(3)
      route_choice_1()  
  else:
    print("Invalid answer. Please type either 'climb through the trapdoor' or 'leave through the window'.")
      
def extreme_rain_2 ():
  print("Your door is blown off it's hinges with the force of the gale, and water pours in the door. Do you stay where you are, or barricade yourself in the other room?")
  extreme_rain_2_answer = (raw_input().replace(" ","")).upper()
  if extreme_rain_2_answer == ("Stay where I am".replace(" ","")).upper():
    print("You stay in your chair, watching as the water floods the room.")
    time.sleep(2)
    print("You doze off, peacefully.")
    time.sleep(2)
    print("You do not wake up. You have drowned. You have failed. Your score is 400 points.")
    sys.exit()
  if (extreme_rain_2_answer).upper() == ("barricade myself in the other room".replace(" ","")).upper():
    print("You run to the door, and pause. Should you take the bucket?")
    takethebucket = (raw_input()).upper()
    if takethebucket == 'YES':
      print("You grab the bucket, then turn, and rush into the other room, barricading it behind you.")
      bucketYorN = 0
      stuck_in_room_2()
    if takethebucket == "NO":
      print("You ignore the bucket, and dash into the room.")
      bucketYorN = 1
      stuck_in_room_2()
    else:
      print("That is not a valid answer. Please type either 'Yes' or 'No'.")
  else:
      print("That is not a valid answer. Please type either 'stay where I am' or 'barricade myself in the other room'.")
      extreme_rain_2()

def very_thirsty_rain_big_roof_leak ():
  print("You are extremely thirsty. You stumble over to the stream of water dribbling down from the tiles, and drink until your thirst is sated.")
  extreme_rain_2()
  
def rain_1_roof_leak_big ():
  time.sleep(1)
  print("The leak in the roof gets slowly larger. There are some wooden boards to the side of the room, and some tiles. Do you plug the hole, and if so, with what?")
  rain_1_roof_leak_big_answer = (raw_input()).upper()
  if (rain_1_roof_leak_big_answer.replace(" ","")).upper() == ("Plug the hole with boards".replace(" ","")).upper():
    print("You pick up the boards, and nail them in place. The leak stops completely.")
    time.sleep(2)
    print("An hour later, you are unbearable thirsty. You gaze at the empty bucket longingly, and at the plugged hole in the ceiling.")
    time.sleep(2)
    print("You open the door, and stumble outside, only to find the sun blinding you with it's heat. \n You fall backwards.")
    time.sleep(2)
    print("You stay there until you die of thirst. You have failed. Your score is 350 points.")
    sys.exit(2)
  if rain_1_roof_leak_big_answer.replace(" ","") == ("Plug the hole with tiles".replace(" ","")).upper():
    print("You pick up the tiles, and glue them to the roof. Some water still seeps through.")
    very_thirsty_rain_big_roof_leak()
  if rain_1_roof_leak_big_answer.replace(" ","") == ("Leave the hole".replace(" ","")).upper():
    time.sleep(1)
    print("The roof, weakened by the downpour and the hole, collapses, crushing you. \n" + "You have failed. Your score is 300 points.")
    sys.exit(2)
  else:
    print("Invalid answer. Please type 'Plug the hole with boards', 'Plug the hole with tiles', or 'Leave the hole'.")
    rain_1_roof_leak_big()

def correct_answer_rain_1_answer_1 ():
  print("You get a bucket and place it under the dripping ceiling. Water begins to collect in the bottom of the bucket.")
  time.sleep(2)
  extreme_rain_2()

def incorrect_answer_rain_1_answer_1 ():
  print("You sit back in your chair, content to let the rain drip. It's only a small leak after all.")
  time.sleep(2)
  rain_1_roof_leak_big()

def other_answer_rain_1_answer_1 ():
  print("Invalid response. Please type either 'fetch a bucket' or 'let it drip'.")
  rain_1_answer_function()

def rain_1_answer_function (rain_1_answer_1):
  if rain_1_answer_1.replace(" ", "") == bucket.replace(" ", ""):
    correct_answer_rain_1_answer_1()
  if rain_1_answer_1.replace(" ", "") == drip.replace(" ", ""):
    incorrect_answer_rain_1_answer_1()
  if rain_1_answer_1.replace(" ", "") != drip.replace(" ","") or bucket.replace(" ", ""):
    other_answer_rain_1_answer_1()

def extreme_rain_1 ():
  print("The rain is bucketing down around you. You are sitting at home, snug inside your small, two-room house. The roof begins to leak, just a little. What do you do?")
  rain_1_answer_function((raw_input("Do you fetch a bucket and catch the water, or do you let it drip?").replace(" ",""))).upper()

    
#intro()
extreme_rain_1()