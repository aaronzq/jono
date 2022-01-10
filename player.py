from cardset import card_in_player, cardset
from typing import List, Tuple
from enum import Enum
import random

class move_type(Enum):
    UNKNOWN_TABLE_CARDS = 1
    KNOWN_TABLE_CARDS = 2
    HAND_CARDS = 3
    WINNING = 4

class player():

    def __init__(self, player_name:str, cards:card_in_player) -> None:
        self.name = player_name
        self.cards = cards
        self.moves = []
        self.mvtype = move_type.HAND_CARDS

    def available_moves(self, last_card_id:int, cardset:cardset) -> None:
        candidate_cards = dict()
        moves = []
        if self.cards.have_hc():
            if (not self.cards.have_utc()) and (len(self.cards.hc())==1):
                for c in self.cards.hc():
                    if cardset.card_lut[last_card_id] == 998:
                        if cardset.card_lut[c] < 9:
                            candidate_cards[cardset.card_lut[c]] = [c]                        
                    else:
                        if cardset.card_lut[c] >= cardset.card_lut[last_card_id] and cardset.card_lut[c] < 996:
                            candidate_cards[cardset.card_lut[c]] = [c]                    
            else:
                for c in self.cards.hc():
                    if cardset.card_lut[last_card_id] == 998:
                        if cardset.card_lut[c] < 9 or cardset.card_lut[c] >= 996:
                            if cardset.card_lut[c] in candidate_cards.keys():
                                candidate_cards[cardset.card_lut[c]] = candidate_cards[cardset.card_lut[c]] + [c]
                            else:
                                candidate_cards[cardset.card_lut[c]] = [c]                        
                    else:
                        if cardset.card_lut[c] >= cardset.card_lut[last_card_id] or cardset.card_lut[c] >= 996:
                            if cardset.card_lut[c] in candidate_cards.keys():
                                candidate_cards[cardset.card_lut[c]] = candidate_cards[cardset.card_lut[c]] + [c]
                            else:
                                candidate_cards[cardset.card_lut[c]] = [c]

            for i in candidate_cards:
                for j,k in enumerate(candidate_cards[i]):
                    moves.append(candidate_cards[i][0:j+1])
            mvtype = move_type.HAND_CARDS

        elif self.cards.have_ktc():
            for c in self.cards.ktc():
                if cardset.card_lut[last_card_id] == 998:
                    if cardset.card_lut[c] < 9 or cardset.card_lut[c] >= 996:
                        if cardset.card_lut[c] in candidate_cards.keys():
                            candidate_cards[cardset.card_lut[c]] = candidate_cards[cardset.card_lut[c]] + [c]
                        else:
                            candidate_cards[cardset.card_lut[c]] = [c]                        
                else:
                    if cardset.card_lut[c] >= cardset.card_lut[last_card_id] or cardset.card_lut[c] >= 996:
                        if cardset.card_lut[c] in candidate_cards.keys():
                            candidate_cards[cardset.card_lut[c]] = candidate_cards[cardset.card_lut[c]] + [c]
                        else:
                            candidate_cards[cardset.card_lut[c]] = [c]
            for i in candidate_cards:
                for j,k in enumerate(candidate_cards[i]):
                    moves.append(candidate_cards[i][0:j+1])
            mvtype = move_type.KNOWN_TABLE_CARDS

        elif self.cards.have_utc():
            moves = [[c] for c in range(-1, -self.cards.n_utc()-1, -1)]
            mvtype = move_type.UNKNOWN_TABLE_CARDS

        else:
            moves = [[1000]] 
            mvtype = move_type.WINNING

        self.moves = moves
        self.mvtype = mvtype

        return None
    
    def my_move(self, move_id:int, cardset:cardset):

        if self.mvtype==move_type.HAND_CARDS:
            hc_temp = self.cards.hc()
            for c in self.moves[move_id]:               
                hc_temp.remove(c)
                cardset.add_public_cards(c)
            self.cards.update_hc(hc_temp)
        elif self.mvtype==move_type.KNOWN_TABLE_CARDS:
            ktc_temp = self.cards.ktc()
            for c in self.moves[move_id]:
                ktc_temp.remove(c)
                cardset.add_public_cards(c)
            self.cards.update_ktc(ktc_temp)
        elif self.mvtype==move_type.UNKNOWN_TABLE_CARDS:
            utc_temp = self.cards.utc()
            c = utc_temp[-self.moves[move_id][0]-1]
            utc_temp.remove(c)
            cardset.add_public_cards(c)
            print("The picked unknown table card is: ", cardset.id2name(c))
            self.cards.update_utc(utc_temp)
        else:
            c = self.moves[move_id][0]
            cardset.add_public_cards(c)

        return None


    def my_turn(self, last_card_id:int, cardset:cardset):
        self.available_moves(last_card_id, cardset)
        valid = True
        if len(self.moves)==0:
            print("You dont have any available move. Please pick a card for an invalid move and take all the public cards.")
            if self.mvtype==move_type.HAND_CARDS:
                self.moves = [[c] for c in self.cards.hc()]
            elif self.mvtype==move_type.KNOWN_TABLE_CARDS:
                self.moves = [[c] for c in self.cards.ktc()]
            valid = False
        
        if self.mvtype==move_type.WINNING:
            print("Game finished. You won.")
            self.my_move(0, cardset)
        elif self.mvtype==move_type.UNKNOWN_TABLE_CARDS:
            print("The available moves are: ", self.moves)

            # insert strategy here to replace the user input
            mvid = int(input("Which move do you wanna choose, from 1 to "+str(len(self.moves))+": ")) - 1

            # random strategy
            # print("Which move do you wanna choose, from 1 to "+str(len(self.moves))+": ")
            # mvid = self.random_strategy(self.moves) - 1

            print("You chose card: ", self.moves[mvid])
            self.my_move(mvid, cardset)
            check = cardset.public_cards[-1]
            if cardset.card_lut[last_card_id] == 998:
                valid = cardset.card_lut[check] < 9 or cardset.card_lut[check] >= 996                     
            else:
                valid = cardset.card_lut[check] >= cardset.card_lut[last_card_id] or cardset.card_lut[check] >= 996
        else:
            print("The available moves are: ", cardset.id2name(self.moves))

            # # insert strategy here to replace the user input
            mvid = int(input("Which move do you wanna choose, from 1 to "+str(len(self.moves))+": ")) - 1

            # random strategy
            # print("Which move do you wanna choose, from 1 to "+str(len(self.moves))+": ")
            # mvid = self.random_strategy(self.moves) - 1

            print("You chose card: ", cardset.id2name(self.moves[mvid]))
            self.my_move(mvid, cardset)

        return valid

    def hc(self) -> List[int]:

        return self.cards.hc()

    def update_hc(self, cards:List[int]) -> None:

        self.cards.update_hc(cards)

    def add_hc(self, cards:List[int]) -> None:

        self.cards.update_hc(cards+self.cards.hc())

    def _view_card_debug(self, cardset:cardset):

        print(self.cards.hc(), cardset.id2val(self.cards.hc()))
        print(self.cards.ktc(), cardset.id2val(self.cards.ktc()))
        print(self.cards.utc(), cardset.id2val(self.cards.utc()))

    def view_card(self, cardset:cardset):

        print("Viewing player: ", self.name, "'s cards:")
        print("Hand cards: ", cardset.id2name(self.cards.hc()))
        print("Known table cards: ", cardset.id2name(self.cards.ktc()))
        print("Unknown table cards: ", ["*" for c in self.cards.utc()])       




if __name__ == '__main__':

    poker_card = cardset()
    p1_cards, p2_cards, p3_cards, p4_cards = poker_card.init_shuffle()
    p1_cards.update_hc([1])
    p1_cards.update_ktc([])
    p1_cards.update_utc([])
    p1 = player('p1', p1_cards)

    last = 13
    print(poker_card.id2val(last))


    p1.view_card(poker_card)
    p1.my_turn(last, poker_card)
    p1.view_card(poker_card)

    print(poker_card.public_cards)




