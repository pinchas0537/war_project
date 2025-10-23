from utils.deck import create_deck,shuffle

def create_player(name:str = "AI") -> dict:
    player = {"name":name,"hand":[],"won_pil":[]}
    return player

def init_game()->dict:
    game_dict = {}
    player_1 = create_player("yy")
    player_2 = create_player()

    shuffle_ = shuffle(create_deck())
    p1 = shuffle_[:26]
    p2 = shuffle_[26:]

    return game_dict
def play_round(p1:dict,p2:dict):
    pass