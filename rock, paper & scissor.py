import random
Choko=input("select Stone, Paper, or Scissor :").lower()
Mistu=random.choice(["Stone", "Paper","Scissor"]).lower()
print("Mistu choiced: ",Mistu)

if Mistu == "Stone" and Choko == "Scissor":
    print("Mistu won")
elif Mistu == "Paper" and Choko == "Stone":
    print("Mistu won")
elif Mistu == "Scissor" and Choko == "Paper":
    print("Mistu won")
elif Mistu == Choko:
    print("Tie")
else:
    print("Choko won")    