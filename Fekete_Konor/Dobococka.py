import random

Start = (input("akkarsz dobni a DND kockával ? (Y/N) : "))

Stop = ("Szomorúvá tetél hogy nem játszol DND-t :( ")

Egg = ("A DUNGEON MESTER AZT MONDJA EZ 36 VOLT")

kocka = random.randint(1, 32)

if Start == "Y":
    print(kocka  )
elif Start == "N":
    print(Stop)
elif Start == "EGG":
        print(Egg)





