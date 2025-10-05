import random

print('welcome to hand cricket')

select=input('ODD or EVEN:')

comp_input=random.randint(1,6)
player_input=int(input('enter the toss:'))

print('toss: YOU:'+ str(player_input))
print('toss: comp:'+str(comp_input))

status=""

if select=='EVEN':
    if ((comp_input+player_input)%2==0):
        status=input('BOWLING or BATTING ')
    else:
        choice=random.random()
        if choice<0.5:
            print('computer WON the toss and chose to BAT')
            status='BOWLING'
        else:
            print('computer WON the toss and chose to BOWL')
            status='BATTING'

if select=='ODD':
    if ((comp_input+player_input)%2==1):
        status=input('BOWLING or BATTING ')
    else:
        choice=random.random()
        if choice<0.5:
            print('computer WON the toss and chose to BAT')
            status='BOWLING'
        else:
            print('computer WON the toss and chose to BOWL')
            status='BATTING'

score=0
target=1
innings=1

while True:
    player_input=int(input('you: '+status+' innings '+str(innings)))
    comp_input=random.randint(1,6)
    print('you:'+str(player_input))
    print('comp:'+str(comp_input))

    if(comp_input==player_input):
        if(status=='BATTING' and innings==1):
            status='BOWLING'
            innings=2
            print('OUT...')
            print('to defent '+str(score))
        elif(status=='BOWLING' and innings==1):
            status='BATTING'
            innings=2
            print('OUT...')
            print('to get '+str(target))
        elif(status=='BATTING' and innings==2):
            print('you LOSS:( comp WIN the game!!')
            break
        elif(status=='BOWLING' and innings==2):
            print('comp LOSS:( you WIN the game!!')
            break
    else:
        if(status=='BATTING' and innings==1):
            score=score+player_input
            print('score:'+str(score))
        elif(status=='BATTING' and innings==2):
            if(target-player_input>0):
                target=target-player_input
                print('to get '+str(target))
            else:
                print('you WON the game:)')
                break
        elif(status=='BOWLING' and innings==1):
            target=target+comp_input
            print('score'+str(target))
        elif(status=='BOWLING' and innings==2):
            if(score-comp_input>0):
                score=score-comp_input
                print('to defent '+str(score))
            else:
                print('you LOST the game:(')
                break
