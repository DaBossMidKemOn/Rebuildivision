#Created by Oli McPherson and Ben OSU!

import random
import time

projectlist = ['-A wind tunnel\n','-A weather vane\n','-A wind turbine\n','-Guttering around the roof\n','-A water tank\n','-A garden\n']

def gameintro ():
  print("It is a cold, dark night, and you sit shivering in your hut in the wilderness...\n")
  time.sleep(2)
  print("The door is blown off it's hinges as a particularly nasty blast of wind strikes your hut. You flinch back involuntarily...\n")
  time.sleep(2)
  print("A stranger, clad all in black rags, stumbles in the door...\n")
  time.sleep(2)
  print("He falls onto the rickety, threadbare couch, and gasps for air...\n")
  time.sleep(2)
  print("He looks up at you, and says he can help you get rid of this storm...\n")
  time.sleep(2)
  print("He talks of different projects that could be undertaken to stop the storm, and make the most of it's effects...\n")
  time.sleep(2)
  print("Once morning arrives, you sit with your list of projects, and try to decide what to do...\n")
  time.sleep(2)

def listProjects():
    for element in projectlist:
        print(element)
    
gameintro()

def projectchooser ():
  print("The projects available are:\n")
  listProjects()
    
  project1=input('What project should be undertaken?')
  
projectchooser()