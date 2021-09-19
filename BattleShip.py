

class battleship ():
  def __init__(self):
    # 4 boards: player has one board to see their ships
    #           and another to see their hits
    #0 = empty square 1 = missed shot 2 = hit ship 3 = battleship
    self.p1board1 = [[0 for x in range(9)] for x in range(9)]
    self.p1board2 = [[0 for x in range(9)] for x in range(9)]
    self.p2board1 = [[0 for x in range(9)] for x in range(9)]
    self.p2board1 = [[0 for x in range(9)] for x in range(9)]
#     self.p1board1 = [[3, 3, 3, 3, 3, 0, 0, 0, 0],
# [3, 3, 3, 3, 3, 0, 0, 0, 0],
# [3, 0, 3, 3, 3, 0, 0, 0, 0],
# [3, 0, 0, 0, 3, 0, 0, 0, 0],
# [3, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     self.p1board2 = [[2, 2, 2, 2, 2, 0, 0, 0, 0],
# [2, 2, 2,2, 2, 0, 0, 0, 0],
# [2, 0, 2, 2, 2, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     self.p2board1 = [[3, 3, 3, 3, 3, 0, 0, 0, 0],
# [3, 3, 3, 3, 3, 0, 0, 0, 0],
# [3, 0, 3, 3, 3, 0, 0, 0, 0],
# [3, 0, 0, 0, 3, 0, 0, 0, 0],
# [3, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    self.p2board2 = [[0 for x in range(9)] for x in range(9)]
    self.ships_p1 = ['carrier', 
    'submarine',
    'destroyer', 
    'cruiser',
    'battleship']
    self.ships_p2 = ['carrier', 
    'submarine',
    'destroyer', 
    'cruiser',
    'battleship']
    # self.ships_p1=[]
    # self.ships_p2=[]
    self.turn = 0
    self.end = False

  def getCoords (self, coords):
    self.place = int(coords)
    y = int(self.place % 10)
    self.place-=y
    self.place/=10
    x = int(self.place)
    self.coords = [x,y]

  def setships(self, type, direction, coordinates, player):
    if player==1:
      if type in self.ships_p1:

        if 'carrier' in type:
          self.shiplength = 5
        elif 'submarine' in type:
          self.shiplength = 3
        elif 'destroyer' in type:
          self.shiplength = 2
        elif 'cruiser' in type:
          self.shiplength = 3
        elif 'battleship' in type:
          self.shiplength = 4

        self.getCoords(coordinates)
        if 'left' in direction:
          if self.coords[0]-self.shiplength<0:
            for x in range(0,self.shiplength):
              if self.p1board1[self.coords[1]][x] ==3:
                return 0
            for x in range(0,self.shiplength):
              self.p1board1[self.coords[1]][x] = 3
          else:
            for x in range(self.coords[0], self.coords[0]-self.shiplength,-1):
              if self.p1board1[self.coords[1]][x] ==3:
                return 0
            for x in range(self.coords[0], self.coords[0]-self.shiplength,-1):
              self.p1board1[self.coords[1]][x]=3
        if 'right' in direction:
          if self.coords[0]+self.shiplength>8:
            for x in range(8,8-self.shiplength,-1):
              if self.p1board1[self.coords[1]][x] ==3:
                return 0
            for x in range(8,8-self.shiplength,-1):
              self.p1board1[self.coords[1]][x] = 3
          else:
            for x in range(self.coords[0], self.coords[0]+self.shiplength):
              if self.p1board1[self.coords[1]][x] ==3:
                return 0
            for x in range(self.coords[0], self.coords[0]+self.shiplength):
              self.p1board1[self.coords[1]][x]=3
        if 'up' in direction:
          if self.coords[1]+self.shiplength>8:
            for y in range(8,8-self.shiplength,-1):
              if self.p1board1[y][self.coords[0]] ==3:
                return 0
            for y in range(8,8-self.shiplength,-1):
              self.p1board1[y][self.coords[0]] = 3
          else:
            for y in range(self.coords[1], self.coords[1]+self.shiplength):
              if self.p1board1[y][self.coords[0]] ==3:
                return 0
            for y in range(self.coords[1], self.coords[1]+self.shiplength):
              self.p1board1[y][self.coords[0]]=3
        if 'down' in direction:
          if self.coords[1]-self.shiplength<0:
            for y in range(0, self.shiplength):
              if self.p1board1[y][self.coords[0]] ==3:
                return 0
            for y in range(0, self.shiplength):
              self.p1board1[y][self.coords[0]] = 3
          else:
            for y in range(self.coords[1], self.coords[1]-self.shiplength,-1):
              if self.p1board1[y][self.coords[0]] ==3:
                return 0
            for y in range(self.coords[1], self.coords[1]-self.shiplength,-1):
              self.p1board1[y][self.coords[0]]=3
        self.ships_p1.remove(type)
    elif player == 2:
      if type in self.ships_p2:

        if 'carrier' in type:
          self.shiplength = 5
        elif 'submarine' in type:
          self.shiplength = 3
        elif 'destroyer' in type:
          self.shiplength = 2
        elif 'cruiser' in type:
          self.shiplength = 3
        elif 'battleship' in type:
          self.shiplength = 4

        self.getCoords(coordinates)


        if 'left' in direction:
          if self.coords[0]-self.shiplength<0:
            for x in range(0,self.shiplength):
                if self.p2board1[self.coords[1]][x] ==3:
                  return 0
            for x in range(0,self.shiplength):
              self.p2board1[self.coords[1]][x] = 3
          else:
            for x in range(self.coords[0], self.coords[0]-self.shiplength,-1):
              if self.p2board1[self.coords[1]][x] ==3:
                return 0
            for x in range(self.coords[0], self.coords[0]-self.shiplength,-1):
              self.p2board1[self.coords[1]][x]=3
        if 'right' in direction:
          if self.coords[0]+self.shiplength>8:
            for x in range(8,8-self.shiplength,-1):
              if self.p2board1[self.coords[1]][x] ==3:
                return 0
            for x in range(8,8-self.shiplength,-1):
              self.p2board1[self.coords[1]][x] = 3
          else:
            for x in range(self.coords[0], self.coords[0]+self.shiplength):
              if self.p2board1[self.coords[1]][x] ==3:
                return 0
            for x in range(self.coords[0], self.coords[0]+self.shiplength):
              self.p2board1[self.coords[1]][x]=3
        if 'up' in direction:
          if self.coords[1]+self.shiplength>8:
            for y in range(8,8-self.shiplength,-1):
              if self.p2board1[y][self.coords[0]] ==3:
                return 0
            for y in range(8,8-self.shiplength,-1):
              self.p2board1[y][self.coords[0]] = 3
          else:
            for y in range(self.coords[1], self.coords[1]+self.shiplength):
              if self.p2board1[y][self.coords[0]] ==3:
                return 0
            for y in range(self.coords[1], self.coords[1]+self.shiplength):
              self.p2board1[y][self.coords[0]]=3
        if 'down' in direction:
          if self.coords[1]-self.shiplength<0:
            for y in range(0, self.shiplength):
              if self.p2board1[y][self.coords[0]] ==3:
                return 0
            for y in range(0, self.shiplength):
              self.p2board1[y][self.coords[0]] = 3
          else:
            for y in range(self.coords[1], self.coords[1]-self.shiplength,-1):
              if self.p2board1[y][self.coords[0]] ==3:
                return 0
            for y in range(self.coords[1], self.coords[1]-self.shiplength,-1):
              self.p2board1[y][self.coords[0]]=3
        self.ships_p2.remove(type)

  def checkhit(self, shot):
    # game starts with player1 going first
    self.getCoords(shot)
    if self.turn % 2==0:
      if self.p2board1[self.coords[1]][self.coords[0]]==3:
        self.p1board2[self.coords[1]][self.coords[0]]=2
      elif self.p2board1[self.coords[1]][self.coords[0]]==0:
        self.p1board2[self.coords[1]][self.coords[0]]=1

    elif self.turn % 2==1:
      if self.p1board1[self.coords[1]][self.coords[0]]==3:
        self.p2board2[self.coords[1]][self.coords[0]]=2
      elif self.p1board1[self.coords[1]][self.coords[0]]==0:
        self.p2board2[self.coords[1]][self.coords[0]]=1

    self.turn+=1
  
  def check_gameover(self):
    numof2 = 0
    for i in range(9):
      for j in range(9):
        if self.p1board2[i][j]==2:
          numof2+=1
    if numof2 == 17:
      self.end = True
    numof2 = 0
    for i in range(9):
      for j in range(9):
        if self.p2board2[i][j]==2:
          numof2+=1
    if numof2 == 17:
      self.end = True
    
  def showboards(self, player):
    msg ='```'
    if player==1:
        msg +='your board (P1)\n'
        for i in range(9):
            msg+=str(self.p1board1[i])
            msg+='\n'
        msg +='hits board (P1)\n'
        for i in range(9):
            msg+=str(self.p1board2[i])
            msg+='\n'
    elif player==2:
        msg +='your board (P2)\n'
        for i in range(9):
            msg+=str(self.p2board1[i])
            msg+='\n'
                
        msg +='hits board (P2)\n'
        for i in range(9):
            msg+=str(self.p2board2[i])
            msg+='\n'
    msg+='```'
    return msg

  # def start (self):

  #   #add exceptions to each method call
  #   while self.ships_p1:
  #     #print('Set your ships P1')
  #     typeofship = input("Type?")
  #     direction = input('Direction?')
  #     coords = input('Coords?')
  #     if self.setships(typeofship, direction, coords, 1)==0:
  #       #print("Overlapping ships enter other coords")
  #       continue
  #     self.showboards(1)
  #   while self.ships_p2:
  #     typeofship = input("Type?")
  #     direction = input('Direction?')
  #     coords = input('Coords?')
  #     if self.setships(typeofship, direction, coords, 2)==0:
  #       #print("Overlapping ships enter other coords")
  #       continue
  #     self.showboards(2)

  #   while self.end == False:
  #     if self.turn%2==0:
  #       self.showboards(1)
  #       #print('Enter Shot P1')
  #       shot = input()
  #     elif self.turn%2==1:
  #       self.showboards(2)
  #       #print('Enter Shot P2')
  #       shot = input()
  #     self.checkhit(shot)
  #     self.check_gameover()
  #   #print('Game Over')


    
    


  
    
    
    


