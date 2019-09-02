
# coding: utf-8

# In[5]:

#This is paper rock siscissors 
# u choose ur play first then pc makes its own #Have Fun 
from random import randint as ri
#EndGame=int(input('enter 1 to end game'))
me = int(input("choose any one from 1 to 3 : 1 is hgr 2 is wra'a 3 is ma'as  "))

pc = ri(1,3)


#while(EndGame!=1):
if 1<=me<=3 and 1<=pc<=3 :
    print("me : ",format(me) )
#print('\n')
    print("pc : ",format(pc)  )
#print('\n')
    while(me ==1)  :
        if pc ==1 :
            print('1 all ')
            break
        elif pc==2 :
            print('pc wins ')
            break
        elif pc==3 : 
            print('me wins')
            break
    
    while(me ==2)  :
        if pc ==1:
            print('me wins ')
            break
        elif pc==2 :
            print('1 all ')
            break
        elif pc==3 : 
            print('pc wins')
            break
    
    while(me ==3)  :
        if pc ==1 :
            print('pc wins ')
            break
        elif pc==2 :
            print('me wins ')
            break
        elif pc==3 : 
            print('1 all')
            break
        
else :
    print('error nums ')
    #break
    
        
#else :
    #print('end game !')
    #break



# 
