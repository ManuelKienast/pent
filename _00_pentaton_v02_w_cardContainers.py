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
tile_dict = {}

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
        
    def getValue(self):
        return int(self.value)
    
        
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
    



"""
test = Wit(5)
print(test)
test.getValue()
test.increase_value(2)
test.getValue()
"""

# =============================================================================
#     
# playing with the Player:
# =============================================================================

class Player():
    """the player base class."""
    
    def __init__(self, name, text, Wit, Stren, Dex, Intel, ):
        self.name = name
        self.text = text
        self.Wit = Wit
        self.Stren = Stren
        self.Dex = Dex
        self.Intel = Intel
        self.atr_tup = ('Wit', 'Stren', 'Dex', 'Intel')
        self.atr_self_tup = (self.Wit, self.Stren, self.Dex, self.Intel)
        self.track = 0
        self.tier_complete = 0
        self.hand = []
        
    
    def __str__(self):
        return "\nPlayer Name: {} \n{}'s Wit: {} \n{}'s Stren: {} \n{}'s Dex: {}\
                \n{}'s Intel: {} {} Cards: {}".format\
                (self.name, self.name, self.Wit, self.name, self.Stren, self.name, self.Dex,\
                 self.name, self.Intel, self.name, self.hand)
    
    
    def test_attribute(self, attribute, test_value):
        """tests attribute, the self.atr against a test_value."""
        
        global tile_dict
        
        atr = attribute
        
        if atr >= test_value:
            print('you passed')
            return True
        else:
            print('you failed')
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
        
        if atr == 'Wit' and self.test_attribute(self.Wit.getValue(), tier[atr]) == True:
            self.tier_complete += 1; print('\ngz, you are in tier', self.tier_complete,' now.')
            self.level_up()
        if atr == 'Stren' and self.test_attribute(self.Stren.getValue(), tier[atr]) == True:
            self.tier_complete += 1; print('\ngz, you are in tier', self.tier_complete,' now.')
            self.level_up()
        if atr == 'Dex' and self.test_attribute(self.Dex.getValue(), tier[atr]) == True:
            self.tier_complete += 1; print('\ngz, you are in tier', self.tier_complete,' now.')
            self.level_up()
        if atr == 'Intel' and self.test_attribute(self.Intel.getValue(), tier[atr]) == True:
            self.tier_complete += 1; print('\ngz, you are in tier', self.tier_complete,' now.')
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
                if up == 'Wit':
                    self.Wit.increase_value(1); print('\ngz, your new self:\n', self); break
                if up == 'Stren':
                    self.Stren.increase_value(1); print('\ngz, your new self:\n', self); break
                if up == 'Dex':
                    self.Dex.increase_value(1); print('\ngz, your new self:\n', self); break
                if up == 'Intel':
                    self.Intel.increase_value(1); print('\ngz, your new self:\n', self); break
       
        
        
    def draw_card(self, amount):
        
        i = 0
        while i <= amount:
            try:
                rand_index = random.randrange(0, deck.deck_size())
                drawn_card = deck.deck[rand_index]
                drawn_card.location = 'hand'
                self.hand.append(drawn_card)
                deck.deck.pop(rand_index)
                print(self.hand)
                i += 1
            except ValueError:
                print('pile exhausted, shuffle yard back to deck\n raised by draw_card.')
                break
    
    def discard_card(self):
        pass    
        
    
    def play_card(self):
        pass
        
    
    def return_from_yard(self):
        pass
           
"""
drizzt = Player('Drizzt', 'can kill stuff', Wit(21), Stren(5), Dex(5), Intel(5))
print(drizzt)
drizzt.Dex.increase_value(15)
print(drizzt)
drizzt.Dex.getValue()
drizzt.test_attribute(drizzt.Dex.getValue(), 11)
type(drizzt.Dex)
drizzt.tile_check()
drizzt.Wit.ability()
"""

drizzt = Player('Drizzt', 'can kill stuff', Wit(21), Stren(5), Dex(5), Intel(5))
print(drizzt)

# =============================================================================
# 
# just read the fucking card:
# =============================================================================

