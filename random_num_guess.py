
import random 

def computerguess(rand,i,j):

    a=1
    t=0
    while a>0:
        
        t+=1
        gen_rand=random.randint(i,j)
        u=input(f'Is {gen_rand} too high (H)? or too low ? (L),or correct? (C) :')
        print('')

        if u.lower()=='h' and gen_rand>int(rand):
            j=gen_rand-1
        elif u.lower()=='h' and (gen_rand>int(rand)) ==False:
            print('Liar Liar Bum on Fire')
            print('')
        elif u.lower()=='l' and gen_rand<int(rand):
            i=gen_rand+1
        elif u.lower()=='l' and (gen_rand<int(rand)) ==False:
            print('Liar Liar Bum on Fire')
            print('')


        elif u.lower()=='c' and gen_rand==int(rand):
            if t==1:
                print(f'The computer got it in {t} try !')
                print('')
            else:
                print(f'The computer got it in {t} tries!')
                print('')
            a-=1
        elif u.lower()=='c' and (gen_rand==int(rand))==False:
            print('Liar Liar Bum on Fire')

    print('')
    print('*------------*')    
    print('|GAME OVER !!|')
    print('*------------*') 
    print('')
    replay=input('Do you want to Play again? (Y/N): ')
    print('')
    if replay.lower()=='y':
        print('')
        print('*----------------*')    
        print('|Guesser = YOU !!|')
        print('*----------------*') 
        print('')
        rand=int(input('Enter the random number for computer to guess ):'))
        print('')
        computerguess(rand,0,100)
    
        
        
def youguess():
    a=1
    
    while a>0:
        lost=True
        print('')
        print('*----------------*')    
        print('|Guesser = YOU !!|')
        print('*----------------*') 
        print('')    
        com_num=random.randint(1,100)
        print('')
        print('Computer has genrated a number between 1 and 100, Can you guess the Number ?')
        print('')
        print('You get 10 tries , All The Best! :)')
        print('')
        i=10
        while i>0:
            user_num=int(input('Enter your guess between 1 and 100:'))
            if user_num>100:
                print('')
                print(f'The number {user_num} is greater than 100, Please enter a number between 1 and 100')
            elif user_num>com_num:
                print('')
                print(f'Your guessed number {user_num} is greater than the actual number')
                i-=1
                print(f'Remaning tires :{i}')
                
            elif user_num<com_num:
                print('')
                print(f'Your guessed number {user_num} is lesser than the actual number')
                i-=1    
                print(f'Remaning tires :{i}')
                
            elif user_num==com_num:
                print('')
                if i== 10:
                    print(f'Congrats the number is {user_num} and you got it Right in "{11-i}" try!!')
                else:
                    print(f'Congrats the number is {user_num} and you got it Right in "{11-i}" tries!!')
                lost=False
                break
        if lost==True:
            print('')
            print('You lost !!')
            print(f'The Number was {com_num}')
        print('')
        print('*------------*')    
        print('|GAME OVER !!|')
        print('*------------*') 
        print('')
        replay=input('Do you want to Retry? (Y/N): ')
        if replay.lower()=='n':
            break


print("*--------------------------------------*")
print("|                                      |")
print("| Welcome to the Number guessing game! |")
print("|  **********************************  |")
print("*--------------------------------------*")
print('')
print ('Select the mode .')
print('')
print('1. Let you guess the number.')
print('2. Let the computer guess your number. ')
print('3. Exit?')
mode=int(input('Select the mode you want to play. (1/2/3) :'))
print('')


if mode==1:
     youguess()
elif mode==2:
    print('')
    print('*---------------------*')    
    print('|Guesser = Computer !!|')
    print('*---------------------*') 
    print('')
    rand=input('Enter the random number for computer to guess :')
    print('')
    computerguess(rand,0,100)
elif mode==3:
    print('')
    print('*----------------*')    
    print('|SEE YOU AGAIN !!|')
    print('*----------------*')     
    exit()


   
