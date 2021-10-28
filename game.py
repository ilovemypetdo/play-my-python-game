#Import modules
import random
 
#Define species, causes of death, and genders
different_species = ["ant", "ape", "bear", "cat", "dog", "wolf"]
 
ant_deaths = ["you got crushed.", "you carried a little more than 50\ntimes your own weight.", "you forgot your way to the hill.", "you recieved the death sentence from\nthe queen ant."]
 
ape_deaths = ["you climbed too high.", "you failed to find your daily banana."]
 
bear_deaths = ["the fishermen took all the fish.", "you hibernated too long!"]
 
cat_deaths = ["you didn't use the scratching pole\nfor more than 5 minutes.", "your owner got a dog.", "starvation."]
 
dog_deaths = ["you ran too fast.", "you returned to the wild to\nfind your ancestors. Little did you know the wild doesn't\nhave belly rubs!", "starvation"]
 
wolf_deaths = ["you got outplayed", "you tripped and fell down a steep\nflight of stairs, crashing into a Ginsu knife\ndisplay at the bottom.", "you didn't find any food."]
 
genders = ["male", "female"]
 
#Define different species' habitats
ant_habitats = ["desert", "grassland", "ant farm"]
 
ape_habitats = ["jungle", "savanna", "mountainous area"]
 
bear_habitats = ["forest", "tundra", "mountainous area"]
 
wolf_habitats = ["tundra", "forest", "mountainous area", "shrubland"]
 
#Define variables
life_status = "alive"
age = -1
gender = random.choice(genders)
species = random.choice(different_species)
death_message = ""
 
#Define different scenarios
ant_queen = False
ant_worker = False
ant_drone = False
ant_defender = False
 
ape_leader = False
ape_family = False
ape_hungry = False
ape_productive = False
 
bear_mom = False
bear_hungry = False
 
cat_mom = False
cat_dad = False
cat_owner_left = False
 
dog_mom = False
dog_dad = False
dog_owner_left = False
 
wolf_alpha = False
wolf_mom = False
wolf_dad = False
wolf_hungry = False
wolf_productive = False
 
#Define high and low chances of events happening
low_chance = 1
high_chance = 75
 
#Define functions
def decide_home():
    if species == "ant":
        home = random.choice(ant_habitats)
        return home
    
    elif species == "ape":
        home = random.choice(ape_habitats)
        return home
        
    elif species == "bear":
        home = random.choice(bear_habitats)
        return home
    
    elif species == "cat" or species == "dog":
        home = "human's house"
        return home
    
    elif species == "wolf":
        home = random.choice(wolf_habitats)
        return home
 
def start_life():
    home = decide_home()
    male_random_message = chance_dice(0, 1)
    female_random_message = chance_dice(0, 1)
    if gender == "male":
        if male_random_message == 0:
            print("You are born into this world with the two\nchromosomes:")
            print("XY")
            print("Thus, you become a male " + species + ".")
            print("You live in a " + home + ".")
        
        elif male_random_message == 1:
            print("Nice! A computer algorithm chose you to become\na male " + species + "!")
            print("You live in a " + home + ".")
    
    elif gender == "female":
        if female_random_message == 0:
            print("You are born into this world with the two\nchromosomes:")
            print("XX")
            print("Thus, you become a female " + species + ".")
            print("You live in a " + home + ".")
        
        elif female_random_message == 1:
            print("Awesome! A cool computer algorithm chose you to\nbecome a female " + species + "!")
            print("You live in a " + home + ".")
 
def determine_death():
    if species == "ant" and ant_queen == True:
        death_message = random.choice(ant_deaths[0:4])
    
    elif species == "ant" and ant_queen == False:
        death_message = random.choice(ant_deaths)
    
    elif species == "ape":
        death_message = random.choice(ape_deaths)
    
    elif species == "bear" and bear_hungry == True:
        death_message = bear_deaths[0]
    
    elif species == "bear" and bear_hungry == False:
        death_message = bear_deaths[1]
       
    elif species == "cat" and cat_owner_left == True:
        death_message = cat_deaths[2]
        
    elif species == "cat" and cat_owner_left == False:
        death_message = random.choice(cat_deaths[0:3])
    
    elif species == "dog" and dog_owner_left == True:
        death_message = dog_deaths[2]
    
    elif species == "dog" and dog_owner_left == False:
        death_message = random.choice(dog_deaths[0:3])
    
    elif species == "wolf" and wolf_hungry == True:
        death_message = wolf_deaths[2]
    
    elif species == "wolf" and wolf_hungry == False:
        death_message = random.choice(wolf_deaths[0:3])
    
    elif species == "ant" and ant_queen == True and age >= 25:
        death_message = "natural causes."
    
    elif species == "ant" and ant_queen == False and age >= 3:
        death_message = "natural causes."
    
    elif species == "ape" and age >= 25:
        death_message = "natural causes." 
    
    elif species == "bear" and age >= 33:
        death_message = "natural causes."
    
    elif species == "dog" and age >= 9:
        death_message = "natural causes." 
    
    elif species == "cat" and age >= 11:
        death_message = "natural causes." 
    
    elif species == "wolf" and age >= 9:
        death_message = "natural causes." 
        
    return death_message
 
