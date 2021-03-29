#import random


pHealth=[1,1,1,1,1,1,1,1,1,1]
nHealth=[1,1,1,1,1,1,1,1,1,1]

pMana=[1,1,1,1,1]
nMana=[1,1,1,1,1]

#dmg = random.randint
#heal = random.randint

whoseTurn=[0]

def playerTurn():
    z=input('Attack or use spell? (a/s): ')
    whoseTurn.pop(0)
    whoseTurn.append(1)
    if z.lower()=='a':
        attack()
    elif z.lower()=='s':
        spell()
    else:
        print('Skipping turn... ')

def npcTurn():
    whoseTurn.pop(0)
    whoseTurn.append(0)
    attack()

def checkScore():
    if len(pHealth)==0:
        print('NPC won! ')
        exit()
    elif len(nHealth)==0:
        print('Player won! ')
        exit()
    else:
        print('Player\'s Health: ',len(pHealth))
        print('NPC\'s Health: ',len(nHealth))
        print('Next turn! ')
    
def attack():
    if 1 in whoseTurn:
        nHealth.pop(0)
        print('Attacked enemy! \n')
    elif 0 in whoseTurn:
        pHealth.pop(0)
        print('Attacked player! \n')

def spell():
    nHealth.pop(0)

def main():
    while True:
        playerTurn()
        checkScore()
        npcTurn()
        checkScore()

main()
