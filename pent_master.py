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



# =============================================================================
# 
# about a BOARD:
# =============================================================================

class Board:
    """ the board class, builds the playing field w/ all tracks. """
    
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
        """ selects 2 random atributes for the tile and sets its min_val and max_val."""
        
        pos = ['Wit', 'Stren', 'Dex', 'Intel']
        pos = random.sample(pos, 2)
        tile_value = {}
        for i in pos:
            tile_value[i] = random.randrange(min_val, max_val+1)
        return tile_value

    
    def build_track(self):
        """ builds a track of tiles, incrementing the min & max vals. """
        
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
print(td)
td = Board(10,1,4)
print(td.dict_)

"""

# =============================================================================
# 
# concerning ATTRIBUTES:
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
# die WWÜRFEL sind gefallen:
# =============================================================================

class Dice():
    """ the dice class w/ rolling dice functinality. """
    
   
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
    """ the D6 entity. """
    
    def __init__(self):
        super().__init__()
        #super(type(self))
        self.sides = 6
        
        
class D4(Dice):
    """ the D4 entity. """
    
    def __init__(self):
        super().__init__()
        #super(type(self))
        self.sides = 4

'''        
D6().throw_dice(3)
'''

# =============================================================================
# 
# just read the fucking CARD:
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
                
'''
deck = Deck()
p1.draw_card(5)
active_Card = p1.select_card_by_name()
input_ = input('player name: >')
active_Card.mod_player(p1); print(p1)
p1.play_card()
'''

# =============================================================================
# 
# all the cards are in CONTAINERs:
# =============================================================================

class Card_container:
    """ base class of card container with functionalities. """
    
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
        """ populates the containers, for deck loads abd reads the card file. """
        
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
        """ counts the cards in the container. """
        
        if self.container:
            return len(self.container)
        else:
            print('your pile is empty.')


class Deck(Card_container):
    """ sets the deck card container. """
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'deck'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

class Hand(Card_container):
    """ sets the players hand card-container. """
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'hand'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

class Graveyard(Card_container):
    """ sets the graveyard card container. """
    
    def __init__(self):
        
        super(type(self))
        self.name      = 'yard'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        

# =============================================================================
#     
# playing with the PLAYER:
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
        self.track         = -1
        self.tier          = 1
        self.container     = Hand()
        self.hand_size     = self.container.container_size()
        self.card_playable = 'no'
        self.active_turn   = 'no'
        self.success_pool  = 0
        self.atr_challange = False
        self.tile_checked  = False
       
    
    
    def __str__(self):
        return "\nPlayer Name: {} \n{}'s Wit  : {} \n{}'s Stren: {} \n{}'s Dex  : {}\
                \n{}'s Intel: {} \n{}'s Track: {} \n{}'s Cards: \n{}".format\
                (self.name, self.name, self.Wit, self.name, self.Stren, self.name, self.Dex,\
                 self.name, self.Intel, self.name, self.track, self.name, self.container.__str__())
    
    

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
        """ prints the hand of player. """
        
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
                    
            
            active_card = hand[active_card_index]
            print(active_card)
            return active_card
    
    
    def draw_card(self, amount):
        """draws an amount of cards from the deck. """
        
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
        """ play card from hand after selecting card and target player. """
        
        
        if self.container.container:
            hand = self.container.container
            
            active_card = self.select_card_by_name()
            
            hand.remove(active_card)
            graveyard.container.append(active_card)
            active_card.location = 'yard'
            
            print('choose the player to target with {}: >'.format(active_card.name))
            player = player_dict.select_player()
            active_card.mod_player(player)
            
            print(player)
            
            while True:
                allowed_cmds_play_card = ('Yes', 'No')
                input_ = input('Do you want to play another card? Yes or No: >').capitalize()
                if input_ in allowed_cmds_play_card:
                    break
                else:
                    print('I dont understand your input, plz repeat.')
                
            if input_ == 'Yes':
                self.play_card()
            else:
                print('will be asking other players if they want to respond..')
        
        else:
            print('You dont have any cards to play..')
    
    
    def return_from_yard(self):
        pass
    
    
    def show_active_tile(self):
        """ returns the current tile to challange and the complete track """
        
        challenge_tile = tile_dict[self.track][self.tier]
        print('\n the track you are on: \n', tile_dict[self.track], '\nso far you have beaten ', self.tier -1, 'tiles.')
        print('\n the Tile you need to beat: \n', challenge_tile)
        
        
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
        
        if self.success_pool and not atr == self.atr_challange:
            self.success_pool = 0
        
        self.atr_challange = atr
        
        for i in D6().throw_dice(atr_int):
            self.success_pool += i 
            
        print('this go around you accumulated', self.success_pool, 'points')
        
        if self.test_attribute(self.success_pool, challenge_tile[atr]):
            self.tier        += 1
            self.success_pool = 0
            print('\ngz, you are in tier', self.tier,' now.')
            self.level_up()
            
        

'''
print(p1)
type(tile_dict)
p1.select_track()
p1.track
p1.tile_check()
p1.success_pool
tile_dict['Track1'][1]

print(tile_dict)

frank
print(player_dict)
frank = player_dict.select_player()
frank.tile_check()
print(frank)
frank.select_track()
'''

# =============================================================================
# 
# about the Players -- MANAGING the beast:
# =============================================================================

class PMS():
    """ player managment system, keeps a record of all players and their turn order. """
    
    def __init__(self, **kwargs_PMS):
        
        self.number        = False
        self.name          = []
        
        acceptable_kwargs = ['number', 'name']
        for k in kwargs_PMS.keys():
            if k in acceptable_kwargs:
                setattr(self, k, kwargs_PMS[k])
        
        self.no_of_players     = self.init_pms()
        self.player_dict       = self.create_player()
        self.player_dict_dummy = self.create_dummies()
        self.player_class_list = self.create_player_class_list()
        self.player_list       = self.create_player_list()
        self.player_list_dummy = self.create_player_list_dummies()
         
        
    
    def __str__(self):
        
        players = ''
        for name in self.player_dict:
            players += self.player_dict[name].__str__() + '\n'
            
        return players
    
    
    def init_pms(self):
        """ sets the number of participating players --> input. """
        
        if not self.number:
            
            while True:
                
                no_of_players = input('how many players will be participating(max 5)? Give me a number! >')
                
                if no_of_players in ['1', '2', '3', '4', '5']:
                    
                    #no_of_players = no_of_players        
                    return int(no_of_players)
                    
                else:
                    print('you need to enter a number like: 1 or 2 up to 5')
                    
        else:
            #no_of_players = no_of_players
            return self.number
        
        
            
    def select_track(self, players, name):
        """ sets the track a player will be playing on. """
    
        print(players[name])
        print('\n\n Hej,', self.name, '\n You can choose one of the following tracks: ')
    
        for count, track in enumerate(board.dict_, 1):
            if str(count) in available_tracks:
                print(' \n', track, ':\n', board.dict_[track])
        
        while True:
            track_selected = input('Choose the track you want to challenge. Give me a number 1-5: >')
            if track_selected in available_tracks:
                break
        
        available_tracks.remove(track_selected)
        board_dict_key = 'Track' + track_selected
        print('you chose track number: ', track_selected, board.dict_[board_dict_key])
        
        print(players[name])
        
        setattr(players[name], 'track', board_dict_key)
        
        return players
        
        
        
            
    def create_player(self):
        """ creates the player instances for all participating players. """
        
        players = {}
        
        if not self.name:
            
            for i in range(self.no_of_players):
                name = input('name your player: >')
                players[name] = Player(name, 'can kill stuff', Wit(1), Stren(1), Dex(1), Intel(1))
                print(players[name])
                players = self.select_track(players, name)
                print(players[name])
            
        else:
            for name in self.name:
                players[name] = Player(name, 'can kill stuff', Wit(1), Stren(1), Dex(1), Intel(1))
                print(players[name])
                players = self.select_track(players, name)
                print(players[name])
        return players
    
    
    def create_dummies(self):
        """ creates the dummy versions for 5 - actual players. """
        
        player_dict = dict(self.player_dict)
        
        if len(self.player_dict) < 6:
            
            for dummy_players in range(len(self.player_dict), 5):
                name = 'dummy' + str(dummy_players + 1)
                player_dict[name] = Player(name, 'im not here, really', Wit(0), Stren(0), Dex(0), Intel(0))
                
        return player_dict
    
    
    def create_player_class_list(self):
        
        player_class_list = []
        
        for player in self.player_dict.keys():
            player_class_list.append(self.player_dict[player])
            
        return player_class_list
    
    
    def create_player_list(self):
        """ creates the list of all actual players. """
        
        player_list = []
        
        for i in self.player_dict.keys():
            
            player_list.append(i)
            
        return player_list
        
    
    def create_player_list_dummies(self):
        """ creates the dummy list filled up to 5 in additon to the actual players. """
        
        player_list = []
        
        for i in self.player_dict_dummy.keys():
            
            player_list.append(i)
            
        return player_list
    
    
    def show_players(self):
        """ returns all actual participating players. """
        
        for name in self.player_dict:
            print(self.player_dict[name])
            
    
    def select_player(self, **kwargs_select_player):
        """ enables selection of active player. """
        
        
        if not kwargs_select_player.keys():
            while True:
                print(self.player_list)
                name = input('pick a name: >')
                
                if name in self.player_list:
                    break
            
            return self.player_dict[name]
        
        else:
            selected_players = []
            
            for name in kwargs_select_player.values():
                selected_players.append(self.player_dict[name])
            
            return selected_players
                
        
'''
player_dict = PMS(number=2, name = ['frank', 'tank']); print(player_dict)
player_dict.select_player(name=['tank','frank'])

player_dict.player_dict['frank'].active_turn
print(available_tracks)

'''

# =============================================================================
# 
# time walking - the story about TURNS:
# =============================================================================

class Turn:
    
    def __init__(self):
        
        self.turn_no         = 0
        self.player_active   = ''
        self.player_position = -1
        self.card_turn       = False
    

    
    def loop_player_list(self):
        """ loops trough all active players, resets to [0] if end is reached."""
        
        if self.player_position < player_dict.no_of_players -1:
            self.player_position += 1
            
        else:
            self.player_position = 0
    
    
    def turn_play_cards(self):
        pass #build the list of players on turn, ask to play card if yes call player play card
    
    
    def turn_start(self):
        """ starts the turn by selecting the active player. """
        
        if not self.player_active:
            self.player_active = player_dict.player_class_list[0]
            self.player_position = 0
            
        self.player_active.active_turn = 'yes'
        self.player_active.tile_checked = False
        
        try:
            self.player_active.draw_card((4 - self.player_active.container.container_size()))
        except TypeError:
            self.player_active.draw_card(4)
            
        self.turn_options()
            
    
    def turn_end(self):
        """ implements end of turn behavior, activating the next active player, dicarading cards etc.."""
        
        self.loop_player_list()
            
        self.player_active = player_dict.player_class_list[self.player_position]
        
        self.turn_start()
        
        
        
    def end_game(self):
        """ Ends all """
        print('Until the next time, bye.')
        
        
        
    def turn_options(self):
        """ the main menu, keeps the turn functionalities. """
        
        allowed_cmds = ('1', '2', '3', '4', '5', '6', 'x', 'Q')
        turn_menu = '\nHey ' + self.player_active.name + """:\nIt's your turn now.
        You can:
            
            1: Show the current tile you need to beat.
            2: Activate your special abilities.
            3: Look at your hand.
            4: Play cards from your hand.
            5: Make your challenge attempt.
            6: End your turn.
            
            x, Q : End the whole game.
            
            Choose number 1-4 - x,Q(to end all): >"""
            
        while True:
            input_ = input(turn_menu)
            
            if input_ in allowed_cmds:
                break
            else:
                print('You need to choose a number: 1-4. plz repeat.')
        
        # show the challenge tile
        if input_ == '1':
            
            self.player_active.show_active_tile()
            
            self.turn_options()
            
            
        # special ability
        if input_ == '2':
            self.turn_options()
            
        # show players hand    
        if input_ == '3':
            self.player_active.show_hand()
            
            self.turn_options()
            
        # play cards    
        if input_ == '4':
            if self.player_active.container.container_size() <= 0:
                print('you currently can\'t play any cards, you have none.')
            else:
                self.player_active.play_card()
            
            self.turn_options()
            
        # challenge attempt            
        if input_ == '5':
            if self.player_active.tile_checked == True:
                print('you already tried it this turn. Don\'t try to cheat.')
            else:
                self.player_active.tile_check()
            
            self.player_active.tile_checked = True                
            turn.turn_options()
            
        # end turn    
        if input_ == '6':
            self.turn_end()
            
        # end game    
        if input_ == 'x' or input_ == 'Q':
            print('until the next time.')
            self.end_game()
        
'''     
turn = Turn()
turn.turn_start()
print(turn.player_active)
turn.turn_end()  
print(turn.player_active)
print(player_dict)
'''

# =============================================================================
# 
# GAME on:
# =============================================================================

class Game:
    """ putting it all together, impementing the final logic."""
    
    def __init__(self):
        self.name = 'im game'
        self.board = Board(10, 1, 4)
        self.player_dict = PMS(number=2, name = ['frank', 'tank']); print(player_dict)
        self.deck = Deck()
        self.graveyard = Graveyard()
        self.turn = Turn()
    
    global board, player_dict, deck, graveyard
    
#    board = Board(10, 1, 4)
#    #player_dict = PMS()
#    player_dict = PMS(number=2, name = ['frank', 'tank']); print(player_dict)
#    deck = Deck()
#    graveyard = Graveyard()
#    turn = Turn()
    

# =============================================================================
#     
# game logic - functional
# =============================================================================

if __name__ == '__main__':
    
    available_tracks = ['1', '2', '3', '4', '5']
    board = Board(10, 1, 4)
    tile_dict = board.dict_
    #player_dict = PMS(number=2, name = ['frank', 'tank']); print(player_dict)
    #no_of_players = PMS.init_pms()
    player_dict = PMS()
    deck = Deck()
    graveyard = Graveyard()
    turn = Turn()
    
    turn.turn_start()
    
    
#print(board.)
#print(player_dict.player_dict['tank'])
#print(deck)    
#
def test(**kwargs):
    
    if kwargs.keys():
        print(kwargs.items())
    else:
        print('nothing')
        
test()
    
    
    