import random
import time
limb = ['left hand', 'right hand', 'left foot', 'right foot']
color = ['red', 'blue', 'green', 'yellow', 'in the air']
pain = ['kiss mom', 'jump in the air', 'scream at the top of your lungs for 10 seconds', 'bark 5 times very loudly', 'sing happy b-day at the top of your lungs']
doit = ['0', '0', '0', '1', '0', '0']
keepGoing = True
while keepGoing:
    ylimb = random.choice(limb)
    ycolor = random.choice(color)
    ypain = random.choice(doit)
    if ypain == '0':
            print(ylimb, ycolor)
    if ypain == '1':
        ypain1 = random.choice(pain)
        print(ylimb, ycolor, 'and', ypain1)
    time.sleep(10)
