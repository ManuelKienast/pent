# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:17:23 2018

@author: Manuel

the pentaton logic go around II

"""


import random
import time


random.seed(0)
print(random.getrandbits(5))


# =============================================================================
# 
# Variables
# =============================================================================

# list of still available tracks:
available_tracks = ['1', '2', '3', '4', '5']


# =============================================================================
# 
# aBout the Board:
# =============================================================================

class Board:
    
    def __init__(self, length, min_val, max_val):
        
        self.min_val = min_val
        self.max_val = max_val
        self.value   = self.create_tile(min_val, max_val)
        self.length  = length
        self.track1  = self.build_track()
        self.track2  = self.build_track()
        self.track3  = self.build_track()
        self.track4  = self.build_track()
        self.track5  = self.build_track()
        self.dict_   = {'Track1': self.track1, 'Track2': self.track2,\
                        'Track3': self.track3, 'Track4': self.track4,\
                        'Track5': self.track5}

        
        if 'Wit' in self.value.keys(): 
            self.Wit = self.value['Wit']
        else:
            self.Wit =  None
        
        if 'Stren' in self.value.keys():
            self.Stren = self.value['Stren']
        else:
            self.Stren =  None
        
        if 'Dex' in self.value.keys(): 
            self.Dex = self.value['Dex']
        else:
            self.Dex =  None
        
        if 'Intel' in self.value.keys(): 
            self.Intel = self.value['Intel']
        else:
            self.Intel =  None
     
    
    def __str__(self):
        
        string = ''
        for count, track in enumerate(self.dict_.values(), 1):
            for tile in track.items():
                string += '\nTrack Number: {} --> Tier: {}, '.format(count, tile)
        return string
        
    
    def create_tile(self, min_val, max_val):
        
        pos = ['Wit', 'Stren', 'Dex', 'Intel']
        pos = random.sample(pos, 2)
        tile_value = {}
        for i in pos:
            tile_value[i] = random.randrange(min_val, max_val+1)
        return tile_value

    
    def build_track(self):
        
        tile_dict = {}
        var_min = self.min_val
        var_max = self.max_val
        
        for i in range(1, self.length+1):
            
            tile_dict[i] = self.create_tile(var_min, var_max)
            var_min += 3
            var_max += 3
            
        print('tile_track created.')
        return tile_dict

"""        
print(board)
td = Board(10,1,4)
print(td.dict_)

"""


# =============================================================================
# 
# concerning Attributes:
# =============================================================================

class Attribute:
    """the base atr-class"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def increase_value(self, increment):
        self.value += increment
        
    def get_value(self):
        return int(self.value)
    
    def set_value(self, value):
        setattr(self, 'value', value)
    
        
class Wit(Attribute):
    """Wit-atr w/ wit-special ability"""
    
    def ability(self):
        
        if self.value < 6:
            print('you noob')    
        if self.value > 5 and self.value < 11:
            print('keep growing')    
        elif self.value > 10 and self.value < 16:
            print('getting there')
        elif self.value > 15 and self.value < 17:
            print('pretty good')
        elif self.value > 20:
            print('woaah')
        
        
class Stren(Attribute):
    """Stren-atr w/ stren-special ability"""
    
    def ability(self):
        
        if self.value < 6:
            print('you noob')    
        if self.value > 5 and self.value < 11:
            print('keep growing')    
        elif self.value > 10 and self.value < 16:
            print('getting there')
        elif self.value > 15 and self.value < 17:
            print('pretty good')
        elif self.value > 20:
            print('woaah')
    
    
class Dex(Attribute):
    """Dex-atr w/ dex-special ability"""
    
    def ability(self):
        
        if self.value < 6:
            print('you noob')    
        if self.value > 5 and self.value < 11:
            print('keep growing')    
        elif self.value > 10 and self.value < 16:
            print('getting there')
        elif self.value > 15 and self.value < 17:
            print('pretty good')
        elif self.value > 20:
            print('woaah')
    
    
class Intel(Attribute):
    """Intel-atr w/ intel-special ability"""
    
    def ability(self):
        
        if self.value < 6:
            print('you noob')    
        if self.value > 5 and self.value < 11:
            print('keep growing')    
        elif self.value > 10 and self.value < 16:
            print('getting there')
        elif self.value > 15 and self.value < 17:
            print('pretty good')
        elif self.value > 20:
            print('woaah')
    

# =============================================================================
# 
# die würfel sind gefallen:
# =============================================================================

class Dice():
    
    
    def throw_dice(self, throws):
        
        result_list = []
        
        for throw in range(throws):
            result = random.randrange(1, (self.sides +1))
            
            print('\nyou rolled a: ', result)
            result_list.append(result)
            time.sleep(1)
        
        print('you achieved a total result of: ', sum(result_list))
        return result_list
        

