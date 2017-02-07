import random
from knight import Knight
from crossbow import Crossbow
from swordsman import Swordsman

def start_war():
    essos_army = []
    westerors_army = []

    # Take input from user regarding army composition in Essos and Westerors
    # 1. Knights
    # 2. Crossbow
    # 3. Swordsman
    print("********** WAR BETWEEN ESSOS AND WESTERORS **********")
    print("Tell me the number of knights, swordsman, and crossbowman in Essos")
    e_knights_count = input("Number of knights in Essos : ")
    e_crossbow_count = input("Number of CrossBowman in Essos : ")
    e_swordsman_count = input("Number of Swordsman in Essos : ")

    print("Tell me the number of knights, swordsman, and crossbowman in Westerors")
    w_knights_count = input("Number of knights in Westerors : ")
    w_crossbow_count = input("Number of CrossBowman in Westerors : ")
    w_swordsman_count = input("Number of Swordsman in Westerors : ")

    # Create instance of knight, crossbowman and swordsman and populate essos and westeror army list respwctively.
    for x in range(int(e_knights_count)):
        knight = Knight()
        essos_army.append(knight)

    for x in range(int(e_crossbow_count)):
        crossbow = Crossbow()
        essos_army.append(crossbow)

    for x in range(int(e_swordsman_count)):
        swordsman = Swordsman()
        essos_army.append(swordsman)

    for x in range(int(w_knights_count)):
        knight = Knight()
        westerors_army.append(knight)

    for x in range(int(w_crossbow_count)):
        crossbow = Crossbow()
        westerors_army.append(crossbow)

    for x in range(int(w_swordsman_count)):
        swordsman = Swordsman()
        westerors_army.append(swordsman)

    # Choose soldier from essos and Westeror randomly
    essos_soldier = random.choice(essos_army)
    westeror_soldier = random.choice(westerors_army)
    print("Essos", essos_soldier.__class__.__name__, "is fighting against Westerors", westeror_soldier.__class__.__name__)

    # Condition to check if essos army and westeror army is not empty. Once the user is attacked, health is reduced and
    # once health becomes zero the soldier is removed from the army list. If list becomes empty, all soldiers from the
    # army are dead.

    while len(essos_army) > 0 and len(westerors_army) > 0:

        health_impact_essos = westeror_soldier.attack - essos_soldier.defense
        # Considering the scenario where defense power of a soldier is greater than the attack power
        # In such a scenario the health of soldier with poor attack gets deteriorated.
        if health_impact_essos < 0:
            westeror_soldier.health = westeror_soldier.health - abs(health_impact_essos)
        else:
            essos_soldier.health =  essos_soldier.health - health_impact_essos

        health_impact_westerors = essos_soldier.attack - westeror_soldier.defense
        # Considering the scenario where defense power of a soldier is greater than the attack power
        # In such a scenario the health of soldier with poor attack gets deteriorated.
        if health_impact_westerors < 0:
            essos_soldier.health =  essos_soldier.health - abs(health_impact_westerors)
        else:
            westeror_soldier.health = westeror_soldier.health - health_impact_westerors

        # Condition to increase counter of Essos if Essos soldier health is Zero or less than zero.
        # Such that next soldier in army plays against current Westrors soldier
        if essos_soldier.health < 0 :
            print("Essos", essos_soldier.__class__.__name__, "died!")
            essos_army.remove(essos_soldier)
            # Break the loop if no more Essos soldier are alive
            if len(essos_army) > 0:
                essos_soldier = random.choice(essos_army)
                print("Essos", essos_soldier.__class__.__name__, "is fighting against Westerors",
                      westeror_soldier.__class__.__name__)
            else:
                break

        # Condition to increase counter of Westeror if Westeror soldier health is Zero or less than zero.
        # Such that next soldier in army plays against current Essos soldier
        if westeror_soldier.health < 0:
            print("Westeror", westeror_soldier.__class__.__name__, "died!")
            westerors_army.remove(westeror_soldier)
            # Break the loop if no more Westeror soldier are alive
            if len(westerors_army) > 0:
                westeror_soldier = random.choice(westerors_army)
                print("Essos", essos_soldier.__class__.__name__, "is fighting against Westerors",
                      westeror_soldier.__class__.__name__)
            else:
                break

    # Checking condition to see for which army all the soldiers died.
    if  len(essos_army) == 0:
        print("All essos soldiers died. Essos defeated, Westerors Won")
    if  len(westerors_army) == 0:
        print("********* All Westerors soldiers died. Westerors defeated, Essos Won *********")


if __name__ == '__main__':
    start_war()