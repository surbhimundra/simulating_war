import json

def start_war():
    # Loading the json file for two armies which have every soldier information(name, attack power, defense power and health)
    with open('essos.json') as data_file:
        essos = json.load(data_file)
    with open('westerors.json') as data_file:
        westerors = json.load(data_file)

    # Instantiating variables for storing eash army size
    essos_army = len(essos)
    westerors_army = len(westerors)

    # Counters to iterate through army
    ecount = 0
    wcount = 0

    print(essos[ecount]['name'], "from essos is fighting", westerors[wcount]['name'], "from Westerors")

    # e_health = Essos health
    # w_health = Westerors health
    e_health = essos[ecount]['health']
    w_health = westerors[wcount]['health']


    while 1 == 1:
        # Condition to increase counter of Essos if Essos soldier health is Zero or less than zero.
        # Such that next soldier in army plays against current Westrors soldier
        if e_health < 0 :
            print(essos[ecount]['name'], "died!")
            e_health = essos[ecount]['health']
            ecount += 1
            # Break the loop if no more Essos soldier are alive
            if ecount >= essos_army:
                break
            print(essos[ecount]['name'], "from essos is fighting", westerors[wcount]['name'], "from Westerors")

        # Condition to increase counter of Westeror if Westeror soldier health is Zero or less than zero.
        # Such that next soldier in army plays against current Essos soldier
        if w_health < 0:
            print(westerors[wcount]['name'], "died!")
            w_health = westerors[wcount]['health']
            wcount += 1
            # Break the loop if no more Westeror soldier are alive
            if wcount >= westerors_army:
                break
            print(essos[ecount]['name'], "from essos is fighting", westerors[wcount]['name'], "from Westerors")


        health_impact_essos = westerors[wcount]['attack'] - essos[ecount]['defense']
        # Considering the scenario where defense power of a soldier is greater than the attack power
        # In such a scenario the health of soldier with poor attack gets deteriorated.
        if health_impact_essos < 0:
            w_health = w_health - abs(health_impact_essos)
        else:
            e_health =  e_health - health_impact_essos

        health_impact_westerors = essos[ecount]['attack'] - westerors[wcount]['defense']
        # Considering the scenario where defense power of a soldier is greater than the attack power
        # In such a scenario the health of soldier with poor attack gets deteriorated.
        if health_impact_westerors < 0:
            e_health =  e_health - abs(health_impact_westerors)
        else:
            w_health = w_health - health_impact_westerors

    # Checking condition to see for which army all the soldiers died.
    if ecount >= essos_army:
        print("Essos defeated, Westerors Won")
    if wcount >= westerors_army:
        print("Westerors defeated, Essos Won")


if __name__ == '__main__':
    start_war()