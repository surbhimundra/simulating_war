# WAR OF ESSOS AND WESTERORS
This program simulates the war between the two armies ESSOS adn WESTERORS
For this project, I take the composition(Number of knights, ) of each army from the user.
Once the composition of each team is known, I populate the list with the respective knight, crossbowman and swordsman object
for each army.

Each Knight, Crossbowman and Swordsman uses
Defense Power: Scale of 20
Attack Power: Scale of 20
Health: Scale of 25

I iterate through essos list and westeror list. On the basis of outcome of the attack, health of the soldiers is reduced
untill the health becomes less than zero. When the soldier health becomes zero or negative, we remove the soldier form the
list. For the team whose list gets empty, the other team wins.

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
