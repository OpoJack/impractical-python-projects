# Name: Jack Oporto
# Project: Silly name generator
# "Impractical Python projects Chapter 1"

# Given a list of first and last names, the program will randomly
# generate a name by combining a first and last name. The user will
# have the option to replay once a name is given.

import sys, random
from time import sleep
first =('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chungis', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
        '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
        'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
        'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
        "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Dickensteinburg III' , 'Dinkleburg' , 'Endicott', 'Fewhairs', 'Gooberdapple', 
        'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

intro = ('Coming in at seven billion pounds...' , "You're gonna like this folks, it's..." ,
        "Introducing, for the first time since the accident..." , "I should've known it was you,",
        "The powerful, the pleasurable, the indestructable", "From the highest mountains, it's",
        "By Odin's beard! You must be", "OMG IT'S", "The returning champion enters the ring once more...it's",
        "Great Scott! That's", "Oh my gosh oh my gosh oh my gosh I'm your biggest fan", "Holy shit it's",
        "It's you...what are you doing here")

outro = ("Can I have your signature!?" , "Inconceivable!" , "Fly, you fool!")

while True:
        firstName = random.choice(first)
        lastName = random.choice(last)
        introduction = random.choice(intro)
        outroduction = random.choice(outro)
        print("\n{} {} {}! {}".format(introduction, firstName, lastName, outroduction), file=sys.stderr)
        sleep(2)

        playAgain = input("\n***Press enter to try again, or 'q' to quit :")
        if playAgain.lower() == "q":
                print("Thanks for playing!")
                break