#Caroline West
#chill112@charlotte.edu

import time
import random
user_error = 0

print("")

while 1:
	try: 
		start_game=input("Start game? Y/N ")
		if not (start_game =="Y" or "y" or "yes" or "YES" or "Yes" or "N" or "n" or "no" or "No"):
			raise TypeError 
			break
		elif (start_game =="Y" or "y" or "yes" or "YES" or "Yes" or "N" or "n" or "no" or "No"):
			break

	except TypeError:
		user_error = user_error+1
		if user_error == 1:
			print("That was not a valid option")

		elif user_error >1:
			print("That is STILL not a valid option")

if start_game == ("Y" or "y" or "yes" or "Yes" or "YES"):
	print("You are ready to begin")

##elif start_game == "N"or "n" or "no" or "No":
	

	print("")
print("")
print("**********************************************************************************************************")

print("Before we get started, please answer a few questions")
name = input("Name: ")
career = input("What is/was your career? ")
hobbies = input("Hobies? ")
dislikes = input("Dislikes? ")
town = input("Where do you live? ")

print("**********************************************************************************************************")

print("")

print("Hi beautiful. It's so good to meet you,  " + name + "!!!")
#greets the user based on user input
print("")
time.sleep(1)

print("******************************************************")
water_counter=10
#water_counter is how thirsty you are. This will play a role in the final battle decision

#storyline
print("How's your day going?")
print("*******************************************************")

print("\t 1. Red flag. Bye") #Go back to sleep
print("\t 2. I'm doing well, how are you doing?") #Drink the liquid dripping from the celing")
print("\t 3. Fantastic! I went for a walk around " + town + ".") #Venture out into the hallway

while 1:
	try:
		choice=input("Choose an option ")
		if (choice.isnumeric() == False):
			raise TypeError
		elif not (choice =="1" or choice =="2" or choice =="3"):
			raise ValueError 
		else:
			break
	except TypeError:
		print("That is not a number")
		user_error = user_error +1
	except ValueError:
		print("Not a valid option")
		user_error = user_error +1 

if choice == "1":
	#ends the game
	#storyline
	print("That is an answer. However, this is often an innocent question")
	quit()

elif choice == "2": 
	#storyline
	print("I'm so glad to hear that! I am having a great day now that I get to talk to you ;) ")
	print("Tell me about yourself? ")

	water_counter=water_counter+5

	print("\t 1.Umm no thank you. Red flag ") #Now that your thirst is quenched, you lay down and sleep
	print("\t 2. I am a " + career + "and I really enjoy " + hobbies + ".") #Venture out into the hallway

	while 1:
		try:
			choice2 = input("What do you do next? ")
			if (choice2.isnumeric() == False):
				raise TypeError
			elif not (choice2 =="1" or choice2 == "2"):
				raise ValueError
			elif (choice =="1" or choice =="2"):
				break
		except TypeError:
			print("That is not a number")
		except ValueError:
			print("You did not enter 1 or 2")

	

	if choice2 == "1":
		#ends the game
		#storyline
		print("Good job trying to be safe.")
		print("However, this is often an okay question to be asked.")
		quit()


elif choice == "3":
	water_counter=water_counter-5
	#Initial decision of going into the hallway instead of sleeping or drinking the liquid

#storyline
print("Wow! What a small world. I was just visiting " + town + " and it's so beautiful this time of year. ")
print("I would love to visit " + town + " again.") 
print("")

print("\t 1. I am a " + career + "it's so convenvient being walkable from my house, but I feel like I'm meant for more") #Go to the left into the darkness
print("\t 2. I am a " + career + "It's very fulfilling and rewarding") #Go to the right to the voices

while 3:
	try:
		choice3=input("How should you respond? ")
		if (choice3 == "1" or choice3 =="2"):
			break
		elif (choice3.isnumeric() == False):
			raise TypeError
		elif (choice3.isnumeric() == True and choice3 !="1" and choice3 !="2") :
			raise ValueError

	except TypeError:
			print("That was not a number")

	except ValueError:
			print("Not a valid option")


