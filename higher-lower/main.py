from art import logo
from art import vs
from game_data import data
import random

print(logo)

def pick_people():
  num1 = random.randint(0, len(data))
  pick = data[num1-1]
  #count = pick1['follower_count']
  print(pick['name'])
  return pick
  #print(count)

def followers():
  person1 = pick_people()
  #print(person1['follower_count'])
  return person1['follower_count']

def ask_pick():
  comparing = True
  p1 = pick_people()
  pnum1 = p1['follower_count']
  pname1 = p1['name']
  p2 = pick_people()
  pnum2 = p2["follower_count"]
  pname2 = p2['name']
  newlist = []
  newlist.append(p1)
  newlist.append(p2)
  while comparing:


    print(f"A:  {pname1} is against... ")
    print(vs)
    print(f"B:  {pname2}. Who has more followers?")
    question = input(f" A for {pname1}, B for {pname2}.    ").lower()
    if question == 'a':
      if pnum1 > pnum2:
        print("Right choice")
        #newlist.pop(1)
        #print(newlist)
        p2 = pick_people()
        #newlist.append(p2)
      elif pnum1 < pnum2 :
        print("You lose")
        return

    elif question == 'b':
      if pnum2 > pnum1:
        print("Right choice")
       # newlist.pop(0)
       # print(newlist)
        p1 = pick_people()
       # newlist.append(p1)
      elif pnum2 < pnum1 :
        print("You lose")
        return


ask_pick()
