import random
randomnum = random.randint(1, 5)
smallertipp = " A szám kevesebb amit kitaláltam, mint amit te írtál :'("
biggertipp = " A szám nagyobb amit kitaláltam, mint amit te írtál :'("
righttipp = " Gratulálok! :D ELtaláltad!"
newgame = " Ha újra szeretnél próbálkozni akkor indíts újra."
failtipp = " Sajnos ez nem talált. Majd legközelebb. :'( ", newgame
useranswer = input("Gondolok egy számra 1-től 5-ig és megmondom, hogy mennyire közel jártál. Csak egy találatod van. Mehet a játék? (Y/N) ")
useranswerfail = " Akkor zárj be most azonnal >:("
if useranswer == "Y":
    usernum = int(input("Adj meg egy számot: "))
    if usernum == randomnum:
        print(righttipp, newgame)
    elif usernum < randomnum:
        print(smallertipp, failtipp)
    elif usernum > randomnum:
        print(biggertipp, newgame)
elif useranswer == "N":
    print(useranswerfail)
