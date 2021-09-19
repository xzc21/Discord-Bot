import random



class RPS_game ():
  def __init__(self, input):
    self.status=0
    self.message = ''
    if 'rock' in input:
      self.input = 1
    elif 'paper' in input:
      self.input = 2
    elif 'scissors' in input:
      self.input = 3

  def CompAction(self):
    # 1=Rock 2=Paper 3=Scissors
    self.action = random.randint(1,3)

    self.message += ("The computer played ")

    if self.action==1:
      self.message += ('***rock.***\n')
    elif self.action==2:
      self.message += ('***paper.***\n')
    elif self.action==3:
      self.message += ('***scissors.***\n')

  def Compare (self):
    if self.input==self.action:
      #tie
      self.status =0
    elif (self.input-self.action<0 and self.input-self.action !=-2)  or self.input-self.action==2:
      #User loses
      self.status = -1
    elif self.input-self.action>0 or self.input-self.action==-2:
      #User wins
      self.status = 1


  def messagetouser(self):
    if self.status==0:
      self.message += ('It\'s a tie!')
    elif self.status==-1:
      self.message += ('You lost!')
    elif self.status==1:
      self.message += ('You won! 🥳')
  def __call__(self):
    self.CompAction()
    self.Compare()
    self.messagetouser()
    return(self.message + " Type $ExitRPS to stop")
    




    