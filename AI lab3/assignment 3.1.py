import random


states = {
    ("A","dirty") : "suck",
    ("A","clean") : "MoveRight",
    ("B","dirty") : "suck",
    ("B","clean") : random.choice(["MoveLeft","MoveRight"]),
    ("C","dirty") : "suck",
    ("C","clean") : "MoveLeft"
}


condition = {
    "A" : "dirty",
    "B" : "dirty",
    "C" : "dirty"
}

present_location="A"

for i in range(6):
    percept=(present_location,condition[present_location])
    action= states[percept]
    print(f"Step {i+1}: Location={present_location}, Status={condition[present_location]}, Action={action}")

    if action=="suck":
        condition[present_location]="clean"
    elif action=="MoveRight":
        if present_location=="A":
            present_location="B"
        else:
            present_location="C"
    elif action == "MoveLeft":
        if present_location=="C":
           present_location="B"
        else:
            present_location ="A"


#

import random


states = {
    ("A","dirty") : "suck",
    ("A","clean") : "MoveRight",
    ("B","dirty") : "suck",
    ("B","clean") : random.choice(["MoveLeft","MoveRight"]),
    ("C","dirty") : "suck",
    ("C","clean") : "MoveLeft"
}


condition = {
    "A" : "dirty",
    "B" : "dirty",
    "C" : "dirty"
}

present_location = "A"


action_cost = {
    "suck": 2,
    "MoveRight": 1,
    "MoveLeft": 1
}

total_cost = 0


for i in range(6):
    percept = (present_location, condition[present_location])
    action = states[percept]
    step_cost = action_cost[action]  
    total_cost =total_cost + step_cost
    
    print(f"Step {i+1}: Location={present_location}, Status={condition[present_location]}, Action={action}, Cost={step_cost}, TotalCost={total_cost}")

    if action == "suck":
        condition[present_location] = "clean"
    elif action == "MoveRight":
        if present_location == "A":
            present_location = "B"
        else:
            present_location = "C"
    elif action == "MoveLeft":
        if present_location == "C":
            present_location = "B"
        else:
            present_location = "A"

print("\nFinal Total Cost:", total_cost)


#
    