class D6(Dice):
    
    def __init__(self):
        
        super(type(self))
        self.sides = 6
        
        
class D4(Dice):
    
    def __init__(self):
        
        super(type(self))
        self.sides = 4
        
D6().throw_dice(3)

# =============================================================================
# 
# just read the fucking card:
# =============================================================================

class Card():
    """description of Card; with M/ for testing im card can target a player and 
    applying the card effect depending on temp/perm mod effect"""
    
    
    def __init__(self, name, text, atr, atri_mod, temp, location):
        self.name      = name
        self.text      = text
        self.atr       = atr
        self.atri_mod  = atri_mod
        self.temp      = temp
        self.container = []
        self.location  = location
        
        
        
    def __str__(self):
        return '\nName    : {}\nText    : {}\nModifies: {}\nBy      : {}\nTemp    : {}\nLocation: {}'.format\
                (self.name, self.text, self.atr, self.atri_mod, self.temp, self.location)
                
    
    def test_card(self):
        """tests if card can mod a player, by checking if the mod is type(int)"""
        
        return isinstance(self.atri_mod, int)
    
    
    def show_cards(self):
        """prints/returns a list of all cards in contianer."""
        
        for card in self.container:
            print(card)
        

    def mod_player(self, player):
        """applys the atri-mod-number to eihter the player's temp or perm atr(attribute),
        if atri-mod would set art to < 0 it sets 0 instead."""
    
        if self.test_card() == True and self.atr in dir(player):
            
            if self.temp:
                
                player_atr   = getattr(player, self.atr).get_value()
                modified_atr = player_atr + self.atri_mod
                
                if modified_atr < 0:
                    value = getattr(player, self.atr)
                    value.set_value(0)
                    
                else:
                    value = getattr(player, self.atr)
                    value_int = value.get_value()
                    value.set_value(value_int + self.atri_mod)
                    #value.increase_value(self.atri_mod)
                
                setattr(player, self.atr, value)
                

#deck = Deck()
#p1.draw_card(5)
#active_Card = p1.select_card_by_name()
#input_ = input('player name: >')
#active_Card.mod_player(p1); print(p1)
#p1.play_card()

# =============================================================================
# 
# all the cards are in contianers:
# =============================================================================

class Card_container:
    
    def __init__(self):
        self.name      = 'base_container'
        self.size      = self.container_size()
        self.container = []
    
    
    def __str__(self):
        
        result = ""
        for c in self.container:
            result += c.__str__() + '\n'
        if result == '':
            result = 'there is nothing here'
        return result
    
    
    def initialize_container(self):
        
        if self.name == 'deck':
        
            file_path = 'pent_resc/cards.txt'
            deck_list = []            
            fopen = open(file_path, 'r')
            
            for line in fopen:
                
                text_list = line.split(', ')
                list_format = [text_list[0], text_list[1], text_list[2], int(text_list[3]), bool(text_list[4]), 'deck']
                deck_list.append(Card(*list_format))
                
            print('\nDeck created:\n')
            #deck.__str__()
            fopen.close()
                
        if self.name == 'hand':
            deck_list = []
            
        if self.name == 'yard':
            deck_list = []
            
        return deck_list
    
    
    def container_size(self):
        
        if self.container:
            return len(self.container)
        else:
            print('your pile is empty.')


class Deck(Card_container):
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'deck'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

class Hand(Card_container):
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'hand'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

class Graveyard(Card_container):
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'yard'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

# =============================================================================
#     
# playing with the Player:
# =============================================================================

