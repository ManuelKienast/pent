# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:17:23 2018

@author: Manuel

the pentaton logic go around II

"""


import random

random.seed(0)
print(random.getrandbits(5))


# =============================================================================
# 
# Variables
# =============================================================================

# one board track with all tiles from start to finish


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
        self.dict_   = {'Tracks': [self.track1, self.track2, self.track3, self.track4, self.track5]}

        
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
        
        for i in range(self.length):
            
            tile_dict[i] = self.create_tile(var_min, var_max)
            var_min += 3
            var_max += 3
            
        print('tile_track created.')
        return tile_dict
    


#    def __str__(self):
#        return '\n'.join(str(i) for i in self.dict_['Tracks'])
#    
#    def __str__(self):
#        #return '{}'.format(i) (for board.dict_['Tracks'][i] in board.dict_)
#        return ','.join("{}\n".format(i) for i in self.dict_['Tracks'])
#        
#    def __str__(self):
#        return ('{}\n{}\n{}\n{}\n{}'.format(self.track1, self.track2, self.track3, self.track4, self.track5))

"""
board = Board(10, 1, 4)
print(board.track1, board.track2)
track1 = Board(10, 1, 4).track1
print(track1)
track2 = Board(10, 1, 4).track2
print(track2)
print(board.dict_['Tracks'][3])
print(board)

tr_dict = board.dict_

for i in tr_dict['Tracks']:
    print('\n\n', i)
"""    

# =============================================================================
# 
# about the Players -- managing the beast:
# =============================================================================

class PMS():
    
    def __init__(self):
        self.player_dict = {}
        
    
    def __str__(self):
        return self.player_dict.items()
    
    
    def create_player(self):
        
        name = input('name your player: >')
        self.player_dict[name] = Player(name, 'can kill stuff', Wit(20), Stren(5), Dex(5), Intel(5))
    


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
    



'''
test = Wit(5)
print(test)
type(test)
test.get_value()
test.increase_value(2)
test.get_value()
test.set_value(-5)
type(test)
'''
# =============================================================================
# 
# die würfel sind gefallen:
# =============================================================================

class Dice():
    
    
    def throw_dice(self, d6=1, d4=0):
        
        result_sum = 0
        
        for throws in range(d6):
            result = random.randrange(1,7)
            print(result)
            result_sum += result
            print(result_sum)
                
        
        if d4 != 0:
            
            for throws in range(d4):
                result = random.randrange(1,5)
                print(result)
                result_sum += result
                print(result_sum)
                
        return result_sum
            
            
#print(Dice().throw_dice(10))

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
                
'''try passing the player with the actual player class object from dict reference 
created during player instanciation, not with its instance aka drizzt
or use the Player().name class attribute

also need that dict for player managment which needs to happen during instanciation pref 
as a dict, where player name is the key the object is referenced'''

deck = Deck()
drizzt = Player('drizzt', 'can kill stuff', Wit(21), Stren(5), Dex(5), Intel(5))
drizzt.draw_card(5)
active_Card = drizzt.select_card_by_name()
input_ = input('player name: >')
active_Card.mod_player(drizzt); print(drizzt)

                    
#                if self.atr == 'Stren' and not player.Stren.get_value() + self.atri_mod < 0:
#                    player.Stren.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Stren', Stren(0))
#                
#                if self.atr == 'Dex' and not player.Dex.get_value() + self.atri_mod < 0:
#                    player.Dex.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Dex', Dex(0))
#                
#                if self.atr == 'Wit' and not player.Wit.get_value() + self.atri_mod < 0:
#                    player.Wit.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Wit', Wit(0))
#                
#                if self.atr == 'Intel' and not player.Wit.get_value() + self.atri_mod < 0:
#                    player.Wit.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Wit', Wit(0))
#                
#            
#            else:    
#                
#                if self.atr == 'Stren' and not player.Stren.get_value() + self.atri_mod < 0:
#                    player.Stren.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Stren', Stren(0))
#                
#                if self.atr == 'Dex' and not player.Dex.get_value() + self.atri_mod < 0:
#                    player.Dex.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Dex', Dex(0))
#                
#                if self.atr == 'Wit' and not player.Wit.get_value() + self.atri_mod < 0:
#                    player.Wit.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Wit', Wit(0))
#                
#                if self.atr == 'Intel' and not player.Wit.get_value() + self.atri_mod < 0:
#                    player.Wit.increase_value(self.atri_mod)
#                else:
#                    setattr(player, 'Wit', Wit(0))
#        else: 
#            print('it is not a moddable target.')
                


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
                
            print('\nDeck created:\n', deck.__str__())
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
        
"""        
print("*" * 40)
deck = Deck()
type(deck)    
print(deck)
print(deck.container)
print("*" * 40)

