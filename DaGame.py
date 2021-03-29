import random


pHealth=[]
nHealth=[]

for i in range(1,20):
    pHealth.append(1)
    nHealth.append(1)

pMana=[1,1,1,1,1]
nMana=[1,1,1,1,1]

#dmg = random.randint
#heal = random.randint

whoseTurn=[0]

def playerTurn():
    print('\nPLAYER\'s TURN\n')
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
    print('\n NPC\'s TURN\n')
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
    n=random.randint(1,3)
    if 1 in whoseTurn:
        for i in range(0,n):
            nHealth.pop(0)
            if len(nHealth)==0:
                break
            else:
                continue
        if n==1:
            print('Regular attack' )
        elif n==2:
            print('Lucky strike!' )
        elif n==3:
            print('CRITICAL ATTACK! ')
        print('Attacked enemy! \n')
    elif 0 in whoseTurn:
        for i in range(0,n):
            pHealth.pop(0)
            if len(pHealth)==0:
                break
            else:
                continue
        if n==1:
            print('Regular attack' )
        elif n==2:
            print('Lucky strike!' )
        elif n==3:
            print('CRITICAL ATTACK! ')
        print('Attacked player! \n')

def spell():
    nHealth.pop(0)

def main():
    while True:
        print('\n\n\n\n\n\n')
        playerTurn()
        checkScore()
        npcTurn()
        checkScore()

main()
