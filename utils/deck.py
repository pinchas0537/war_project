import random

def create_card(rank:str,suite:str) -> dict:
    cards_value = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    cards_rank_and_suita = {"rank": rank ,"suita": suite}
    cards_rank_and_suita["value"] = cards_value[rank]
    return cards_rank_and_suita

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "WAR"
    
    
def create_deck() -> list[dict]:
    rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suite  = ["H","C","D","S"]
    all_tickets = []
    for i in rank:
        for j in suite:
            card = create_card(i,j)
            all_tickets.append(card)
    return all_tickets


def shuffle(deck:list[dict]) -> list[dict]:
    for _ in range(1000):
        index1 = random.randint(0,51)
        index2 = random.randint(0,51)
        while index1 == index2:
            index2 = random.randint(0,51)
            
        temp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp
        
    return deck