if choice3=="1":
	#You've gone into the hallway and decided to turn left
	#storyline
	print("I'm so impressed! Not everyone can be a " + career + ". You must be a really hard worker")
	time.sleep(2)
	print("You should go where you feel appreciated! People like you and me are meant for more than the status quo has to offer.")
	time.sleep(2)
	print("")
	print("Even though we just met, I feel like I've known you for years. It's so hard finding someone I can relate to like this...")
	print("Not trying to be too forward, but it would make my day if I could send you flowers. What is your address?  ")
	print("\t 1. I'm sorry, but no. I would feel more comfortable meeting in a public location first") #Fully submit to all that is right with the universe
	print("\t 2. You are so sweet, here is my address.") #Fight with the shred of willpower left to overcome the creature

	while 4:
		try:
			choice4 = input("What will you do? ")
			if (choice4.isnumeric() == False):
				raise TypeError
			elif not (choice4 =="1" or choice4 == "2"):
				raise ValueError
			elif (choice4 =="1" or choice4 =="2"):
				break
		except TypeError:
			print("That is not a number")
		except ValueError:
			print("You did not enter 1 or 2")
	
	if choice4=="1":
		#You've gone into the hallway, turned left into darkness, and submitted to Cthullu
		#storyline
		print("Not a problem " + name +  ". I never want you to feel unformfortable")
		print("Honestly, I'm really proud of you for being so protective of your personal information. It's hard to find someone as discerning as you.")
		print("My address is 1600 Pennslyvania Avenue. You work so hard sweetheart, can I send you some money so you can buy yourself flowers?")
		print("That way, you don't have to give a stranger your home address.")
		print("Venmo is probably the safest way for me to send you money with the end-to-end encryption")
		print("Because venmo is so secure, it is asking me for your phone number and email address.")
		print("Worst case scenario " + name + "if things don't work out, you can always block me :) ")
		print("")

		print("\t 1. Pause at the doorway to assess the situation")
		print("\t 2. Charge into the room")

		while 5:
			try:
				choice5 = input("How to proceed? ")
				if (choice5.isnumeric() == False):
					raise TypeError
				elif not (choice5 =="1" or choice5 == "2"):
					raise ValueError
				elif (choice5 =="1" or choice5 =="2"):
					break
			except TypeError:
				print("That is not a number")
			except ValueError:
				print("You did not enter 1 or 2")


		if choice5=="1":
			#You've gone into the hallway, left into darkness, submitted to Cthullu, and paused at the doorway
			#storyline
			print("You wait at the edge of the doorway, listening as you count the number of people in the room by the different voices.")
			print("You’re confused by the weird growling. ")
			print("You so badly want to just rush in there, that’s what your brain is compelling.") 
			print("Fighting it… is… pain. But you are cautious, just a few more moments to learn more about who it is you were sent to annihilate.") 
			print("Fighting with the will of Cthullu has exhausted you, and you don’t notice how dimmed your senses are until you’re surrounded.")
			print("How did you not notice the quiet that had descended into the room?")
			print("The leader sighs at you, with melancholy resignation in his worn eyes.") 
			print("You lunge at him, baring your teeth, muscles tense, when someone shoves a mirror in your face, stopping you in your tracks, frozen at the reflection.") 
			print("Red, soulless eyes peer back at you, your face contorted with shock and malice.") 
			print("What are you?") 
			print("You stare deeper into your own eyes as the gravity of existential dread consumes you.") 
			print("You don’t even notice the sound of a sword unsheathing or register the flash of silver of the sword raised above your head before it comes down on you.") 
			print("And then there is nothing.")

		elif choice5=="2":
			#You've gone into the hallway, left into darkness, submitted to Cthullu, and charged into the room
			#storyline
			print("You burst through doorway with unnatural speed and a hiss escaping your lips. ")
			time.sleep(1)
			print("You scan the room as you rage takes control of your limbs, running into the first sentry with such force he crumples to the ground. ")
			print("The power coursing through you surges as you completely submerge yourself into the ethereal ocean of power. ")
			print("You’re so incredibly thirsty for more as you drink from the never ending well of magic. ")
			print("")
			print("")
			time.sleep(1)
			print("The ground beneath you quivers as the stone walls crumble around you. ")
			time.sleep(1)
			print("A fiendish smile graces your mouth as you behold the ruin. ")
			print("Rock plummets from the ceiling, and within seconds, rubble covers everyone and everything in the room, completing this mission, but you are safe. ")
			print("You will always be safe. Before stalking out of the room, you glance at the mirror broken in the corner and behold a creature reminiscent of a human, but not quite anymore. ")
			print("Your own red eyes stare back at you, the pupils swirling. ")
			print("For a second you think you see a pained face begging for escape, but then it vanishes, replaced by your own cruel reflection. ")
			print("")
			time.sleep(3)
			print("Your soul has been stolen by Cthullu. You will never experience rest, cursed to roam the worlds for eternity. ")
			time.sleep(5)
			quit()

	elif choice4=="2":
		#You've gone into the hallway, left into the darkness, fought Cthullu and you will lose
		#storyline
		print("You scream at the searing pain disobedience costs you. ")
		print("You desperately want the power this creature silently offers you, but you know something isn’t right about it. ")
		print("The power… it’s too much, and the word “evil” slips into the periphery, but you can’t grasp onto it before the word is erased from your memory. ")
		print("You grasp blindly around you for any kind of weapon, but you know it’s futile. ")
		print("The best you can do is attempt to maintain your autonomy in a battle of wills against the creature. ")
		print("")
		print("You feel the talons of Cthullu wrapping around your consciousness as you are excruciatingly forced out of existence. ")
		time.sleep(5)
		quit()

