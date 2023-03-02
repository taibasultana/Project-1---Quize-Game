print("Welcome to my computer quize!")

playing=input("Do you want to play?" )
text=("Tim IS GReat!".lower())
print(text.lower())

if playing != "yes":
    quit()

print("Okay! Let's play:")
Score=0

answer = input("What does CPU stand for?").lower()
if answer.lower()=="Central Processing Unit":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

answer = input("What does CPU stand for?").lower()
if answer.lower()=="Central Processing Unit":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?").lower()
if answer.lower()=="Graphics Processing Unit":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?").lower()
if answer.lower()=="Random Access Memory":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?").lower()
if answer.lower()=="Power Supply":
    print("Correct!")
    Score +=1
else:
    print("Incorrect!")

    print("You got" + str(Score) + "questions correct!")
    print("You got" + str((Score/4)*100) + "%")
