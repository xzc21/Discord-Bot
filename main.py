

import os
import discord
import requests
import RockPaperScissors as rps
import BattleShip as bs
import TicTacToe as ttt
#import BlackJack as bj
# list_of_cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,
                #  1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]


rpsStatus = 0
tttStatus = 0
BSstatus = 0
bjstatus = 0
tttGame = ttt.TicTacToe()


bsGame = bs.battleship()
bsTypeStatus = 0
bsDirectionStatus = 0
bsCoordinateStatus = 0
bsPlayerStatus = 0
bsType = ''
bsDirection = ''
bsCoordinates = ''
bsPlayer = ''
bsPlayers = []
channel = 888638986413809674


#https://discordpy.readthedocs.io/en/stable/quickstart.html



name = "GAME BOT"
TOKEN = os.environ['token']



#pfp
pfp_path = "pfp_temp.png"
fp = open(pfp_path, 'rb')
pfp = fp.read()



client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Type $help for usage!"))
    await client.user.edit(username=name)
    #await bot.user.edit(avatar=pfp) to change pfp but you have to comment it after because it changes pfp everytime

@client.event
async def on_message(message):

    global rpsStatus
    global tttStatus
    global tttGame
    global bsGame
    global BSstatus
    global bsTypeStatus
    global bsDirectionStatus 
    global bsCoordinateStatus
    global bsPlayerStatus
    global bsType
    global bsDirection
    global bsCoordinates
    global bsPlayer
    global bsPlayers
    global channel
    global bjstatus 

    if message.author == client.user:
        return

    if message.content.startswith('$test'):
      await message.author.send("Test")

    if message.content.startswith('$help'): #embed stuff https://cog-creators.github.io/discord-embed-sandbox/
      embed=discord.Embed(title="Help Command", color=0x264af4)
      embed.add_field(name="Games", value="`$PlayRPS`\n`$PlayTTT \n$PlayBS`", inline=True)
      await message.channel.send(embed=embed)
  

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

      #async def on_message(message):
    if message.content.startswith('$rock') and rpsStatus == 1:
        await message.channel.send('{} '.format(message.author.mention) + rps.RPS_game('rock')())
        #await message.channel.send('{}'.format(message.author.mention))
        #test = 0
    elif message.content.startswith('$paper') and rpsStatus == 1:
        await message.channel.send('{} '.format(message.author.mention) + rps.RPS_game('paper')())
        #test = 0
    elif message.content.startswith('$scissors') and rpsStatus == 1:
        await message.channel.send('{} '.format(message.author.mention) + rps.RPS_game('scissors')())
        #test = 0
    
    if message.content.startswith('$PlayRPS'):
      await message.channel.send("Use $ followed by either rock, paper or scissors. eg: $rock \nBTW everyone can play! ")
      rpsStatus = 1
    
    if message.content.startswith('$ExitRPS'):
      await message.channel.send("Game Stopped, bye!")
      rpsStatus = 0
    

    
    if message.content.startswith('$PlayBS'):
      channel = client.get_channel(message.channel.id)
      bsGame = bs.battleship()
      await message.channel.send("Started 2 player Battleship")
      await message.author.send(bsGame.showboards(1))
      await message.author.send("It's time to setup your ships. Enter ship type. ($carrier, $submarine, $destroyer, $cruiser, $battleship)")
      bsTypeStatus = 1

    if message.content in ['$carrier','$submarine', '$destroyer','$cruiser','$battleship'] and bsTypeStatus == 1:
      bsType = message.content.replace('$','')
      await message.author.send("Select a direction for your ship. ($left, $up, $right, $down")
      bsTypeStatus = 0
      bsDirectionStatus = 1

    if message.content in ['$left','$right','$up','$down'] and bsDirectionStatus == 1:
      bsDirection = message.content.replace('$','')
      await message.author.send("Select the coordinates for your ship. Eg $55")
      bsDirectionStatus = 0
      bsCoordinateStatus = 1

    try:
      if message.content.startswith('$') and message.content[1:3].isdigit() and bsCoordinateStatus == 1:
        bsCoordinates = message.content.replace('$','')
        await message.author.send("Which player is this? $1 or $2")
        bsCoordinateStatus = 0
        bsPlayerStatus = 1
    except:
      pass
    
    try:
      if message.content.startswith('$') and message.content[1:3].isdigit() and BSstatus == 1:
        shot = message.content.replace('$','')
        bsGame.checkhit(shot)
        
        if bsGame.turn%2==1:
          await message.author.send(bsGame.showboards(1))
        elif bsGame.turn%2==0:
          await message.author.send(bsGame.showboards(2))
        
        bsGame.check_gameover()
        if bsGame.end == True and bsGame.turn%2==0:
          await channel.send('Game Over P2 Won')
          BSstatus= 0
        elif bsGame.end == True and bsGame.turn%2==1:
          await channel.send('Game Over P1 Won')
          BSstatus= 0
        if bsGame.end == False and bsGame.turn%2==0 :
          await channel.send('P1 Turn to Shoot')
        elif bsGame.end == False and bsGame.turn%2==1:
          await channel.send('P2 Turn to Shoot')
    except:
      pass

    if message.content in ['$1','$2'] and bsPlayerStatus == 1:
      bsPlayer = int(message.content.replace('$',''))
      if bsGame.setships(bsType, bsDirection, bsCoordinates, bsPlayer) == 0:
        await message.author.send('There is already a ship there')
      if bsPlayer == 1 and not bsGame.ships_p1:
        await message.author.send('You have placed all your ships')
      elif bsPlayer == 2 and not bsGame.ships_p2:
        await message.author.send('You have placed all your ships')
      await message.channel.send(bsGame.showboards(bsPlayer))
      if not bsGame.ships_p1: #channel where the game started
        await channel.send("Enter another ship type.")
      else: #same channel
         await message.channel.send("Enter another ship type.")
      bsPlayerStatus = 0
      bsTypeStatus = 1
      if not bsGame.ships_p1 and not bsGame.ships_p2:
        await message.author.send('All ships are placed, start shooting!')
        await channel.send('P1 Turn to Shoot')
        BSstatus= 1
        



    #make it so that only the player who started the game can play, only 1 person can play
    if message.content.startswith('$PlayTTT'):
      await message.channel.send('Type the coordinates of where you want to play your piece at. eg: a1')
      tttPlayers = message.author.id
      tttGame = ttt.TicTacToe()
      tttStatus = 1

      embed=discord.Embed(title="TicTacToe", color=0x264af4)
      embed.add_field(name= message.author.name + " vs CPU", value=tttGame.PrintBoard(), inline=True)
      await message.channel.send(embed=embed)

    if message.content in ['a1','a2','a3','b1','b2','b3','c1','c2','c3'] and tttStatus == 1:
      if tttGame.CheckWin(tttGame.board) == False:
        tttGame.PlayerInput(message.content) 
        await message.channel.send('Your turn:')
        embed=discord.Embed(title="TicTacToe", color=0x264af4)
        embed.add_field(name= message.author.name + " vs CPU", value=tttGame.PrintBoard(), inline=True)
        await message.channel.send(embed=embed)
      if tttGame.CheckWin(tttGame.board) == False and tttGame.PlayerPlayed:
        tttGame.CPUTurn()
        await message.channel.send('CPU turn: ')
        embed=discord.Embed(title="TicTacToe", color=0x264af4)
        embed.add_field(name= message.author.name + " vs CPU", value=tttGame.PrintBoard(), inline=True)
        await message.channel.send(embed=embed)
      if tttGame.CheckWin(tttGame.board) == 'player':
        await message.channel.send('You win')
        tttStatus = 0
      elif tttGame.CheckWin(tttGame.board) == 'cpu':
        await message.channel.send('You lose')
        tttStatus = 0
      elif tttGame.CheckWin(tttGame.board) == 'tie':
        await message.channel.send('It\'s a tie')
        tttStatus = 0

    if message.content.startswith('$ExitTTT'):
      await message.channel.send('Game stopped, bye!')
      tttStatus = 0
    
    # if message.content.startswith('$Playbj'):
    #   bjgame = bj.Blackjack()

    # if message.content.startswith('$Playbj'):
    #   await message.channel.send('Lets play BlackJack')
    #   bjstatus = 0
    #   user_cards = [random.choice(list_of_cards), random.choice(list_of_cards)]
    #   bj.Blackjack()
      
      
    
    # if message.content.startswith('$hold') and bjstatus == 1:
    #   await message.channel.send('Test hold')



client.run(TOKEN)

