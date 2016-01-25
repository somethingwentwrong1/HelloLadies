from sys import exit


def start():
    print "Welcome. Please have a seat, nube."
    print "I can smell your young flesh..Hmm...."
    print "Those white skin with bright red blood flowing inside.."
    print "Are you really gonna join the Navy Seal? It's not a playground."
    question()


def question():
    choice = raw_input("> ")

    if choice == "Yes":
        sign()
    elif choice == "No":
        kicked_out()
    else:
        not_following_order()


def sign():
    print "Okay. I kinda like ya passion."
    print "Come on. Sign in here. What is your name?"
    name = raw_input("> ")

    print "All right. Come follow me."
    next()


def next():
    print "Here is the weapon training center."
    print "Show me your skills."
    print "Where would you aim?"
    print "'Choose 1)Target 2)General'"
    choice = raw_input("> ")

    if choice == "Target":
        good_job()
    elif choice == "General":
        kicked_out()
    else:
        not_following_order2


def good_job():
    print "Hmm..Follow me."
    sniper_room()


def sniper_room():
    print "He is a nube sniper. Welcome him and teach him some skills."
    print "Chris: 'Hey bud, welcome.I'm Chris Kyle.'"
    print "Chris: 'Oh, it's time for training. Come, follow me."
    training()


def training():
    print "The hardcore training has started.."
    print "4 months later..."
    ready()


def ready():
    print "Chris: 'Oh yeah! We are finally going out to the battle field!'"
    print "Chris: 'Let's kill those yellow guys!'"
    in_war()


def in_war():
    print "General: 'Okay little rabbits! Clean up all those bastards!'"
    print "General: 'Go! Go! Go! Move! Move!'"
    print "How will you jump down? 1)Right away 2)Hesitate"
    choice = raw_input("> ")

    if choice == "Right away":
        print "The bullets of enemy combat plane tore you into 911 pieces."
        in_war()

    elif choice == "Hesitate":
        print "You've dodged the bullets of enemy combat planes."
        print "Half of your comrades are dead."
        landed()

    else:
        not_following_order2


def landed():
    print "Chris: 'No.. We have survived.. but what shall we do.."
    print "Chris: 'We've got only 12 men, and the enemies are about 30."
    print "Bill: 'Enemy spotted!!'"
    print "Chris: 'Hey! Duck down!!'"
    print "What will you do? 1)Duck down 2)Run to the building in front of you"

    choice = raw_input("> ")

    if choice == "Duck down":
        print "The bullets went over your head."
        battle()

    elif choice == "Run to the building in front of you":
        print "You've dodged the bullets and went into building safely,"
        print "but your comrades are going to the other way."
        print "Chris: Oh man! Hey!! Come back!!!"
        left_alone()


def left_alone():
    print "You are carefully going towards the enemies."
    print "The enemies don't know you are coming."
    print "Will you go back to your comrades? Yes/No"

    choice = ("> ")

    if choice == "Yes":
        print "You have safely returned to your comrades."
        battle()

    elif choice == "No":
        print "You are close to the enemies now. It is only about 25 meters."
        print "There are approximately 15 enemies in front. What will you do?"
        shoot()

    else:
        not_following_order2


def shoot():
    print "1)Shoot them 2)Move on"

    choice = ("> ")

    if choice == "Shoot them":
        print "You've killed 10 enemies."
        print "The enemies spotted you."
        print "You are dead, but US won the battle."
        print "You became a war hero."
        print "Ridiculus Ending."
        credit()

    elif choice == "Move on":
        print"You found approximately 25 enemies in front. What will you do?"
        shoot2()

    else:
        not_following_order2


def shoot2():
    print "1)Shoot them 2)Move on"

    choice = ("> ")

    if choice == "Shoot them":
        print "You've killed all the assults."
        print "Chris shut down the rest of the enemy snipers."
        print "You became the legend of the warfare."
        print "Nonrealistic Ending"
        credit()

    elif choice == "Move on":
        print "You are spotted by the enemies."
        print "You are dead without doing anything."
        print "Greedy Ending"
        credit()

    else:
        not_following_order2


def battle():
    print "Bill: 'Hey! Chris and you! Run up to that roof and support us!'"
    print "Bill: 'Try to get the enemy snipers as well.'"
    print "Bill: 'Rest of you ladies follow me. Good luck to you all.'"
    print "Chris and you ran up the roof and supported the comrades."
    print "You found a young boy far away,"
    print "and he was running towards the comrades with a C4."
    print "You: 'Please, please put it down, boy"
    print "You: 'Please..Please...'"
    print "The boy came right in front, and the comrades didn't see him."
    print "You with a wireless set: 'I see a boy with C4 running towards you.'"
    print "Bill: 'I trust your decision. Do what you think is right.'"
    print "What will you do? 1)Shoot him down 2)Wait until the last second"

    choice = raw_input("> ")

    if choice == "Shoot him down":
        print "The boy's chest popped up. You've saved the comrades."
        move_on2()
    elif choice == "Wait until the last second":
        print "The boy dropped C4 and ran away. The comrades are safe."
        move_on1()
    else:
        not_following_order2


def move_on1():
    print "Chris: 'Go! Go! It's  time to slaughter those guys!!'"
    print "The comrades shut down all the enemies."
    print "Chris and you have killed all the enemy snipers."
    victory1()


def move_on2():
    print "Chris: 'Go! Go! It's  time to slaughter those bastards!!'"
    print "The comrades shut down all the enemies."
    print "Chris and you have killed all the enemy snipers."
    victory2()


def victory1():
    print "You came back to US and was rewarded by the General."
    print "You still remember those terrific situations you were in,"
    print "and those memories make you stronger and stronger."
    print "The End."
    credit()


def victory2():
    print "You came back to US and was rewarded by the General."
    print "Even though you are called as a war hero,"
    print "you are suffering in the memory of shooting that little boy."
    print "You cannot erase that memory and choose to commit suicide."
    print "The sound of a loud burst echoes in the house."
    credit()


def credit():
    print "<<<<<<<Made by Jonny Choi.>>>>>>>"
    print "<<<<<<<Thank you.>>>>>>>"


def kicked_out():
    print "You gotta be kidding me right?"
    print "Move your body away from my sight. I'll give you 3 seconds."
    print "3..."
    print "2..."
    print "1..!"
    print "You quickly ran away from the general."
    exit(0)


def not_following_order():
    print "What are you talkin' 'bout? Answer me with Yes or No."
    question()


def not_following_order2():
    print "I don't understand what you are doing. Follow the order."
    next()


start()
