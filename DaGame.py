import random


pHealth=[1,1,1,1,1,1,1,1,1,1]
nHealth=[1,1,1,1,1,1,1,1,1,1]

pMana=[1,1,1,1,1]
nMana=[1,1,1,1,1]

whoseTurn=[0]

#dmg = random.randint
#heal = random.randint


def playerTurn():
    z=input('Attack or use spell? (a/s): ')
    if z.lower()=='a':
        attack()
    elif z.lower()=='s':
        spell()
    else:
        print('Skipping turn... ')

def npcTurn():
    print('npcTurn... (not working yet)')

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
   nHealth.pop(0)
   print('Attacked enemy! ')

def spell():
    nHealth.pop(0)

def main():
    while True:
        playerTurn()
        checkScore()
        npcTurn()
        checkScore()

main()