for card in deck.container:
    if card.name == 'Dexterity Potion':
        active_card = card
        print(active_card)
        
card = [card for card in deck.container if card.name == 'Dexterity Potion']
print(card)
index = next(i for i, card in enumerate(deck.container) if card.name == 'Strength Potion')
print(deck.container[index])
"""


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
        self.tier_complete = 0
        self.container     = Hand()
        self.hand_size     = self.container.container_size()
       
    
    def __str__(self):
        return "\nPlayer Name: {} \n{}'s Wit  : {} \n{}'s Stren: {} \n{}'s Dex  : {}\
                \n{}'s Intel: {} \n{}'s Cards: \n{}".format\
                (self.name, self.name, self.Wit, self.name, self.Stren, self.name, self.Dex,\
                 self.name, self.Intel, self.name, self.container.__str__())
    
    
    def test_attribute(self, atr, test_value):
        """tests attribute, the self.atr against a test_value."""
        
        global tile_dict
        
        if atr >= test_value:
            print('you passed your check.')
            return True
        else:
            print('you failed your check.')
            return False


    def tile_check(self):
        """lets player select the atr he wants to challenge in self.Track and self.tier;
        if passsed applies lvl-up m/ to player."""
        
        tier = tile_dict['Tracks'][self.track][self.tier_complete]
        
        while True:
            
            print(tier)
            atr = input('\nwhich atr to challange: ').capitalize()
            
            if atr not in tier:
                print('\nno match, try agian..')
            else:
                print('\natrb choice accepted.')
                break
        
        atr_int = getattr(self, atr).get_value()
        
        if self.test_attribute(atr_int, tier[atr]):
            self.tier_complete += 1
            print('\ngz, you are in tier', self.tier_complete,' now.')
            self.level_up()
            
            
    def level_up(self):
        """after a succesfull self.tile_check() it allows the player to increase one
        of his atris by +1 and increases self.tier_complete."""
        
        print('\nyour current stats:  Wit: {}  Stren: {}  Dex: {}  Intel: {}.'.format\
                                     (self.Wit, self.Stren, self.Dex, self.Intel))
        
        while True:
            
            up = input('\nwhich atribute do you wanna level up(+1)? ').capitalize()
            
            if up not in self.atr_tup:
                print('\nplease retype, couldnt understand your input.')
            
            else:
                new_value = getattr(self, up).get_value() +1
                setattr(self, up, new_value)
                print(self)
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
        
        hand       = self.container.container
        
        self.show_hand()
        active_card = self.select_card_by_name()
        
        hand.remove(active_card)
        graveyard.container.append(active_card)
        active_card.location = 'yard'
        
        player = input('choose the player to target with {}: >'.format(active_card.name))
        active_card.mod_player(player)
        
        print('SCHALALALALLALLALALALLALA')
        
        
        
    def return_from_yard(self):
        pass
    
    
#    def dice_pool(self):
#        
#        pool = ()
#        
#        if self.luck <= 2:
#            pool = ()
    
'''
drizzt = Player('Drizzt', 'can kill stuff', Wit(21), Stren(5), Dex(5), Intel(5))
#print(drizzt)
#drizzt.Dex.increase_value(15)
#print(drizzt)
#drizzt.Dex.get_value()
#drizzt.test_attribute(drizzt.Dex.get_value(), 11)
#drizzt.tile_check()
#type(drizzt.Dex)
#drizzt.tile_check()
#drizzt.Wit.ability()
#deck.container_size()
#print(drizzt)
drizzt.discard_card(5)
#print(graveyard)
#print(deck)
drizzt.draw_card(1)
#drizzt.show_hand()
drizzt.play_card()
#print(graveyard)

print(drizzt)
'''
# =============================================================================
#     
# game logic - functional
# =============================================================================

if __name__ == '__main__':
    
    tile_dict = Board(10, 1, 4).dict_
    for i in tile_dict['Tracks']:
        print('\n', i)
    
    
    graveyard = Graveyard()
    deck = Deck()
 