def death_note():
    print("\n======== R.I.P ========")
    print("You have just passed away.\nCause of death: " + determine_death())
    print("Click 'RUN' for a new life!")
    
    if determine_death == "natural causes.":
        natural_death_note()
 
def natural_death_note():
    if determine_death() == "natural causes.":
        print("\n======== R.I.P ========")
        print("You have just passed away of natural causes.")
        print("Click 'RUN' for a new life!")
    
    elif determine_death() == "natural causes." and ant_queen == True:
        print("\n~~~~~~~~ R.I.P ~~~~~~~")
        print("The queen ant has just passed away of natural causes.")
        print("Click 'RUN' for a new life!")
    
    elif determine_death() == "natural causes." and ape_leader == True:
        print("\n~~~~~~~~ R.I.P ~~~~~~~")
        print("The leader of the apes has just passed\naway of natural causes.")
        print("Click 'RUN' for a new life!")
    
    elif determine_death() == "natural causes." and wolf_alpha == True:
        print("\n~~~~~~~~ R.I.P ~~~~~~~")
        print("The alpha wolf has just passed away of natural causes.")
        print("Click 'RUN' for a new life!")
 
def chance_dice(a,b):
    return int(random.randint(a,b))
 
#Show the instructions and set the scene
old_age_death = chance_dice(0, 2)
 
print("Welcome to The Circle of Life, made by DrChicken24.")
print("Press the 'RUN' button for a new life every time!")
print("")
 
print("----------------------------------------------------\n") #Seperator
 
start_life()
print("")
print("And here goes your life as a " + species + ":")
print("")
 