class Player():
    """the player base class."""
    
    def __init__(self, name, text, Wit, Stren, Dex, Intel, ):
        self.name          = name
        self.text          = text
        self.Wit           = Wit
        self.Stren         = Stren
        self.Dex           = Dex
        self.Intel         = Intel
        self.atr_tup       = ('Wit', 'Stren', 'Dex', 'Intel')
        self.atr_self_tup  = (self.Wit, self.Stren, self.Dex, self.Intel)
        self.track         = 0
        self.tier          = 1
        self.container     = Hand()
        self.hand_size     = self.container.container_size()
        self.card_playable = 'no'
        self.active_turn   = 'no'
        self.success_pool  = 0
       
    
    def __str__(self):
        return "\nPlayer Name: {} \n{}'s Wit  : {} \n{}'s Stren: {} \n{}'s Dex  : {}\
                \n{}'s Intel: {} \n{}'s Cards: \n{}".format\
                (self.name, self.name, self.Wit, self.name, self.Stren, self.name, self.Dex,\
                 self.name, self.Intel, self.name, self.container.__str__())
    
    
    def select_track(self):
        
        for count, track in enumerate(board.dict_, 1):
            if str(count) in available_tracks:
                print('\n', track, ':\n', board.dict_[track])
        
        while True:
            track = input('Choose the track you want to challenge. Give me a number 1-5: >')
            if track in available_tracks:
                break
        
        board_dict_key = 'Track' + track
        self.track = board_dict_key
        
        available_tracks.remove(track)
        print('those tracks are still available', available_tracks)
        print('you chose track number: ', track, board.dict_[board_dict_key])
    
    
    def test_attribute(self, atr, test_value):
        """tests attribute, the self.atr against a test_value."""
        
        global tile_dict
        
        if atr >= test_value:
            print('you passed your check.')
            return True
        else:
            print('you failed your check.')
            return False

            
            
    def level_up(self):
        """after a succesfull self.tile_check() it allows the player to increase one
        of his atris by +1 and increases self.tier."""
        
        print('\nyour current stats:  Wit: {}  Stren: {}  Dex: {}  Intel: {}.'.format\
                                     (self.Wit, self.Stren, self.Dex, self.Intel))
        
        while True:
            
            up = input('\nwhich atribute do you wanna level up(+1)? ').capitalize()
            
            if up not in self.atr_tup:
                print('\nplease retype, couldnt understand your input.')
            
            else:
                value = getattr(self, up)
                value.increase_value(1)
                break
                
       
    def show_hand(self):
        
        if self.container.container_size():
            print('\nThis is your current hand:\n', self.container.__str__())
        else:
            print('your hand is empty, my friend.')
            
            
    def select_card_by_name(self):
        """lets player select one card by name from hand."""
        
        hand       = self.container.container
        card_names = [card.name for card in hand]
        
        
        if not hand:
            print('\nyou have nothing to select, draw some cards. duh.')
            
        else:
            while True:
                
                self.show_hand()
                name = input('\nWhich card do you want to select? Print its name: >')
                
                if name in card_names:
            
                    active_card_index = next(i for i, card in enumerate(hand) if card.name == name)
                    break
                    
                else:
                    print('\ncant find your selection, plz enter the name again.')
                    continue
            
            active_card = hand[active_card_index]
            print(active_card)
            return active_card
    
    
    def draw_card(self, amount):
        
        i = 0
        while i < amount:
            try:
                rand_index = random.randrange(0, deck.container_size())
                card_active = deck.container[rand_index]
                card_active.location = 'hand'
                self.container.container.append(card_active)
                deck.container.pop(rand_index)
                print('\nyour new card: \n', self.container.container[-1])
                i += 1
            except ValueError:
                print('pile exhausted, shuffle yard back to deck\n raised by draw_card.')
                break
    
    
    def discard_card(self, amount=None, name=None):
        """discards cards from hand to yard either at random (amount) or specific cards(name)"""
        
        card_names = [card.name for card in self.container.container]
        hand       = self.container.container
        
        if self.container.container_size():
            
            if isinstance(amount, int):
                print('im Int')
                if amount >= self.container.container_size():
                    while hand:
                        card_active = hand.pop(0)
                        card_active.location = 'yard'
                        graveyard.container.append(card_active)
                        print('you discarded: ', card_active)
                else:
                    for i in range(amount):
                        card_index = random.randrange(0, self.container.container_size())
                        card_active = hand.pop(card_index)
                        card_active.location = 'yard'
                        graveyard.container.append(card_active)
                        print('you discarded: ', card_active)
                            
            if isinstance(name, str):
                print('im string')
                
                if name in card_names:
                    card_index = next(i for i, card in enumerate(hand) if card.name == name)
                    active_card = hand[card_index]
                    
                else:
                    active_card = self.select_card_by_name()
                    
                hand.remove(active_card)
                active_card.location = 'yard'
                graveyard.container.append(active_card)
                print('\nhas been discarded.')
                    
        else:
            print('you have nothing to discard')
    
    
    def play_card(self):
        
        hand = self.container.container
        
        self.show_hand()
        active_card = self.select_card_by_name()
        
        hand.remove(active_card)
        graveyard.container.append(active_card)
        active_card.location = 'yard'
        
        print('choose the player to target with {}: >'.format(active_card.name))
        player = player_dict.select_player()
        active_card.mod_player(player)
        
        print(player)
        
        
        
    def return_from_yard(self):
        pass
    

    def tile_check(self):
        """lets player select the atr he wants to challenge in self.Track and self.tier;
        if passsed applies lvl-up m/ to player."""
        
        global tile_dict
        challenge_tile = tile_dict[self.track][self.tier]
        
        while True:
            
            print(challenge_tile)
            atr = input('\nwhich atr to challange: ').capitalize()
            
            if atr not in challenge_tile:
                print('\nno match, try agian..')
            else:
                print('\natrb choice accepted.')
                break
        
        atr_int = getattr(self, atr).get_value()
        
        self.success_pool += D6().throw_dice(atr_int)
        
        if self.test_attribute(self.success_pool, challenge_tile[atr]):
            self.tier        += 1
            self.success_pool = 0
            print('\ngz, you are in tier', self.tier,' now.')
            self.level_up()
            

