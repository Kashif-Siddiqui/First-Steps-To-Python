# 5-3
print("--Alien Color # 1--")
alien_color = "red"
# VERSION-1
if alien_color == 'green':
    print("You have got 5 points!")
# VERSION-2
else:
    print()

# 5-4
print("\n --Alien Color # 2--")
# VERSION-1
if alien_color != 'green':
    print("You have just earned 10 points.")
# VERSION-2
else:
    print("You have just earned 5 points for shooting the aliens!")

# 5-5
print("\n --Alien Color # 3--")
if alien_color == 'green':
    print("You have got 5 points!")
elif alien_color == 'yellow':
    print("You have got 10 points!")
elif alien_color == 'red':
    print("You have got 15 points!")

# 5-6
print("\n --Stages of Life--")
person=13

if person <2 :
    print("Person is a baby")
elif person >= 2 and person <4 :
    print("Person is a toddler")
elif person >= 4 and person < 13:
    print("Person is a kid")
elif person >= 13 and person < 20:
    print("Person is a Teenager")
elif person >= 20 and person < 65:
    print("Person is a Adult")
else:
    print("Person is a Elder")
