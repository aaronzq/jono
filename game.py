from cardset import cardset
from player import player


class gameplay():

    def __init__(self) -> None:
        self.poker_card = cardset()
        p1_cards, p2_cards, p3_cards, p4_cards = self.poker_card.init_shuffle()
        self.p1 = player('p1', p1_cards)
        self.p2 = player('p2', p2_cards)
        self.p3 = player('p3', p3_cards)
        self.p4 = player('p4', p4_cards)
        self.p1.view_card(self.poker_card)
        self.p2.view_card(self.poker_card)
        self.p3.view_card(self.poker_card)
        self.p4.view_card(self.poker_card)
        # self.p1._view_card_debug(self.poker_card)
        # self.p2._view_card_debug(self.poker_card)
        # self.p3._view_card_debug(self.poker_card)
        # self.p4._view_card_debug(self.poker_card)
        self.playing_player_id = 0
        self.last_card_id = 0
        self.current_card_id = 0

    def step(self):
        winning = 0
        if self.playing_player_id==0:
            valid = self.p1.my_turn(self.last_card_id, self.poker_card)

            if not valid:
                self.current_card_id = 0
                self.p1.add_hc(self.poker_card.public_cards)
                self.poker_card.empty_public_cards()
            else:
                self.current_card_id = self.poker_card.public_cards[-1]
                if self.current_card_id == 1000:
                    return True
                if self.poker_card.id2val(self.current_card_id) == 996:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                elif self.poker_card.id2val(self.current_card_id) == 999:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                    self.poker_card.public_cards.pop(-1) # delete the card from the game
                    cards_temp = self.p1.hc()+self.p2.hc()+self.p3.hc()+self.p4.hc()
                    p1c, p2c, p3c, p4c = self.poker_card.shuffle(cards_temp)
                    self.p1.update_hc(p1c)
                    self.p2.update_hc(p2c)
                    self.p3.update_hc(p3c)
                    self.p4.update_hc(p4c)
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4

        elif self.playing_player_id==1:
            valid = self.p2.my_turn(self.last_card_id, self.poker_card)

            if not valid:
                self.current_card_id = 0
                self.p2.add_hc(self.poker_card.public_cards)
                self.poker_card.empty_public_cards()
            else:
                self.current_card_id = self.poker_card.public_cards[-1]
                if self.current_card_id == 1000:
                    return True                
                if self.poker_card.id2val(self.current_card_id) == 996:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                elif self.poker_card.id2val(self.current_card_id) == 999:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                    self.poker_card.public_cards.pop(-1) # delete the card from the game
                    cards_temp = self.p1.hc()+self.p2.hc()+self.p3.hc()+self.p4.hc()
                    p1c, p2c, p3c, p4c = self.poker_card.shuffle(cards_temp)
                    self.p1.update_hc(p1c)
                    self.p2.update_hc(p2c)
                    self.p3.update_hc(p3c)
                    self.p4.update_hc(p4c)
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4

        elif self.playing_player_id==2:
            valid = self.p3.my_turn(self.last_card_id, self.poker_card)

            if not valid:
                self.current_card_id = 0
                self.p3.add_hc(self.poker_card.public_cards)
                self.poker_card.empty_public_cards()
            else:
                self.current_card_id = self.poker_card.public_cards[-1]
                if self.current_card_id == 1000:
                    return True
                if self.poker_card.id2val(self.current_card_id) == 996:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                elif self.poker_card.id2val(self.current_card_id) == 999:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                    self.poker_card.public_cards.pop(-1) # delete the card from the game
                    cards_temp = self.p1.hc()+self.p2.hc()+self.p3.hc()+self.p4.hc()
                    p1c, p2c, p3c, p4c = self.poker_card.shuffle(cards_temp)
                    self.p1.update_hc(p1c)
                    self.p2.update_hc(p2c)
                    self.p3.update_hc(p3c)
                    self.p4.update_hc(p4c)
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4
                    
        elif self.playing_player_id==3:
            valid = self.p3.my_turn(self.last_card_id, self.poker_card)

            if not valid:
                self.current_card_id = 0
                self.p3.add_hc(self.poker_card.public_cards)
                self.poker_card.empty_public_cards()
            else:
                self.current_card_id = self.poker_card.public_cards[-1]
                if self.current_card_id == 1000:
                    return True
                if self.poker_card.id2val(self.current_card_id) == 996:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                elif self.poker_card.id2val(self.current_card_id) == 999:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                    self.poker_card.public_cards.pop(-1) # delete the card from the game
                    cards_temp = self.p1.hc()+self.p2.hc()+self.p3.hc()+self.p4.hc()
                    p1c, p2c, p3c, p4c = self.poker_card.shuffle(cards_temp)
                    self.p1.update_hc(p1c)
                    self.p2.update_hc(p2c)
                    self.p3.update_hc(p3c)
                    self.p4.update_hc(p4c)
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4
        else:
            pass
        
        self.last_card_id = self.current_card_id
        return False


if __name__ == '__main__':

    game = gameplay()
    iteration = 0
    while True:
        
        print("The game is in iter# ", iteration)
        print("Player ", game.playing_player_id ," is playing...")
        print("The last card is ", game.last_card_id)
        if game.step():
            break
        iteration = iteration+1

    print("Game finished. The winner is player ", game.playing_player_id)