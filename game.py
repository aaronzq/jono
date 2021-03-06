from cardset import cardset
from player import player
import time


class gameplay():

    def __init__(self) -> None:
        self.poker_card = cardset()
        p1_cards, p2_cards, p3_cards, p4_cards = self.poker_card.init_shuffle()
        self.p1 = player('0', p1_cards)
        self.p2 = player('1', p2_cards)
        self.p3 = player('2', p3_cards)
        self.p4 = player('3', p4_cards)
        # self.p1.view_card(self.poker_card)
        # self.p2.view_card(self.poker_card)
        # self.p3.view_card(self.poker_card)
        # self.p4.view_card(self.poker_card)
        self.p1._view_card_debug(self.poker_card)
        self.p2._view_card_debug(self.poker_card)
        self.p3._view_card_debug(self.poker_card)
        self.p4._view_card_debug(self.poker_card)
        self.playing_player_id = 0
        self.last_card_id = 0
        self.current_card_id = 0

    def step(self):
        # time.sleep(1)
        if self.playing_player_id==0:
            print("-----------------------------------------")
            self.p1.view_card(self.poker_card)
            print("-----------------------------------------")
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
                    print("skipping the current player...")
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                    print("skipping both the current and next players...")
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
                    print("shuffling hand cards...")
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4

        elif self.playing_player_id==1:
            print("-----------------------------------------")
            self.p2.view_card(self.poker_card)
            print("-----------------------------------------")
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
                    print("skipping the current player...")
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                    print("skipping both the current and next players...")
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
                    print("shuffling hand cards...")
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4

        elif self.playing_player_id==2:
            print("-----------------------------------------")
            self.p3.view_card(self.poker_card)
            print("-----------------------------------------")
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
                    print("skipping the current player...")
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                    print("skipping both the current and next players...")
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
                    print("shuffling hand cards...")
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4

        elif self.playing_player_id==3:
            print("-----------------------------------------")
            self.p4.view_card(self.poker_card)
            print("-----------------------------------------")
            valid = self.p4.my_turn(self.last_card_id, self.poker_card)

            if not valid:
                self.current_card_id = 0
                self.p4.add_hc(self.poker_card.public_cards)
                self.poker_card.empty_public_cards()
            else:
                self.current_card_id = self.poker_card.public_cards[-1]
                if self.current_card_id == 1000:
                    return True
                if self.poker_card.id2val(self.current_card_id) == 996:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+1)%4
                    print("skipping the current player...")
                elif self.poker_card.id2val(self.current_card_id) == 997:
                    self.current_card_id = self.last_card_id
                    self.playing_player_id = (self.playing_player_id+2)%4
                    print("skipping both the current and next players...")
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
                    print("shuffling hand cards...")
                else:
                    self.playing_player_id = (self.playing_player_id+1)%4
        else:
            pass
        
        self.last_card_id = self.current_card_id
        return False


if __name__ == '__main__':

    game = gameplay()
    iteration = 0
    print()
    print("GAME START!")
    while True:
        # time.sleep(2)
        print()
        print()
        print("***************************************************************")
        print("The game is in iter# ", iteration)
        print("Player ", game.playing_player_id ," is playing...")
        print("The last card is ", game.poker_card.id2name(game.last_card_id))
        if game.step():
            break
        iteration = iteration+1


    print("Game finished. The winner is player ", game.playing_player_id)


    # N_try = 10000
    # iteration_count = []
    # win_count = {0:0, 1:0, 2:0, 3:0}
    # for nt in range(N_try):
    #     game = gameplay()
    #     iteration = 0
    #     print()
    #     print("GAME START!")
    #     while True:
    #         # time.sleep(2)
    #         print()
    #         print()
    #         print("***************************************************************")
    #         print("The game is in iter# ", iteration)
    #         print("Player ", game.playing_player_id ," is playing...")
    #         print("The last card is ", game.poker_card.id2name(game.last_card_id))
    #         if game.step():
    #             break
    #         iteration = iteration+1
    #     print("Game finished. The winner is player ", game.playing_player_id)

    #     iteration_count.append(iteration)
    #     win_count[game.playing_player_id] = win_count[game.playing_player_id] + 1
    
    # print(iteration_count)
    # print(win_count)

    # import matplotlib.pyplot as plt

    # fig, ax = plt.subplots()
    # ax.hist(iteration_count, bins=20)

    # ax.set(xlabel='iterations', ylabel='count',
    #     title='iteration of each game')
    # # ax.grid()

    # # fig.savefig("test.png")
    # plt.show()