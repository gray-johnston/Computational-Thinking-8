# Beginning: create variables
Burger_points = 0
Fish_points = 0

# Middle: Ask questions

answer = input("are you A) a swimmer, or B) a person who likes burgers")
if answer == "A":
    Fish_points += 1
elif answer == "B":
    Burger_points += 1


answer = input("are you A) a person who fishes, or B) a person who burgers")
if answer == "A":
    Fish_points += 1
elif answer == "B":
    Burger_points += 1


answer = input("would wou A) rather have 4 fish, or B) smack a burger")
if answer == "A":
    Fish_points += 1
elif answer == "B":
    Burger_points += 1


answer = input("would you rather A) yes fish, or B) burgaburga")
if answer == "A":
    Fish_points += 1
elif answer == "B":
    Burger_points += 1


answer = input("how do you A) fish fish fish, or B) burger bros")   
if answer == "A":
    Fish_points += 1
elif answer == "B":
    Burger_points += 1
# End: Determine results
if Fish_points > Burger_points:
    print("you are a fish")
elif Burger_points > Fish_points:
    print("you are burger")