#p1.draw_card(5)
#p1.play_card()

#p1.track
#print(graveyard)
"""
print(p1)
type(tile_dict)
p1.select_track()
p1.track
p1.tile_check()
p1.success_pool
tile_dict['Track1'][1]

To Solve:
    success Pool doesnt consider from where it was accumulated...
    print the successpool score in addition to the accumulated current dice thrown result_sum
    
    """


# =============================================================================
# 
# about the Players -- managing the beast:
# =============================================================================

class PMS():
    
    def __init__(self, **kwargs):
        
        self.number        = False
        self.name          = []
        
        acceptable_kwargs = ['number', 'name']
        for k in kwargs.keys():
            if k in acceptable_kwargs:
                setattr(self, k, kwargs[k])
        
        self.no_of_players     = self.init_pms()
        self.player_dict       = self.create_player()
        self.player_dict_dummy = self.create_dummies()
        self.player_list       = self.create_player_list()
        self.player_list_dummy = self.create_player_list_dummies()
        
        
    def __str__(self):
        
        players = ''
        for name in self.player_dict:
            players += self.player_dict[name].__str__() + '\n'
            
        return players
    
    
    def init_pms(self):
        
        if not self.number:
            
            while True:
                
                no_of_players = input('how many players will be participating(max 5)? Give me a number! >')
                
                if no_of_players in ['1', '2', '3', '4', '5']:
                    
                    return int(no_of_players)
                    
                else:
                    print('you need to enter a number like: 1 or 2 up to 5')
                    
        else:
            return self.number
            
            
    def create_player(self):
        
        players = {}
        
        if not self.name:
            
            for i in range(self.no_of_players):
                name = input('name your player: >')
                players[name] = Player(name, 'can kill stuff', Wit(1), Stren(1), Dex(1), Intel(1))
            
        else:
            for name in self.name:
                players[name] = Player(name, 'can kill stuff', Wit(1), Stren(1), Dex(1), Intel(1))
            
        return players
    
    
    def create_dummies(self):
        
        player_dict = dict(self.player_dict)
        
        if len(self.player_dict) < 6:
            
            for dummy_players in range(len(self.player_dict), 5):
                name = 'dummy' + str(dummy_players + 1)
                player_dict[name] = Player(name, 'im not here, really', Wit(0), Stren(0), Dex(0), Intel(0))
                
        return player_dict
    
    
    def create_player_list(self):
        
        player_list = []
        
        for i in self.player_dict.keys():
            
            player_list.append(i)
            
        return player_list
        
    
    def create_player_list_dummies(self):
        
        player_list = []
        
        for i in self.player_dict_dummy.keys():
            
            player_list.append(i)
            
        return player_list
    
    
    def show_players(self):
        
        for name in self.player_dict:
            print(self.player_dict[name])
            
    
    def select_player(self, **kwargs):
        
        name = ''
        if kwargs == False:
            while True:
                print(self.player_list)
                name = input('pick a name: >')
                
                if name in self.player_list:
                    break
            
            return self.player_dict[name]
        
        else:
            print('else clause is talking now')
        
        
    
            
            
      
player_dict = PMS(number=2, name = ['frank', 'tank']); print(player_dict)
#player_dict.player_list
#player_dict.show_players()
#player_dict.select_player()
#print(player_dict.player_dict_dummy)
#print(player_dict.player_list_dummy)
#print(player_dict.player_dict.keys())
#player_dict.player_dict['frank']

#player_dict = PMS().create_player()
#print(player_dict.no_of_players)
#print(player_dict)
#print(player_dict.player_list)
#player_dict.show_players()
#player_dict.create_player()
#print(player_dict)
#player_dict
#print(player_dict)
#player_dict.show_players()
#type(player_dict)
#p = getattr(player_dict, 'player_dict')
#print(p['hank'])



# =============================================================================
# 
# all you need is functions to run:
# =============================================================================

def bind_players_to_vars():
    """Binds all active players to vars: p1 - p5 to access the player instances."""
    
    for player in player_dict.player_list_dummy:
        
        yield player_dict.player_dict_dummy[player]
            
        
p1, p2, p3, p4, p5 = bind_players_to_vars()
print(p3.Dex)


# =============================================================================
#     
# game logic - functional
# =============================================================================

if __name__ == '__main__':
    
    graveyard = Graveyard()
    deck = Deck()
    print(deck)
    board = Board(10, 1, 4)
    tile_dict = Board(10, 1, 4).dict_
    
    
    
    
 