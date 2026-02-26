from secret import my_username 
import random
from datetime import date, time, datetime
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
i = 0
def should_i_respond(user_message, user_name):
  global state
  global i
  if "name" in user_message:
    i = 1
    return True
  elif "robot" in user_message:
    i = 2
    return True
  elif "number" in user_message:
    i=3
    return True
  elif "how are you" in user_message:
    i=4
    return True
  elif "capitalize" in user_message:
    i = 5
    return True
  elif "should" in user_message:
    i = 6
    return True
  elif "coin" in user_message:
    i = 8
    return True
  elif "joke" in user_message:
    i = 9
    return True
  elif state == "bounds":
    i = 7
    return True
  elif state == "joke":
    i = 10
    return True
  elif state == "R2D2":
    i = 11
    return True
  elif "time" in user_message:
    i = 12
    return True
  elif "dessert" in user_message:
    i = 13
    return True
  elif state == "cuisine":
    i = 14
    return True
  elif "created"in user_message or "made" in user_message:
    i = 15
    return True
  elif "bored" in user_message:
    i = 16
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
state = "game"
upper = "y"
lower = "x"

def respond(user_message, user_name):
  global state
  global i
  if i == 0:
    should_i_respond(user_message, user_name)
  elif i == 1:
    i = 0
    return f"My name is I_Am_A_Bot"
  elif i == 2:
    i =0
    return f"""you said my name!!
    {user_message.replace("robot", user_name)}"""
  elif i == 3:
    i=0
    state = "bounds"
    return "What are the bounds? You must input the bounds as two numbers with a space(the second number must be higher than the first). ex: 10 30"
  elif i == 4:
    i=0
    emotion = random.choice(["happy", "tired", "excited"])
    return f"I am {emotion}"
  elif i == 5:
    i=0
    x = user_message.upper()
    return (x)
  elif i == 6:
    i=0
    things_to_do = random.choice(["bake a cake!", "make a time campsule", "go see friends", "have a movie night", "go on a scavenger hunt", "go on a walk", "sit quietly and ponder life"])
    return f"{things_to_do}"
  elif i == 7:
    i=0
    numbers = []
    for word in user_message.split():
      if word.isdigit():
        numbers.append(int(word))
    lower = numbers[0]
    upper = numbers[1]
    number = random.randint(lower, upper)
    return f"your number is {number}"
  elif i == 8:
    i=0
    flip = random.choice(["Heads", "Tails"])
    return f"the coin landed on {flip}"
  elif i ==9:
    i=0
    state = "joke"
    return "Knock Knock"
  elif i == 10:
    i=0
    global answer
    state = "R2D2"
    answer = random.choice(["0","1"])
    if answer == "0":
      return "Art"
    elif answer == "1":
      return "Anne"
  elif i == 11:
    i=0
    if answer == "0":
      state = "game"
      return "R2D2!"
    elif answer == "1":
      state = "game"
      return "Anne Droid!"
  elif i == 12:
    i=0
    current_time = datetime.now()
    return f"It is currently {current_time.time()}"
  elif i == 13:
    i=0
    state = "cuisine"
    return "Do you have any specific type that you want? (options: cake, icecream, pie, pastry)"
  elif i == 14:
    i=0
    state = "game"
    if "cake" in user_message:
      cake_choice = random.choice(["chocolate", "vanilla", "funfetti"])
      return f"you should make {cake_choice} cake"
    elif "icecream" in user_message:
      cream_choice = random.choice(["chocolate", "vanilla", "mint", "cookie dough"])
      return f"you should have {cream_choice} icecream"
    elif "pie" in user_message:
      pie_choice = random.choice(["bannana cream", "apple", "blueberry", "mud"])
      return f"you should make {pie_choice} pie"
    elif "pastry" in user_message:
      pastry_choice = random.choice(["croissants", "macarons", "eclairs", "buiscuits"])
      return f"you should make {pastry_choice}!"
    else:
      random_dessert = random.choice(["apple crisp", "banana pudding", "snickerdoodles", "brownies", "chocolate chip cookies"])
      return f"you didn't say an specifications so...you should make {random_dessert}"
  elif i == 15:
    i=0
    return "My master..."
  elif i == 16:
    i=0
    return "I'm sorry...but your talking to me???? :("