class Card():
    """description of Card; with M/ for testing im card can target a player and 
    applying the card effect depending on temp/perm mod effect"""
    
    
    def __init__(self, name, text, atr, atri_mod, temp):
        self.name = name
        self.text = text
        self.atr = atr
        self.atri_mod = atri_mod
        self.temp = temp
        self.container = []
        
        
        
    def __str__(self):
        return '\nCard name: {}\nText: {}\nModifies: {}\nBy: {}\nTemp: {}'.format\
                (self.name, self.text, self.atr, self.atri_mod, self.temp)
                
    
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
                
                if self.atr == 'Stren' and not player.Stren.getValue() + self.atri_mod < 0:
                    player.Stren.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Stren', Stren(0))
                
                if self.atr == 'Dex' and not player.Dex.getValue() + self.atri_mod < 0:
                    player.Dex.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Dex', Dex(0))
                
                if self.atr == 'Wit' and not player.Wit.getValue() + self.atri_mod < 0:
                    player.Wit.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Wit', Wit(0))
                
                if self.atr == 'Intel' and not player.Wit.getValue() + self.atri_mod < 0:
                    player.Wit.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Wit', Wit(0))
                
            
            else:    
                
                if self.atr == 'Stren' and not player.Stren.getValue() + self.atri_mod < 0:
                    player.Stren.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Stren', Stren(0))
                
                if self.atr == 'Dex' and not player.Dex.getValue() + self.atri_mod < 0:
                    player.Dex.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Dex', Dex(0))
                
                if self.atr == 'Wit' and not player.Wit.getValue() + self.atri_mod < 0:
                    player.Wit.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Wit', Wit(0))
                
                if self.atr == 'Intel' and not player.Wit.getValue() + self.atri_mod < 0:
                    player.Wit.increase_value(self.atri_mod)
                else:
                    setattr(player, 'Wit', Wit(0))
        else: 
            print('it is not a moddable target.')
                
        
"""   
testCard = Card('Strength Potion', 'adds +2 to your strength', 'Stren', 10, True)
print(testCard)
a = testCard.test_card()
print(a)

testCard.mod_player(drizzt)
print(drizzt)
#print(drizzt.Stren.getValue)
#print(dir(Player))
"""

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
        return result
    
    
    def initialize_container(self):
        
        if self.name == 'deck':
        
            file_path = 'pent_resc\\cards.txt'
            deck_list = []            
            fopen = open(file_path, 'r', encoding = 'utf-8')
            
            for line in fopen:
                
                print(line)
                text_list = line.split(', ')
                print(text_list)
                list_format = [text_list[0], text_list[1], text_list[2], int(text_list[3]), bool(text_list[4])]
                print(list_format)
                print('\n')
                deck_list.append(Card(*list_format))
                
            fopen.close()
            print(deck_list)
            return deck_list
        
        
    def container_size(self):
        
        if len(self.container) > 0:
            return len(self.container)
        else:
            print('your pile is empty.')







class Deck(Card_container):
    
    def __init__(self):
        
        super(type(self)).__init__()
        self.name      = 'deck'
        self.container = self.initialize_container()
        self.size      = self.container_size()
        
        
        
deck = Deck()
type(deck)    
print(deck)
print(deck.container)
deck.size

class Hand(Card_container):
    
    def __init__(self):
        
        self.name      = 'hand'
        self.size      = self.container_size()
        self.container = []
        super().__init__()

    

class Graveyard(Card_container):
    
    def __init__(self):
        
        self.name      = 'yard'
        self.size      = self.container_size()
        self.container = []
        super().__init__()
    
    def schuffle_to_deck():
        pass




# =============================================================================
#     
# game logic - functional
# =============================================================================

if __name__ == '__main__':
    
    tile_dict = Board(10, 1, 4).dict_
    for i in tile_dict['Tracks']:
        print('\n', i)
        
        
'''
class C_test():
    
    def __init__(self):
        self.container = self.initialize_container()
        
   
    def __str__(self):
        
        result = ""
        for c in self.container:
            result += c.__str__() + '\n'
        return result
    
    
    def initialize_container(self):
    
            file_path = 'pent_resc/cards.txt'
            deck_list = []            
            fopen = open(file_path, 'r')
            
            for line in fopen:
                
                text_list = line.split(', ')
                list_format = [text_list[0], text_list[1], text_list[2], int(text_list[3]), bool(text_list[4])]
                deck_list.append(Card(*list_format))
                
            fopen.close()
            return deck_list

test = C_test()
test.initialize_container()
print(test)
#test2 = C_test()
#print(test2)
#test2.show_cards()
'''