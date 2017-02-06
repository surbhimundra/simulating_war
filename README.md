# WAR OF ESSOS AND WESTERORS
This program simulates the war between the two armies ESSOS adn WESTERORS
For this project, I have created two json files essos.json and westerors.json
These json files consist of array of json objects where each object provides the information about the individual soldier.

Each json object of soldier provides info about the name, defense power, attack power and the health of the soldier.
Defense Power: Scale of 10
Attack Power: Scale of 10
Health: Scale of 20

# How to run this
```python3 war.py```

# How does it work?
The program assumes that two soldiers come face-to-face each other.
They both attack each other.
So there are two attacks between two soldiers.
1. Essos attack
    Outcome = essos attack - westerors defense
2. Westerors attack
    Outcome = westerors attack - essos defense
Soldier health = health - outcome

# Assumptions
At a time only one soldier fights against the another soldier from opposite army.

# Improvements
- Programmatically pick the random soldier form both army than in a sequence and delte the soldier form the json file who dies.
- Define different categories like Knights etc. and give special power to diffrent categories.