elif choice3=="2":
	#You've gone into the hallway, right towards the voices
	print("You follow the voices")
	print("\t 1. Drink the puddle in the corner first. Hydration is key")
	print("\t 2. Charge right in")
	
	puddle_choice=input("What will you? ")
	#will increase the water count, which will affect the final battle
	if puddle_choice=="1":
		water_counter=water_counter+5
		print("After refreshing puddle water, you charge right in")

	#storyline
	print("At full speed, you burst into the room")
	print("The warrior just stare at you")
	print("The leader asks 'Will you join us to fight the evil that is Cthullu?' ")
	print("You know the only answer is yes, so you agree. ")
	print("You madke an alliance and you all march out to fight. ")
	print("")
	print("************************************************************************")

	print("With many torches and encantations, your team goes down the long hallway")

	#choosing to drink the dripping water or puddle water earlier will increase the water counter
	#the value of water_counter determines the outcome

	print("\t 1. Stone")
	print("\t 2. Diamond")
	print("\t 3. Rage")

	while 3:
		sword_choice = input("Which sword will you choose? Enter a number: ")
		if sword_choice.isnumeric():
			sword_choice = int(sword_choice)
			break
		else:
			print("That was not a number")
			user_error = user_error + 1

	secret_num = random.randint(1,100)
	battle_outcome=sword_choice*secret_num

	if (battle_outcome <= 50 and battle_outcome>= 20):
		print("Your sword is a mighty weapons and instantly does damage")

	elif battle_outcome < 20:
		print("Your sword brings shame to your family, but you can continue")

	if user_error > 1:
		print("Tread carefully adventurer. You don't seem to be one for details")

	if user_error > 3:
		print("Your inability to follow directions has cost you the game")
		time.sleep(2)
		print("************************************************************************")
		print("Goodbye")
		time.sleep(3)
		quit()

	if water_counter>5:
		print("You successfully defeat cthullu in a swift battle")
		print("Congratulations!!!! YOU WIN")
		print("You will have a long, healthy, and prosperous life")
		print("Valhalla awaits, and Odin welcomes you")

	elif water_counter==5:
		print("You and your squad engage in a battle that rages on for days")
		print("After much sweat and blood, you emerge victorious")
		print("With your last breath, you know you have won")

	elif water_counter<5:
		print("Your sword breaks as you valliantly try to slay Cthullu")
		print("It is all futile, and you perish at the hands of Cthullu")
		print("Maybe next time you'll be more grateful when given free water")



			