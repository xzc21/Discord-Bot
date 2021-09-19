import random
list_of_cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,
                 1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
user_card_count = 0
comp_card_count = 0

user_playing = True
comp_playing = True
winner = ''
Ace_check = False
Ace_check_comp = False
playing = True



class Blackjack():
  global user_card_count
  
  def __init__(self,input, user1_cards, dealer_cards):
      uc_1 = user1_cards[0]
      #random.choice(list_of_cards)
      self.card_removal(uc_1)
      #user_card_count+=1
      
      uc_2 = user1_cards[1]
      #random.choice(list_of_cards)
      self.card_removal(uc_2)
      #user_card_count+=1
      
      cc_1 = dealer_cards[0]
      #random.choice(list_of_cards)
      self.card_removal(cc_1)
      #comp_card_count+=1
      
      cc_2 = dealer_cards[1]
      #random.choice(list_of_cards)
      self.card_removal(cc_2)
      #comp_card_count+=1
      
      self.user1cards = [uc_1, uc_2]
      self.dealercards = [cc_1, cc_2]
      
      print("Your Cards: ", self.user1cards)
      print("Computer's Cards: ", self.dealercards)
      #print(list_of_cards)
      self.comp_logic()
      
      while user_playing:
          uinput = input("Enter your move, either hold or hit: \n")
          if 'hit' in uinput:
              self.user_hit()
              
          if 'hold' in uinput:
              self.user_hold()
      while playing:
          if user_playing == False and comp_playing == False:
              self.winner_check()
              print("Your Cards: ", self.user1cards)
              print("Computer's Cards: ", self.dealercards)
              print("The winner is: ", winner)
              Ace_check_comp = False
              Ace_check = False
              break
        

  def comp_logic(self):
      global Ace_check_comp
      global comp_playing
      sum_comp = 0
            
      while comp_playing:
          for b in self.dealercards:
              if b == 1:
                  Ace_check_comp = True
              sum_comp+= b
              if Ace_check_comp:
                  sum_comp+=10
                  if sum_comp>21:
                      sum_comp-=10 
                  
          if sum_comp<=14:
              cc_new = random.choice(list_of_cards)
              self.card_removal(cc_new)
              self.dealercards.append(cc_new)
          elif sum_comp == 21:
              #print(self.dealercards)
              comp_playing = False
          elif sum_comp>14:
              #print(self.dealercards)
              comp_playing = False
          
      
      
  def user_hold(self):
      global user_playing
      user_playing = False
  
  def user_hit(self):
      #user_card_count+=1
      uc_new = random.choice(list_of_cards)
      self.card_removal(uc_new)
      self.user1cards.append(uc_new)
      print(self.user1cards)
      #print(list_of_cards)
      
  def card_removal(self, card):
      for i in list_of_cards:
          if card == i:
              list_of_cards.remove(i)
              break
  
  def winner_check(self):
      global winner
      global Ace_check
      global Ace_check_comp
      sum_user = 0
      sum_comp = 0
      for a in self.user1cards:
          if a == 1:
              Ace_check = True
          sum_user+= a
          if Ace_check:
              sum_user+=10
              if sum_user>21:
                  sum_user-=10
            
          
      for b in self.dealercards:
          if b == 1:
               Ace_check_comp = True
                  
          sum_comp+= b
          if Ace_check_comp:
              sum_comp+=10
              if sum_comp>21:
                  sum_comp-=10  
      
      if sum_user<=21 and sum_comp<=21:
          if sum_user>sum_comp or sum_user == 21:
              winner = "User"
          elif sum_user<sum_comp or sum_comp == 21:
              winner = "Computer"
          else:
              winner = "It's a tie!"
      elif sum_user>21 and sum_comp<=21:
          winner = "Computer"
      elif sum_user<=21 and sum_comp>21:
          winner = "User"
      else:
          winner = "It's a tie!"
          

#Blackjack()