#Game logic
while life_status == "alive":
    age += 1
    if age != 0:
        print("Age: " + str(age))
    
    if random.randint(low_chance, high_chance) == 23:
        life_status = "dead"
    
    #You get more likely to die the longer you live
    #Ants
    if species == "ant" and ant_queen == False and age <= 1:
        high_chance = 25
    elif species == "ant" and ant_queen == False and age <= 2:
        high_chance = 24
    elif species == "ant" and ant_queen == False and age >= 3:
        low_chance = 22
    
    #Queen ant
    if species == "ant" and ant_queen == True and age <= 3:
        high_chance = 150
    elif species == "ant" and ant_queen == True and age <= 10:
        high_chance = 100
    elif species == "ant" and ant_queen == True and age <= 14:
        high_chance = 70
    elif species == "ant" and ant_queen == True and age >= 20:
        high_chance = 30
    elif species == "ant" and ant_queen == True and age >= 30:
        high_chance = 24
    
    #Apes
    if species == "ape" and age <= 4:
        high_chance = 150
    elif species == "ape" and age <= 10:
        high_chance = 100
    elif species == "ape" and age <= 14:
        high_chance = 70
    elif species == "ape" and age >= 25:
        high_chance = 50
    elif species == "ape" and age >= 45:
        high_chance = 30
    elif species == "ape" and age >= 50:
        high_chance = 24
    
    #Bears
    if species == "bear" and age <= 4:
        high_chance = 150
    elif species == "bear" and age <= 10:
        high_chance = 100
    elif species == "bear" and age <= 14:
        high_chance = 70
    elif species == "bear" and age >= 20:
        high_chance = 50
    elif species == "bear" and age >= 30:
        high_chance = 30
    elif species == "bear" and age >= 35:
        high_chance = 24
    
    #Cats
    if species == "cat" and age <= 1:
        high_chance = 150
    elif species == "cat" and age <= 3:
        high_chance = 100
    elif species == "cat" and age <= 5:
        high_chance = 70
    elif species == "cat" and age >= 8:
        high_chance = 50
    elif species == "cat" and age >= 12:
        high_chance = 30
    elif species == "cat" and age >= 15:
        high_chance = 24
    
    #Dogs and wolves
    if species == "dog" or species == "wolf" and age <= 1:
        high_chance = 150
    elif species == "dog" or species == "wolf" and age <= 2:
        high_chance = 100
    elif species == "dog" or species == "wolf" and age <= 4:
        high_chance = 70
    elif species == "dog" or species == "wolf" and age >= 7:
        high_chance = 50
    elif species == "dog" or species == "wolf" and age >= 10:
        high_chance = 30
    elif species == "dog" or species == "wolf" and age >= 13:
        high_chance = 24
        
    #Random events that happen during your life
    #Queen ant
    if species == "ant" and age == chance_dice(1, 200) and gender == "female" and ant_queen == False:
        print("WOW! You got amazingly lucky and\nbecame the queen ant!")
        ant_queen == True
    
    #Worker ant
    if species == "ant" and gender == "female" and ant_worker == False:
        print("Since you were born a female, you\nbecame a worker ant to help the colony\nand take care of the queen!")
        ant_worker = True
    
    #Drone ant
    if species == "ant" and gender == "male" and ant_drone == False:
        print("You were born a male, so you\nare born into the drone position.\nYour job is to repopulate the\ncolony so it can live on!")
        ant_drone = True
    
    #Defender ant
    if species == "ant" and age == chance_dice(1, 10) and gender == "male" and ant_defender == False:
        print("You were personally chosen by the queen\nto defend the colony and become a defender ant!")
        ant_defender == True
    
    #Ape leader
    if species == "ape" and age == chance_dice(20, 220) and ape_leader == False:
        print("AMAZING! You recieved the title of\nleader within your troop!")
        ape_leader == True
    
    #Ape family
    if species == "ape" and age == chance_dice(20, 30) and ape_family == False:
        print("You met another ape like\nyourself and had a family!")
        ape_family == True
    
    #Ape hungry
    if species == "ape" and age == chance_dice(1, 70) and ape_hungry == False:
        print("A time of great famine has\nfallen upon your troop.")
        ape_hungry == True
    
    #Ape productive 
    if species == "ape" and age == chance_dice(1, 50) and ape_productive == False:
        print("It was a productive year!")
        ape_productive == True
    
    #Bear mom
    if species == "bear" and age == chance_dice(20, 30) and gender == "female" and bear_mom == False:
        print("You became a mother to " + str(chance_dice(1, 3)) + " cubs!")
        bear_mom = True
    
    #Bear hungry
    if species == "bear" and age == chance_dice(1, 50) and ape_hungry == False:
        print("A time of great famine has fallen upon you.")
        bear_hungry == True
    
    #Cat mom
    if species == "cat" and age == chance_dice(1, 5) and gender == "female" and cat_mom == False:
        print("You found a mate and gave birth to " + str(chance_dice(1, 8)) + " kittens.")
        cat_mom = True
    
    #Cat dad
    if species == "cat" and age == chance_dice(1, 3) and gender == "male" and cat_dad == False:
        print("You found a mate and became a father to " + str(chance_dice(1, 8)) + " kittens.")
        cat_dad = True
    
    #Cat owner left
    if species == "cat" and cat_owner_left == False:
        print("A very unfortunate chain of events\nled to your owner abandoning you...")
        cat_owner_left = True
    
    #Dog mom
    if species == "dog" and age == chance_dice(1, 5) and gender == "female" and dog_mom == False:
        print("You found a mate and gave birth to " + str(chance_dice(1, 15)) + " puppies.")
        dog_mom = True
    
    #Dog dad
    if species == "dog" and age == chance_dice(1, 3) and gender == "male" and dog_dad == False:
        print("You found a mate and became a father to " + str(chance_dice(1, 15)) + " puppies.")
        dog_dad = True
    
    #Dog owner left
    if species == "dog" and dog_owner_left == False:
        print("A very unfortunate chain of events\nled to your owner abandoning you...")
        dog_owner_left = True
    
    #Wolf alpha
    if species == "wolf" and age == chance_dice(5, 10) and wolf_alpha == False:
        print("Nice! You were randomly selected by some\nvery intricate computer algorithm to be the\n(virtual) alpha of a (also virtual) wolf pack!\n(This post was brought to you by wol;f ganfg)")
        wolf_alpha = True
    
    #Wolf dad
    if species == "wolf" and age == chance_dice(2, 3) and gender == "male" and wolf_dad == False:
        print("You found a mate and became a father to " + str(chance_dice(1, 7)) + " pups.")
        wolf_dad = True
    
    #Wolf mom
    if species == "wolf" and age == chance_dice(2, 3) and gender == "female" and wolf_mom == False:
        print("You found a mate and gave birth to " + str(chance_dice(1, 7)) + " pups.")
        wolf_mom = True
    
    #Wolf hungry
    if species == "wolf" and age == chance_dice(1, 50) and wolf_hungry == False:
        print("A time of great famine has fallen upon your pack.")
        wolf_hungry == True
    
    #Wolf productive
    if species == "wolf" and age == chance_dice(1, 50) and wolf_productive == False:
        print("It was a productive year for your pack!")
        wolf_productive == True
    
    #DIE DIE DIE
    if life_status == "dead":
        death_note()
        
    #Natural deaths
    #Ants
    if species == "ant" and age >= 5:
        if old_age_death == 1:
            life_status = "dead"
            natural_death_note()
    
    #Queen ant
    if species == "ant" and ant_queen == True and age >= 30:
        if old_age_death == 1:
            life_status = "dead"
            natural_death_note()
    
    #Ape
    if species == "ape" and age >= 50:
        if old_age_death == 1:
            life_status = "dead"
            natural_death_note()
    
    #Bear
    if species == "bear" and age >= 35:
        if old_age_death == 1:
            life_status = "dead"
            natural_death_note()
    
    #Cats, dogs, and wolves
    if species == "cat" or species == "dog" or species == "wolf" and age >= 13:
        if old_age_death == 1:
            life_status = "dead"
            natural_death_note()
