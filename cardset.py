from typing import Tuple, List, Union
import random
import csv

class card_in_player():

    def __init__(self, cards=None) -> None:
        if cards==None:
            self.unknown_table_cards = []
            self.known_table_cards = []
            self.hand_cards = []
        else:
            self.unknown_table_cards = cards[0:3]
            self.known_table_cards = cards[3:6]
            self.hand_cards = cards[6:]
    
    def utc(self) -> List[int]:
        
        return self.unknown_table_cards

    def ktc(self) -> List[int]:
        
        return self.known_table_cards

    def hc(self) -> List[int]:
        
        return self.hand_cards
    
    def n_utc(self) -> int:

        return len(self.unknown_table_cards)
    
    def have_utc(self) -> bool:
        
        return len(self.unknown_table_cards)>0
    
    def have_ktc(self) -> bool:
    
        return len(self.known_table_cards)>0
    
    def have_hc(self) -> bool:
    
        return len(self.hand_cards)>0

    def update_utc(self, cards:List[int]) -> None:
        if len(cards)<=3:
            self.unknown_table_cards = cards
        else:
            raise Exception("Invalid update for unknown table cards")
    
    def update_ktc(self, cards:List[int]) -> None:
        if len(cards)<=3:
            self.known_table_cards = cards
        else:
            raise Exception("Invalid update for known table cards")

    def update_hc(self, cards:List[int]) -> None:

        self.hand_cards = cards

class cardset():

    def __init__(self, card_map_file='card_map.csv') -> None:
        self.card_ids = list(range(53))
        # 2 3 ... K A, and 4 types
        vals = list(range(2,15))
        vals[0] = 996
        vals[1] = 997
        vals[7] = 998
        vals[8] = 999
        # print(vals)
        self.card_lut = dict(zip(self.card_ids, [0]+vals*4))
        self.card_map = dict()

        with open(card_map_file, newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row in reader:
                self.card_map[int(row[0])] = row[1] + " " + row[2]

        self.public_cards = []
        # print(self.card_lut)

    def shuffle(self, cards:List[int]):
        inds = random.sample(cards, len(cards))
        return inds[0::4], inds[1::4], inds[2::4], inds[3::4]
    
    def init_shuffle(self):
        p1, p2, p3, p4 = self.shuffle(self.card_ids[1:])
        self.player1card = card_in_player(p1)
        self.player2card = card_in_player(p2)
        self.player3card = card_in_player(p3)
        self.player4card = card_in_player(p4)
        
        return self.player1card, self.player2card, self.player3card, self.player4card

    def add_public_cards(self,card_id):
        self.public_cards.append(card_id)

    def empty_public_cards(self):
        self.public_cards=[]

    def id2val(self, card_ids):

        if type(card_ids)==int:
            return self.card_lut[card_ids]
        elif type(card_ids)==list:
            return [self.card_lut[c] if type(c)==int else [self.card_lut[cc] for cc in c] for c in card_ids]
        else:
            return None
    
    def id2name(self, card_ids):

        if type(card_ids)==int:
            return self.card_map[card_ids]
        elif type(card_ids)==list:
            return [self.card_map[c] if type(c)==int else [self.card_map[cc] for cc in c] for c in card_ids]
        else:
            return None       



if __name__ == '__main__':

    cards = cardset()

    print(cards.id2val([[2],[34],[1]]))
    print(cards.id2name([[2],34,[1]]))


    # cards.init_shuffle()
    # print(cards.card_lut[13])
    # print(cards.shuffle('a','b'))
    # print(cards.shuffle.__annotations__)